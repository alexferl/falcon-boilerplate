import falcon


def test_get_welcome_message(client):
    doc = {"message": "Hello, World!"}
    result = client.simulate_get("/")

    assert result.status == falcon.HTTP_OK
    assert result.json == doc
