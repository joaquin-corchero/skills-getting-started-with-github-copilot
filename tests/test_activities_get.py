def test_get_activities_returns_expected_shape(client):
    response = client.get("/activities")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == 9


def test_get_activities_include_required_fields(client):
    response = client.get("/activities")
    data = response.json()

    chess = data["Chess Club"]

    assert "description" in chess
    assert "schedule" in chess
    assert "max_participants" in chess
    assert "participants" in chess
    assert isinstance(chess["participants"], list)
