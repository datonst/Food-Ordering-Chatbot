
# Typing hints
from typing import Optional

# Configuration and helpers
from fastapi.encoders import jsonable_encoder
from src.config import CONFIG
from src.prompts.functions import ALL_ALLOWED_FUNCTIONS
from google.protobuf.json_format import MessageToDict
# Importing schemas and hints
from src.schemas import ChatRequest

# Utils
import json


CFG_PROMPTS = CONFIG["prompts"]
CFG_CHAT = CFG_PROMPTS["chat"]
CFG_FUNCTIONS = CFG_PROMPTS["functions"]


# Utils
from pathlib import Path


## Creating handler
class PromptHandler():
    def __init__(
        self,
    ):
        pass

    def get_messages(self, prompt_request):
        """Gets the chatlog from the user and prepares the prompt for the system"""

        # Gets the system prompt and injects context
        system_prompt = Path(CFG_CHAT["filepath"]).read_text()

        # Retrieves the chat log
        chatlog = jsonable_encoder(prompt_request.query.history)

        # Formatting - removes "name" parameter from non-functional inputs
        chatlog = [
            {"role": "model" if message["role"] == "assistant" else message["role"]
             ,"parts": message["content"]}
            if message["role"] != "function"
            else {
                "role": "model" if message["role"] == "assistant" else message["role"],
                "parts": message["content"],
                "name": message["name"],
            }
            for message in chatlog
        ]
        prompt = [{"role": "user", "parts": f"System prompt: {system_prompt}"},
                 {"role": "model","parts": "Understood."}]
        # Merges all together
        messages = prompt + chatlog
        return messages

    def prepare_response(self, response):
        """Formats the response from the system"""
        value = self.filter_response(response)
        function_call = None
        text = None
        if "function_call" in value:
            function_call=value["function_call"]
        else:
            text = value["text"]
        # text= None
        # if "function_call" not in function_value:
        #     function_call = None
        #     text = response.text
        #     print("function_call is None")
        # else :
        #     function_call = function_value.function_call
        #     ffunction_call
        #     function_call = json.dumps(function_call_dict, indent=4)
        #     print(function_call)
        return {
            'response': text,
            'function_call': function_call,
        }

    def filter_response(self, response):
        """Filters the response from the system"""
        response=json.dumps(response.to_dict(), indent=4)
        response_dict = json.loads(response)
        value = response_dict['candidates'][0]['content']['parts'][0]
        return value
    
    def add_prompt(self, messages,response):
        prompt = [{"role": "model"
                   ,"parts": f"My response your question is: {response}"}
                  ,{"role": "user", "parts": "What is that?"}
                ]
        # Merges all together
        messages = messages + prompt
        return messages
    
    def get_functions(self,):
        """Returns the functions signatures"""
        return ALL_ALLOWED_FUNCTIONS
