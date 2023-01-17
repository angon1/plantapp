from fastapi import FastAPI

from .db import PlantsLib
from .db_config import start_db, start_session
from .utils import parse_plant_info_csv, write_plant_lib_to_db

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


_df = parse_plant_info_csv()
_db_engine = start_db()
write_plant_lib_to_db(engine=_db_engine, df=_df)

app = get_application()

_session = start_session(_db_engine)


def get_db_engine():
    return _db_engine


def get_session():
    return _session


@app.get("/plantslib/")
def plants_library():
    # obiekty z plantslib - z db
    return {"Hello": "Welcome to PlantApp. We know many plants"}


@app.get("/plantslib/{name}")
def plants_library_output(name: str):
    session = get_session()

    plant = session.query(PlantsLib.name).all()
    print(plant)
    return {"Hello": f"This is description of {plant}"}


# @app.get("/plantslib/search/")
# def search(
#     request: Request, db: Session = Depends(get_db_engine), query: Optional[str] = None
# ):
#     jobs = search_job(query, db=db)
#     return templates.TemplateResponse(
#         "general_pages/homepage.html", {"request": request, "jobs": jobs}
#     )


@app.get("/")
def read_index():
    return {"Hello": "Welcome to PlantApp"}
