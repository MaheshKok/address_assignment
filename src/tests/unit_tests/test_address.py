def test_create_address(app):
    address_payload = {
        "latitude": 23.0,
        "longitude": 45.0,
        "pin_code": 411678,
        "primary": True,
    }
    response = app.post(
        "/api/v1/address",
        json=address_payload,
    )
    assert response.status_code == 201
    assert response.json()["latitude"] == address_payload["latitude"]


def test_get_address(app):
    address_payload = {
        "latitude": 23.6,
        "longitude": 45.7,
        "pin_code": 411678,
        "primary": True,
    }

    create_address_response = app.post(
        "/api/v1/address",
        json=address_payload,
    )
    address_id = create_address_response.json()["id"]
    response = app.get(
        f"/api/v1/address/{address_id}",
    )
    assert response.status_code == 200
    assert response.json()["id"] == address_id


def test_search_address(app):
    address_payload_list = [
        {
            "latitude": 23.6,
            "longitude": 45.7,
            "pin_code": 411678,
            "primary": True,
        },
        {
            "latitude": 53.6,
            "longitude": 55.7,
            "pin_code": 413678,
            "primary": False,
        },
        {
            "latitude": 13.6,
            "longitude": 15.7,
            "pin_code": 416678,
            "primary": False,
        },
    ]

    for address_payload in address_payload_list:
        app.post(
            "/api/v1/address",
            json=address_payload,
        )

    response = app.get(
        f"/api/v1/address?latitude=15&longitude=16",
    )


# improvements
# use sentry for errors logging
# use factory for unit test
# use FastAPI CRUDrouter
