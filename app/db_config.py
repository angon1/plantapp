import sqlalchemy
import sqlalchemy_utils


def create_db_connection(name: str = "plantapp_db_1"):
    db = f"postgresql+psycopg2://example:example@plantapp_db/{name}"
    print(db)
    engine = sqlalchemy.create_engine(db, echo=True, future=True)
    return engine


def create_db(engine: sqlalchemy.engine.Engine):
    if not sqlalchemy_utils.database_exists(engine.url):
        sqlalchemy_utils.create_database(engine.url)
    else:
        pass


def start_session(engine: sqlalchemy.engine.Engine):
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    return session


def start_db(db_name: str = "plantapp_db_1"):
    engine = create_db_connection(db_name)
    create_db(engine)
    return start_session(engine)
