### Install modules to run the app:

```
pip install -r requirements.txt
```

### Start project:

#### Filling database with currency rates:
```
cd ./currency_exchanger/
python manage.py upload_currency
python manage.py upload_currency -u # to update an existing database
```
#### Launching app:
```
python manage.py runserver
```
#### POST command to exchange:
```
http://localhost:8000/api/exchanger/
{
    "count_currency": 10,
    "result_currency": "EUR"
}
```

# Currency Exchanger API
## Copyright (c) 2022
## - Aleksandr Boyko
## - Matvey Davidovich