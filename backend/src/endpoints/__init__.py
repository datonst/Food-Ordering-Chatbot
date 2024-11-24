"""Routers class"""
from fastapi.applications import FastAPI
from src.endpoints import routers, health_check

def include_all_routers(app: FastAPI, handler, CONFIG) -> FastAPI:
    """
    Add all routers to the FastAPI app
    """
    app.include_router(health_check.router)

    router = routers.create_router(handler, CONFIG)
    app.include_router(router)

    return app