from tenacity import retry, wait_random, stop_after_attempt

@retry(wait=wait_random(min=1, max=5), stop=stop_after_attempt(5))
async def embeddings(content, CONFIG, client=None):
    """Receives a content in text and embeds it"""
    CFG_GEMINI = CONFIG["gemini"]
    # Initializing the openai configuration
    # CFG_OPENAI = CONFIG["openai"]

    # model_args = {
    #     "model": CFG_OPENAI["embedding_model"],
    # }

    # # Calling the engine
    # model_args["input"] = content

    # response = openai.Embedding.create(
    #     **model_args
    # )["data"][0]["embedding"]
    
    # response = client.embeddings.create(**model_args)["data"][0]["embedding"]
    # print("embedding model")
    client.configure(api_key=CFG_GEMINI["api_key"])
    response = client.embed_content(model="models/text-embedding-004", content=content)
    print(response)
    return response