
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import sys
import dotenv
dotenv.load_dotenv()
your_path = os.getenv("YOUR_PATH")
sys.path.append(f'{your_path}/chatbot-TTNM/backend')

from src.config import CONFIG
from src.endpoints import include_all_routers
from src.handlers import MainHandler

# Integrating SQLite
from src.data import data_models
from src.data import SessionLocal, engine

data_models.Base.metadata.create_all(bind=engine)




print(f'Your path: {your_path}')
class Application:
    @classmethod
    def setup(cls, app: FastAPI, handler: MainHandler, CONFIG):
        # Adding CORS middleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
            expose_headers=["*"],
        )

        # Registering routers and exception handlers
        include_all_routers(app, handler, CONFIG)

        return app


app = FastAPI(
    title="Auto food order",
    description="Auto food prototype implementation",
)

app = Application.setup(app, MainHandler(), CONFIG)

# Running the app
if __name__ == "__main__":

    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, workers=1
    )
