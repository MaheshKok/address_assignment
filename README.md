1. Install all dependencies:
pip install -r requirements.txt


2. To Run the App: 
use command on Terminal::uvicorn src.main:app --reload


3. To Access docs: 
https://localhost:8000/docs 


4. Search Address API
will return all the addresses whose latitude and longitude is less than or equal to whats specified in the query


[comment]: <> (Note:)
This Project is black formatted, flake8 complaint and isort compatible


# Improvements
1. use sentry for errors logging
2. use factory for unit test
3. use FastAPI CRUDrouter
