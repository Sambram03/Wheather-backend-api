# Weather Backend API

This repository contains the code for a simple Flask-based backend API that retrieves weather forecast data based on user input location.

## Setup Instructions

1. Clone this repository.
2. Install Flask by running `pip install Flask`.
3. Replace 'YOUR_API_KEY' in `app.py` with your OpenWeatherMap API key.
4. Run the Flask app using `python app.py`.

## API Documentation

### Endpoints

- `/weather`
    - Method: GET
    - Parameters: `city`
    - Example Usage: `http://localhost:5000/weather?city=London`

### Postman Workspace
Find the Postman workspace [here](<your_postman_workspace_link>).

For detailed API endpoint testing and documentation, refer to the Postman workspace.
## Prerequisites
* Python
* Flask
* Request packages
* Postman for testing API endpoints
* API key generated from OpenWeatherMap API

## Brief Procedure
1. Install the required libraries.
2. To run the program we need to generate the API key using the OpenWeatherMap API key.
3. Run the application , once the code is compiled , open the Postman and create a new request to  `http://127.0.0.1:5000/weather` with the `GET` method.
4. Add a query parameter 'city' with the value being the city.
5. For example (city=Mysore).
6. Once its done , send the request and get the output.To check the accuracy of the Output which contains the weather data by `OpenWeatherMap`.

## Detailed explanation
1. Run the Python script using the virtual environment by using idle or VScode.
2. The script contains the base url `http://127.0.0.1:5000`. When you click on this url, you will see 404 error.
3. Now by creating the new Workspace in the Postman worksapce, set the request type to 'GET'.
4. In the URL column enter Enter the URL for your Flask API endpoint i.e, `http://127.0.0.1:5000/weather?`.
5. Click on the "Params" tab. In the "Key" column, enter `location`. In the "Value" column, enter the city for which you want to retrieve the weather information.
6. Click the send button the data will be retrieved in the form of JSON file.

## Screenshots

<img width="1470" alt="Screenshot 2023-11-28 at 7 48 07 PM" src="https://github.com/Sambram03/Wheather-backend-api/assets/150266186/592d7230-9ff6-48a5-b7dd-b8ead704f5ac">

<img width="1470" alt="Screenshot 2023-11-28 at 7 48 57 PM2" src="https://github.com/Sambram03/Wheather-backend-api/assets/150266186/ce4d90e4-6900-4f74-8248-849049b5fba8">

<img width="1470" alt="Screenshot 2023-11-28 at 7 49 27 PM3" src="https://github.com/Sambram03/Wheather-backend-api/assets/150266186/eb858d42-8435-4a73-a4a4-d546e6e0859f">

<img width="1470" alt="Screenshot 2023-11-28 at 7 51 31 PM4" src="https://github.com/Sambram03/Wheather-backend-api/assets/150266186/abd907e8-81c8-4c9d-932b-bc46b1b0c2bf">
