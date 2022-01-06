Install all dependencies using below command:
pip install -r requirements.txt


TO Run the App
use below command on Terminal::uvicorn src.main:app --reload


To Access docs
https://localhost:8000/docs 

Search Address API
will return all the addresses whose latitude and longitude is less than or equal to whats specified in the query


Note:
This Project is black formatted, flake8 complaint and isort compatible


# improvements
# use sentry for errors logging
# use factory for unit test
# use FastAPI CRUDrouter

