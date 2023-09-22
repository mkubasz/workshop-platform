
def test_signup(httpx_mock, client):
    httpx_mock.add_response(status_code=201)
    response = client.post("/signup",
                           json={
                               "discord_id": "1234",
                               "name": "test",
                               "password": "test",
                               "email": "test",
                               "invoice": "test"
                           })
    assert response.status_code == 201

