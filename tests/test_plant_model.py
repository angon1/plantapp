from sqlalchemy_utils import database_exists

from plantapp.db import Plant


def test_plant_creation(plant_name):
    my_plant = Plant(name=plant_name)

    assert my_plant is not None
    assert my_plant.name == plant_name


def test_start_db(db_connection, db_url):
    print(db_connection)

    assert database_exists(db_url)
