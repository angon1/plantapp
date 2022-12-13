import uvicorn

from .db_config import start_db

start_db()
uvicorn.run("plantapp.app:app", reload=True, host="0.0.0.0", port=8888)
