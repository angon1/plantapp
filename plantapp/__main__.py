import uvicorn

from .db_config import start_db
from .utils import parse_plant_info_csv, write_plant_lib_to_db

df = parse_plant_info_csv()
engine = start_db()
write_plant_lib_to_db(engine=engine, df=df)

uvicorn.run("plantapp.app:app", reload=True, host="0.0.0.0", port=8888)
