from pydantic import BaseModel, EmailStr, root_validator
from typing import Optional, List, Any, Dict

## OpenAI schema for Chat Completion
class FunctionCall(BaseModel):
    name: str
    args: Any

class Message(BaseModel):
    content: str
    role: str
    function_call:FunctionCall
    
class Choices(BaseModel):
    finish_reason: str
    index: int
    message: Message

class Usage(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int

class OpenAIChatCompletionResponse(BaseModel):
    choices: Message
    created: int
    id: str
    model: str
    object: str
    usage: Usage

## Message System
class InputMessage(BaseModel):
    role: str
    content: Any
    name: Optional[str] = None

class InputChatHistory(BaseModel):
    history: List[InputMessage]

class ChatRequest(BaseModel):
    query: InputChatHistory
    function_call: bool=True


## Audio system
class AudioTranscriptRequest(BaseModel):
    audio: str
class AudioResponse(BaseModel):
    message: str

class AudioTTSRequest(BaseModel):
    text: str



class Login(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: str
    @root_validator(pre=True)
    def check_username_or_email(cls, values):
        username, email = values.get('username'), values.get('email')
        if not username and not email:
            raise ValueError("Either username or email must be provided")
        return values

class Register(BaseModel):
    username: str
    fullname: str
    email: EmailStr
    password: str

class UpdateProfile(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
    @root_validator(pre=True)
    def check_at_least_one_field(cls, values):
        email, full_name, password = values.get('email'), values.get('full_name'), values.get('password')
        if not any([email, full_name, password]):
            raise ValueError("At least one of email, full_name, or password must be provided")
        return values

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

