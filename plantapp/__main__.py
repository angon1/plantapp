import uvicorn

from .app import get_db_engine
from .utils import parse_plant_info_csv, write_plant_lib_to_db

df = parse_plant_info_csv()
engine = get_db_engine()
write_plant_lib_to_db(engine=engine, df=df)


uvicorn.run("plantapp.app:app", reload=True, host="0.0.0.0", port=8888)
