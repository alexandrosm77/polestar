**Polestar django ship API**

This is a simple API to be used for listing polestar ships and their positions.

# Endpoints:
* GET /api/ships/ will return all polestar ships
* GET /api/positions/\<imo>/ will return all positions for a ship


# Installation:
##To run with docker:

```
git clone https://github.com/alexandrosm77/polestar.git
cd polestar
docker-compose up
```


## To install in a virtual environment:

```
git clone https://github.com/alexandrosm77/polestar.git
cd polestar
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py import_csv positions.csv
```

### To run the api
`python manage.py runserver 8000`

### To run the tests
`python manage.py test ships/tests`


# Notes
* The api will be accessible at http://localhost:8000/api
* The manager command import_csv can import new positions for the three given ships if required