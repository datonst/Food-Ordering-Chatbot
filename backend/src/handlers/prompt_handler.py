
# Typing hints
from typing import Optional

# Configuration and helpers
from fastapi.encoders import jsonable_encoder
from src.config import CONFIG
from src.prompts.functions import ALL_ALLOWED_FUNCTIONS

# Importing schemas and hints
from src.schemas import ChatRequest

# Utils
import json


CFG_PROMPTS = CONFIG["prompts"]
CFG_CHAT = CFG_PROMPTS["chat"]
CFG_FUNCTIONS = CFG_PROMPTS["functions"]



# Utils
from pathlib import Path

import os
print("Current working directory:", os.getcwd())
## Creating handler
class PromptHandler():
    def __init__(
        self,
    ):
        pass

    def get_messages(self, prompt_request):
        """Gets the chatlog from the user and prepares the prompt for the system"""
        file_path = Path(CFG_CHAT["filepath"])
        # Check if the file exists
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        # Read the file
        with file_path.open("r") as file:
            content = file.read()
        # Gets the system prompt and injects context
        system_prompt = Path(CFG_CHAT["filepath"]).read_text()

        # Retrieves the chat log
        chatlog = jsonable_encoder(prompt_request.query.history)

        # Formatting - removes "name" parameter from non-functional inputs
        chatlog = [
            {"role": message["role"], "content": message["content"]}
            if message["role"] != "function"
            else {
                "role": message["role"],
                "content": message["content"],
                "name": message["name"],
            }
            for message in chatlog
        ]

        # Merges all together
        messages = [{"role": "system", "content": system_prompt}] + chatlog

        return messages

    def prepare_response(self, response):
        """Formats the response from the system"""
  
        print("-----------------------------------")
        content = response.choices[0].message.content
        if content is None:
            function_call = response.choices[0].message.tool_calls[0].function
            print(function_call)
        else:
            function_call = False
        return {
            "response": content,
            "function_call": function_call,
        }

    
    def get_functions(self,):
        """Returns the functions signatures"""
        return ALL_ALLOWED_FUNCTIONS
