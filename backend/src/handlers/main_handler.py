# Handlers 
from .prompt_handler import PromptHandler
from .audio_handler import AudioHandler
from .vectordb_handler import VectorDBHandler

# Abstract class creation
from abc import ABC, abstractmethod

# Typing hints
from typing import Optional

# CONFIG
from ..config import CONFIG
import google.generativeai as genai
# OpenAI
import openai
import dotenv
import os
dotenv.load_dotenv(dotenv_path="../../../.env")
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

## Creating main handler
class MainHandler(ABC):
    def __init__(self,):
        self.openai_client = genai
        self.prompt_handler = PromptHandler()
        self.audio_handler = AudioHandler()
        self.vectordb_handler = VectorDBHandler()
        