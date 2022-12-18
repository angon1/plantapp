import pytest

from plantapp.db_config import create_url, start_db


@pytest.fixture
def plant_name():
    return "kaktus"


@pytest.fixture
def db_connection():
    return start_db()


@pytest.fixture
def db_url():
    return create_url()
