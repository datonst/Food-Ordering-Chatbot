## 1\. Food Ordering Chatbot

Food Ordering Chatbot a simple chatbot project designed for the Human-Machine Interface course. The chatbot is built with LlamaIndex and integrates RAG techniques.

This is a web application that supports voice-activated food ordering for people with hand disabilities, featuring voice control and audio responses. The web application aims to improve the quality of life for people with disabilities, enabling them to be more independent and integrated into the community.

***

## 2\. Setting Up the Application on Your Machine

### 2.1. Preparing the Environment

Ensure you have the following tools installed on your machine:
- Python 3.8+
- Git to clone the source code.
- Node.js (if the project requires a web interface).
- Docker (optional, if you want to deploy in a container).

### 2.2. Clone the Repository

Clone the source code to your machine using the following command:
```bash
git clone https://github.com/datonst/chatbot-TTNM
```

### 2.3. Installing Dependencies

Using pip:
- Step 1: `python3 -m venv venv`
- Step 2: `source venv/bin/activate` # On macOS/Linux or `venv\Scripts\activate` # On Windows
- Step 3: `pip install -r requirements.txt`

If the project uses Poetry:
```bash
poetry install
```

#### 2.3.1. Deploying in a Real Environment

**Docker**: If there is a Dockerfile, build the container:
```bash
docker build -t llm-food-delivery .
docker run -p 8000:8000 llm-food-delivery
```
- Ensure you upload the `.env` file and configure the environment variables correctly.
```