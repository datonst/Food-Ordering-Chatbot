
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core.storage import StorageContext
from llama_index.core import VectorStoreIndex, Document, ServiceContext
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import Settings

def load_pinecone_index(index_name, CONFIG):
    """Loads the pinecone index from the index_name"""
    model_name = "models/text-embedding-004"
    CFG_GEMINI = CONFIG["gemini"]
    GOOGLE_API_KEY=CFG_GEMINI["api_key"]
    embed_model = GeminiEmbedding(model_name=model_name, api_key=GOOGLE_API_KEY)
    # llm = OpenAI(model="gpt-4")
    Settings.embed_model = embed_model
    
    vector_store = PineconeVectorStore(
        index_name=index_name,
        environment=CONFIG["pinecone"]["environment"],
        api_key=CONFIG["pinecone"]["api_key"],
    )

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    index = VectorStoreIndex([], storage_context=storage_context,)

    return index

def get_retriever(index_name: str, top_k:int,  CONFIG, **kwargs):
        """Returns a retriever object from a pinecone index"""

        # Loads the index
        index = load_pinecone_index(index_name, CONFIG)

        # Returns the retriever
        return index.as_retriever(similarity_top_k=top_k, **kwargs)
    