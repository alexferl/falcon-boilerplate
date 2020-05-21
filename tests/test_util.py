from app import configure
from app.config import settings


def test_config_override():
    configure()

    assert settings.get("APP_NAME") == "app"

    configure(app_name="new_name")

    assert settings.get("APP_NAME") == "new_name"
