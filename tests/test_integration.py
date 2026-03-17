def test_signup_then_unregister_round_trip(client):
    email = "round.trip@mergington.edu"

    signup_response = client.post(f"/activities/Programming Class/signup?email={email}")
    assert signup_response.status_code == 200

    activities_after_signup = client.get("/activities").json()
    assert email in activities_after_signup["Programming Class"]["participants"]

    unregister_response = client.delete(
        f"/activities/Programming Class/participants?email={email}"
    )
    assert unregister_response.status_code == 200

    activities_after_unregister = client.get("/activities").json()
    assert email not in activities_after_unregister["Programming Class"]["participants"]


def test_state_is_reset_between_tests(client):
    activities = client.get("/activities").json()

    # If this appears, another test leaked state into this one.
    assert "round.trip@mergington.edu" not in activities["Programming Class"]["participants"]
