def test_coordinates_class(latitude, longitude):
    coord_obj = coordinates.Coordinates(latitude=latitude, longitude=longitude)

    # validate serialize
    check_obj = {"latitude": latitude, "longitude": longitude}

    assert coord_obj.serialize() == check_obj