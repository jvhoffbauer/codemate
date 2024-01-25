def fake_users(models):
    data = [
        models.User(
            id=i,
            username=f"User_{i}",
            password=f"password_{i}",
            create_time=datetime.datetime.strptime(
                f"2022-01-0{i} 00:00:00", "%Y-%m-%d %H:%M:%S"
            ),
            address=["address_1", "address_2"],
            attach={"attach_1": "attach_1", "attach_2": "attach_2"},
        )
        for i in range(1, 6)
    ]
    db.session.add_all(data)
    db.session.commit()
    return data