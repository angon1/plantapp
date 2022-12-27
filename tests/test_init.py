from plantapp.db_config import create_db_connection


def test_something(mocker):
    mocker.patch("plantapp.db_config.create_url", return_value="url")
    create_db_connection()


def test_import_app():
    """Test"""
    import plantapp

    assert plantapp is not None
