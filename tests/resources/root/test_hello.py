import falcon


def test_get_returns_hello_name(client):
    doc = {"message": "Hello, Bob!"}
    result = client.simulate_get("/hello/bob")

    assert result.status == falcon.HTTP_OK
    assert result.json == doc
