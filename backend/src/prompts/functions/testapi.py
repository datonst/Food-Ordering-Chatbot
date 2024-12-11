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
from pathlib import Path


model_args = {
        "temperature": 0.9,
        "top_p": 1,
        # "frequency_penalty": 0,
        # "presence_penalty": 0,
}
# genai.protos.Tool(ALL_ALLOWED_FUNCTIONS)
model = genai.GenerativeModel(
    'gemini-1.5-flash-8b',
    tools = ALL_ALLOWED_FUNCTIONS,
    generation_config=genai.GenerationConfig(**model_args),
    )
print(ALL_ALLOWED_FUNCTIONS)
system_prompt = Path("../chat/system.txt").read_text()
print(system_prompt)
chat = model.start_chat(enable_automatic_function_calling=True,history=[])
prompt= "tìm cho tôi một cửa hàng nhật bản với đồ ăn pizza ngon"
response = chat.send_message(system_prompt+prompt)
model.generate_content()

response=json.dumps(response, indent=4)
response_dict = json.loads(response)

print(jsonable_encoder(str(response_dict)))

# response2 = chat.send_message(
#     """
#     Based on this information: `""" + str(response) + """` 
#     and this question: `""" + prompt + """`
#     respond to the user in a friendly manner.
#     """,
# )
# print(response)
    