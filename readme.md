# Corider API

Corider API is a simple Flask-based web application that provides endpoints for managing user data in a MongoDB database. This API allows users to view, add, update, and delete user records.

## Installation

1. Ensure you have Python and Flask installed on your system.
2. Clone this repository to your local machine.
3. Install the required dependencies using the following command:

   ```
   pip install -r requirements.txt
   ```

## Getting Started

1. Make sure you have a MongoDB instance running on `localhost` at the default port `27017`.
2. Launch the Corider API server by running the following command:

   ```
   python app.py
   ```

3. The API will be accessible at `http://127.0.0.1:5000/`.

## Endpoints

### Get All Users

- **URL**: `/all_users`
- **Method**: `GET`
- **Description**: Fetches all user records from the database and returns a JSON response containing user data.

### Get User by ID

- **URL**: `/get_users/<id>`
- **Method**: `GET`
- **Description**: Retrieves a specific user record based on the provided `id` and returns a JSON response containing user details.

### Add User

- **URL**: `/add_users`
- **Method**: `POST`
- **Description**: Adds a new user record to the database based on the JSON data provided in the request body. The request should include the user's `name`, `email`, and `password`.

### Update User

- **URL**: `/update_user/<id>`
- **Method**: `PUT`
- **Description**: Updates an existing user record in the database with the provided `id`. The request should include the updated `name`, `email`, and `password`.

### Delete User

- **URL**: `/delete_user/<id>`
- **Method**: `DELETE`
- **Description**: Deletes a user record from the database based on the provided `id`.

## Usage Examples

Here are some examples of how to use the Corider API:

1. Fetch all users:

   ```
   GET http://127.0.0.1:5000/all_users
   ```

2. Get a specific user by ID:

   ```
   GET http://127.0.0.1:5000/get_users/<user_id>
   ```

3. Add a new user:

   ```
   POST http://127.0.0.1:5000/add_users
   Content-Type: application/json

   {
       "name": "John Doe",
       "email": "john.doe@example.com",
       "password": "secretpassword"
   }
   ```

4. Update an existing user:

   ```
   PUT http://127.0.0.1:5000/update_user/<user_id>
   Content-Type: application/json

   {
       "name": "Updated Name",
       "email": "updated.email@example.com",
       "password": "updatedpassword"
   }
   ```

5. Delete a user:

   ```
   DELETE http://127.0.0.1:5000/delete_user/<user_id>
   ```

## Contributing

We welcome contributions to improve the Corider API. If you have any suggestions or find any issues, please feel free to open a pull request or create an issue in the repository.

