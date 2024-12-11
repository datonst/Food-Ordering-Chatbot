from tenacity import retry, wait_random, stop_after_attempt
import pickle
@retry(wait=wait_random(min=1, max=5), stop=stop_after_attempt(5))
async def chat_completion(messages, CONFIG, functions=[], client=None):
    """Receives the chatlog from the user and answers"""

    # Initializing the openai configuration
    CFG_OPENAI = CONFIG["openai"]

    model_args = {
        "model": CFG_OPENAI.get("chat_model", "gpt-4o-mini"),
        "temperature": CFG_OPENAI.get("temperature", 0),
        "max_tokens": CFG_OPENAI.get("max_tokens", 512),
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "messages": messages
    }

    # Incrementing in cases of function calling
    if len(functions) > 0:
        model_args["tools"] = functions

    # response = "client.chat.completions.create(**model_args)"
    # print(functions)

    response = client.chat.completions.create(**model_args)
    # with open('data.pkl', 'rb') as f:
    #     response =  pickle.load(f)
    # Returning raw response
    return response