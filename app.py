import os
import uvicorn
from tkww_api import create_app


def run():
    """
    Run the FastAPI application with Uvicorn.
    """
    # Configuration settings
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 80))

    app = create_app()
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    run()
