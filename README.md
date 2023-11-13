# restaurant-kitchen-service

The project reproduces the work of a culinary service, where you can register as a chef and manage your dishes.

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate

```

## Installing

```bash
$ pip install -r requirements.txt
```

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 


## Model DB
![image](https://github.com/VasylTurok/restaurant-kitchen-service/assets/127683195/a51ea13e-2b67-454c-9dbc-416092fc1982)


> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```



## Site 
![image](https://github.com/VasylTurok/restaurant-kitchen-service/assets/127683195/8912f55e-c1c6-40a8-87fc-cf6f5e456fa2)
![image](https://github.com/VasylTurok/restaurant-kitchen-service/assets/127683195/7883f488-185c-40ad-9a1b-a2bfa5bed48e)
![image](https://github.com/VasylTurok/restaurant-kitchen-service/assets/127683195/0c7429f0-faba-4fe2-a9cd-d64c28f61942)
![image](https://github.com/VasylTurok/restaurant-kitchen-service/assets/127683195/af5bbb4d-821c-437b-b3c7-4323f651d751)
![image](https://github.com/VasylTurok/restaurant-kitchen-service/assets/127683195/0bddcae1-a64e-4f4d-8908-13635058803e)
![image](https://github.com/VasylTurok/restaurant-kitchen-service/assets/127683195/d2257c16-6da9-4816-a2a8-ebbb41f8868c)
![image](https://github.com/VasylTurok/restaurant-kitchen-service/assets/127683195/e87f37e3-6ef8-4e39-99d3-302608741f3e)
![image](https://github.com/VasylTurok/restaurant-kitchen-service/assets/127683195/cf89f25c-a895-4511-8fae-d6ee9beee138)
![image](https://github.com/VasylTurok/restaurant-kitchen-service/assets/127683195/dfea08f3-8dce-4d41-8dbb-6f8be690b2bf)

## Test
Use `python manage.py test` to run tests.




