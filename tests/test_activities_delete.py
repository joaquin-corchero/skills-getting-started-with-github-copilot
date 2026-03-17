def test_unregister_success_removes_participant(client):
    email = "michael@mergington.edu"

    response = client.delete(f"/activities/Chess Club/participants?email={email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from Chess Club"

    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]
    assert email not in participants


def test_unregister_returns_404_when_activity_missing(client):
    response = client.delete("/activities/Unknown Club/participants?email=student@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_404_when_student_not_signed_up(client):
    response = client.delete("/activities/Chess Club/participants?email=not-there@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"
