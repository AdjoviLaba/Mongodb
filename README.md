# FastAPI MongoDB CRUD Application

## Introduction
This project is a FastAPI application designed to perform CRUD (Create, Read, Update, Delete) operations on `Person` entities using MongoDB as the database. It's a simple yet powerful API for managing person data.

## Features
- CRUD operations for `Person` entities.
- MongoDB integration for data persistence.
- Automatic ID generation using UUID.
- Pydantic models for data validation.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.6+
- MongoDB server (local or remote)

## Installation

To get this project up and running locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AdjoviLaba/Mongodb.git
   cd Mongodb
   ```

2. **Set Up a Virtual Environment** (Optional, but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   - Set up your MongoDB connection URI in an environment variable or a configuration file.

5. **Run the Application**
   ```bash
   uvicorn main:app --reload
   ```

## Usage

The API provides the following endpoints:

- `POST /`: Create a new `Person`.
- `GET /`: Retrieve a list of `Person` entities.
- `GET /{id}`: Retrieve a `Person` by ID.
- `PUT /{id}`: Update a `Person` by ID.
- `DELETE /{id}`: Delete a `Person` by ID.

## API Documentation

Visit `http://localhost:8000/docs` for Swagger UI documentation, where you can test the API endpoints directly.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

[MIT License](LICENSE)

---



This README provides a basic structure to help users understand and use your application. You can expand it with more details specific to your project as needed.
