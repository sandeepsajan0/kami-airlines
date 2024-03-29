<h1 align="center">KAMI Airlines</h1>

<p align="center"> Airplanes passengers capacity calculator</p>

## Installation

- Clone code `git clone https://github.com/sandeepsajan0/kami-airlines.git`
- Install virtualenv `pip3 install virtualenv` and create virtual environment `python3 -m venv kami_venv`
- Activate virtualenv `source kami_venv/bin/activate`
- Go inside project `cd kami-airlines`
- Install requirements `pip3 install -r requirements.txt`
- Runserver `python manage.py runserver`
 
The site should be available with apidoc on `http://localhost:8000/`

## How to test API manually

- Check the homepage of site, there should be interactive apidoc in browser
- Click on `/capacity/` post api(only one is there for now), click on 'try it out'.
- Add data to Parameters
`[{ "id": "1", "passengers": 100 }, {"id": "2","passengers": 200}]` (Update/Add dicts with desired data).
- Execute the API with parameters and checkout the response body.

## Testing

- Run tests `python manage.py test`
- Or run tests via coverage `coverage run manage.py test`
- Check coverage report `coverage report -m`

## Tech Stack

- Python3
- Django
- DjangoRestFramework
- Swagger

## Assumptions
- Airplane id would be a positive integer(`>0`)
- Passenger number can't be negative
- All the calculations provided in requirements are correct

## Results

- Test coverage is 98%.

