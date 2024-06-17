from fastapi import FastAPI
from tkww_api.controllers.model_controller import router as model_router
from tkww_api.utils.logger import Log


def create_app() -> FastAPI:
    """
    Application factory function for creating a FastAPI application instance.
    """
    app = FastAPI(title="TKWW API", version="1.0.0")

    # Initialize logging
    Log.init_app(app)

    # Include routers
    app.include_router(model_router)

    return app
