# Env variables loader
import os
import dotenv
dotenv.load_dotenv(dotenv_path="../../.env")

# Data handlers
import pandas as pd
from sqlalchemy.orm import Session

# Utils
try:
    from data_utils import get_db, get_restaurants, get_foods
    from data_models import Restaurant, Foods
    from database import SessionLocal
except:
    from .data_utils import get_db, get_restaurants, get_foods
    from .data_models import Restaurant, Foods
    from .database import SessionLocal

# Llamaindex

# imports
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core.storage import StorageContext
from llama_index.core import VectorStoreIndex, Document, ServiceContext
from llama_index.core import  SimpleDirectoryReader
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core.vector_stores import ExactMatchFilter
from llama_index.core import Settings
import google.generativeai as genai
# VDBs
#import weaviate
import pinecone
ENVIRONMENT = "gcp-starter"
INDEX_NAME = "auto-food-order"
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

def process_restaurants():
    # Reading SQLite db
    db = SessionLocal()
    restaurants = get_restaurants(db)
    foods = get_foods(db)

    # Convert the data to a pandas DataFrame
    restaurant_data = [{"id": r.id, "name": r.name, "description": r.description,} for r in restaurants]
    restaurant_df = pd.DataFrame(restaurant_data)

    food_data = [{"id": f.id, "restaurant_id": f.restaurant_id, "name": f.name, "description": f.description, "price": f.price} for f in foods]
    food_df = pd.DataFrame(food_data)

    # Processing for merge: renaming columns
    food_df = food_df.rename(
        columns={
            "id": "food_id",
            "restaurant_id": "id",
            "name": "food_name",
            "description": "food_description",
        }
    )
    

    # Merging
    df = pd.merge(restaurant_df, food_df, on="id")

    # Groupby restaurant and creating text for embedding
    df["food_text"] = "\n-"+df["food_name"] + "\n" + df["food_description"]

    df = df.groupby("id").agg({"name": "first", "description": "first", "food_text": "sum"}).reset_index()
    
    # Creating text for embedding
    df["text"] = "```" + df["name"] + "\nRestaurant description: " + df["description"] + "\nFood available:" + df["food_text"] + "\n```"

    # Llamaindex
    documents = [
        Document(
            text=df_row[1]["text"],
            metadata={
                "search_type": "restaurant",
                "restaurant_id": df_row[1]["id"],
                "restaurant_name": df_row[1]["name"],
                "restaurant_description": df_row[1]["description"],
                "restaurant_menu": df_row[1]["food_text"],
            }
        )
        for df_row in df.iterrows()
    ]

    vector_store = PineconeVectorStore(
        index_name=INDEX_NAME,
        environment=ENVIRONMENT,
    )

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store,
    )
    model_name = "models/text-embedding-004"
    embed_model = GeminiEmbedding(model_name=model_name, api_key=GOOGLE_API_KEY)
    # llm = OpenAI(model="gpt-4")
    Settings.embed_model = embed_model
    
    index = VectorStoreIndex.from_documents(
        documents=documents,
        storage_context=storage_context,
    )
    # index.index_struct.index_id 

    return index

def load_index():
    vector_store = PineconeVectorStore(
        index_name=INDEX_NAME,
        environment=ENVIRONMENT,
        # add_sparse_vector=True,
    )

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    # loaded_index = VectorStoreIndex.from_vector_store(vector_store)
    index = VectorStoreIndex([], storage_context=storage_context,)

    return index

def main():
    # Testing it
    index= process_restaurants()
    idx = load_index()
    
    # qe = idx.as_query_engine()
    ret = idx.as_retriever(similarity_top_k=5)
    ret2 = idx.as_retriever(
        similarity_top_k=5,
        filter=[ExactMatchFilter(key="search_type", value="restaurant")]
    )
    bm25 = idx.as_retriever(similarity_top_k=5, vector_store_query_mode="hybrid", alpha=0.0)
    hret = idx.as_retriever(similarity_top_k=5, vector_store_query_mode="hybrid", alpha=0.75)
    hsnw = idx.as_retriever(similarity_top_k=5, vector_store_query_mode="hybrid", alpha=1.0)
    
    # Testing 
    answers = {
        "regular": [],
        "regular_filtered": [],
        "bm25": [],
        "hybrid_retriever": [],
        "hsnw": [],
    }
    query = "testing, I would like to order a large pizza with mango, thai food, taco fiesta"
    model= genai.GenerativeModel(
            'gemini-1.5-flash-8b',
            # tools = functions,
            # generation_config=genai.GenerationConfig(),
        )
    chat = model.start_chat(enable_automatic_function_calling=True,history=[])
    response = chat.send_message(query)
    print(response)
    
    for retriever in [
        (ret, "regular"),
        (ret2, "regular_filtered"),
        (bm25, "bm25"),
        (hret, "hybrid_retriever"),
        (hsnw, "hsnw")
    ]:
        ans = retriever[0].retrieve(query)
        for response in ans:
            answers[retriever[1]].append(
                (
                    response.node.metadata["restaurant_name"],
                    response.score,
                    # response.node.text,
                )
            )
    # Printing in ordered by score for all the retrievers
    print("Query: ", query)
    for retriever in answers:
        print(f"Retriever: {retriever}")
        for ans in sorted(answers[retriever], key=lambda x: x[1], reverse=True):
            print(ans)
        print("\n\n")


if __name__ == "__main__":
    main()