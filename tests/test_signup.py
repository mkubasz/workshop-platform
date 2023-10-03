
def test_signup(client):
    response = client.post("/signup",
                           json={
                               "discord_id": "1234",
                               "name": "test",
                               "password": "test123456",
                               "email": "test@test.pl",
                               "invoice": "test"
                           })
    assert response.status_code == 201

