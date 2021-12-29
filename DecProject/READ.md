

#Simple REST API:

a basic car makes and models database interacting with an external API. Here's a full specification of endpoints:

POST /cars

- Request body should contain car make and model name,
- Based on this data, its existence should be checked here https://vpic.nhtsa.dot.gov/api/  ,
- If the car doesn't exist - return an error,
- If the car exists - it should be saved in the database.

DELETE /cars/{ id }

- Should delete the car with the given id from database,
- If the car doesn't exist in database - return an error,

POST /rate

- Add a rate for a car from 1 to 5.

GET /cars

 - Should fetch a list of all cars already present in application database with their current average rate.

GET /popular

- Should return top cars already present in the database ranking based on a number of rates (not average rate values).

#Documentation

    Django,
    Django REST framework,
    Json.

#Requirements and setup

    Python 3.9,
    PyCharm 2021.2.2,
    Django 4.0,
    Django REST framework 3.13.1,
    Postman 9.7.0.

