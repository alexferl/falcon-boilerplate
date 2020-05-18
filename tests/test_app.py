from app import start


def test_app_start_log(caplog):
    start()
    assert "Starting" in caplog.text
