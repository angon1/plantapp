from fastapi import FastAPI

from .db_config import start_db

"""
FastAPI(
    *,
    debug=False,
    routes=None,
    title="FastAPI",
    description="",
    version="0.1.0",
    openapi_url="/openapi.json",
    openapi_tags=None,
    servers=None,
    dependencies=None,
    default_response_class=Default(JSONResponse),
    docs_url="/docs",
    redoc_url="/redoc",
    swagger_ui_oauth2_redirect_url="/docs/oauth2-redirect",
    swagger_ui_init_oauth=None,
    middleware=None,
    exception_handlers=None,
    on_startup=None,
    on_shutdown=None,
    terms_of_service=None,
    contact=None,
    license_info=None,
    openapi_prefix="",
    root_path="",
    root_path_in_servers=True,
    responses=None,
    callbacks=None,
    deprecated=None,
    include_in_schema=True,
    swagger_ui_parameters=None,
    generate_unique_id_function=Default(generate_unique_id),
    **extra
)

"""


def get_application() -> FastAPI:
    application = FastAPI(
        docs_url="/docs",
        redoc_url="/redoc",
        title="PlantApp",
    )
    return application


app = get_application()
_db_engine = start_db()


def get_db_engine():
    return _db_engine


@app.get("/plantslib/")
def plants_library_output():
    return {"Hello": "Welcome to PlantApp"}


@app.get("/")
def read_index():
    return {"Hello": "Welcome to PlantApp"}
