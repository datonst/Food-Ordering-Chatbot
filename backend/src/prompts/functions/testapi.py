import google.generativeai as genai
import dotenv
import os
from hello import ALL_ALLOWED_FUNCTIONS
from fastapi.encoders import jsonable_encoder
import json
from google.protobuf.json_format import MessageToDict
dotenv.load_dotenv(dotenv_path="../../../.env")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)


model_args = {
    "temperature": 0.9,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}
# genai.protos.Tool(ALL_ALLOWED_FUNCTIONS)
model = genai.GenerativeModel(
    'gemini-1.5-flash-8b',
    tools = ALL_ALLOWED_FUNCTIONS,
    
    generation_config=genai.GenerationConfig(**model_args),
    )
chat = model.start_chat(history=[])
prompt= "hello"
response = chat.send_message(prompt)

response=json.dumps(response.to_dict(), indent=4)
response_dict = json.loads(response)

print(['text'])

# response2 = chat.send_message(
#     """
#     Based on this information: `""" + str(response) + """` 
#     and this question: `""" + prompt + """`
#     respond to the user in a friendly manner.
#     """,
# )
# print(response)
    