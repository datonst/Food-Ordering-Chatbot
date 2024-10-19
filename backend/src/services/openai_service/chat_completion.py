from tenacity import retry, wait_random, stop_after_attempt
import dotenv
import os

@retry(wait=wait_random(min=1, max=5), stop=stop_after_attempt(5))
async def chat_completion(messages, CONFIG, functions=[], client=None):
    """Receives the chatlog from the user and answers"""

    # Initializing the openai configuration
    CFG_GEMINI = CONFIG["gemini"]

    model_args = {
        "temperature": 0.0,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }
    print(CFG_GEMINI["api_key"])
    client.configure(api_key=CFG_GEMINI["api_key"])
    model = client.GenerativeModel(
        'gemini-1.5-flash-8b',
        tools = functions,
        generation_config=client.GenerationConfig(**model_args),
    )
    # print(messages)
    chat = model.start_chat(enable_automatic_function_calling=True, history = messages[:-1])
    response = chat.send_message(messages[-1]["parts"])
    print(response)
    return response
    # Incrementing in cases of function calling
    # if len(functions) > 0:
    #     model_args["functions"] = functions
    #     model_args["function_call"] = "auto"

    # response = client.chat.completions.create(**model_args)

    # Returning raw response
