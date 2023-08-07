def register_user(db, name, email, password):
    user_data = {
        'name': name,
        'email': email,
        'password': password
    }

    result = db.user_data.insert_one(user_data)

    if result.inserted_id:
        return {'message': 'User registered successfully.'}
    else:
        return {'message': 'Failed to register user.'}
