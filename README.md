# Docker
## Run App using Docker:
sudo docker build -t polestar .
sudo docker run -p 8000:8000 -i -t polestar

######################
# Tools Version
## Python 3.7 is used
## Framework: Django version 2.1.7
## Database: SQLite

######################
# Index Page
## To Check index.html (Map with all the 3 ships tracking points)
http://127.0.0.1:8000/

######################
# Admin
## Admin Login
## Manage Ships, Positions
http://127.0.0.1:8000/admin/
User: admin
Pass: 13579!!!

######################
# Prerequisites
pip install djangorestframework

######################
# REST API
## REST API (returns JSON/API, We can set it to JSON by default for End Users)
http://127.0.0.1:8000/api/ships/
http://127.0.0.1:8000/api/positions/9632179/
http://127.0.0.1:8000/api/positions/9247455/
http://127.0.0.1:8000/api/positions/9595321/

######################
# Import Positions
## Import the positions.csv file
> python manage.py shell < import.py

######################
# Database
## Database Design
## (2 tables with 1 to many (1>M) relation)
Ship (ship_name, imo)
Location (ship_id, lat, lng, timestamp)

######################
# Test Cases

python manage.py test

## 4 Unit Test Cases are created
1. Test if Ships are inserted successfully
2. Test if Locations are inserted successfully
3. Test REST API: Get All ships (checked the returned imo numbers)
4. Test REST API: Get All positions for a Ship by imo number (checked the latitude of the returned positions)