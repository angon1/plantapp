import plantapp
from plantapp.db_config import create_db_connection, create_url


def test_create_url_default():
    """Unit test for testing default url for data base"""
    assert (
        create_url()
        == "postgresql+psycopg2://plant_admin:plant_password@localhost:5432/plantapp_db"
    )


def test_create_db_connection_default(mocker):
    mocker.patch("plantapp.db_config.create_url", return_value="url")
    mocker.patch("plantapp.db_config.create_engine", return_value="engine")
    assert "engine" == create_db_connection()
    plantapp.db_config.create_url.assert_called_once()
    plantapp.db_config.create_engine.assert_called_once_with(
        "url", echo=True, future=True
    )
