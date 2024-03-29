from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from .db import Base, Plant, PlantsLib  # for Base.metadata.create_all() usage


def create_url(
    username: str = "plant_admin",
    password: str = "plant_password",
    host: str = "localhost",
    port: str = "5432",
    db_name="plantapp_db",
    driver: str = "postgresql+psycopg2",
):
    # Todo Prepare config from env. Remove default values - keeping them only for development purpose.
    url_string = f"{driver}://{username}:{password}@{host}:{port}/{db_name}"
    return url_string


def create_db_connection(name: str = "plantapp_db"):
    db_url = create_url()
    engine = create_engine(db_url, echo=False, future=True)
    return engine


def create_db(engine: Engine):
    if not database_exists(engine.url):
        create_database(engine.url)
    else:
        pass


def start_session(engine: Engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def create_tables(engine: Engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def start_db(db_name: str = "plantapp_db"):
    engine = create_db_connection(db_name)
    create_db(engine)
    create_tables(engine)
    session = start_session(engine)
    print("dupadupaadpdaudpaa")
    print(session.query(PlantsLib).filter_by(name="Amaranth").all())
    return engine
