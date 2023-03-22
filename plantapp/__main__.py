import uvicorn

uvicorn.run("plantapp.app:app", reload=True, host="0.0.0.0", port=8888)
