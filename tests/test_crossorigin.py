try:
    import falcon_crossorigin
except ImportError:
    falcon_crossorigin = None

import pytest

from app import configure, create_app

skip_missing_dep = pytest.mark.skipif(
    falcon_crossorigin is None, reason="falcon-crossorigin dependency not found"
)


@skip_missing_dep
def test_crossorigin_available():
    from app import crossorigin_available

    assert crossorigin_available


@skip_missing_dep
def test_crossorigin_unavailable(monkeypatch):
    import app.app

    monkeypatch.setattr(app.app, "crossorigin_available", False)
    with pytest.raises(ImportError):
        configure(cors_enabled=True)
        create_app()


@skip_missing_dep
def test_crossorigin_enabled():
    configure(cors_enabled=True)
    app = create_app()

    assert (
        app._middleware[2][0].__func__
        == falcon_crossorigin.CrossOrigin.process_response
    )
