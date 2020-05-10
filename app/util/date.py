from datetime import datetime


def get_isoformat() -> str:
    return datetime.now().isoformat("T")
