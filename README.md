# restaurant-kitchen-service

## Features
This Django project replicates the functionality of a culinary service, allowing chefs to register and manage their dishes. The key features include:

- User Registration and Authentication: Chefs can register on the platform and log in securely.

- Dish Management: Chefs can add, edit, and delete their dishes. Each dish includes details such as name, description, ingredients.

- Superuser Access: An admin superuser account is available with the credentials provided for managing the overall system.


> 👉 Install modules via `VENV`  

On Linux and Mac:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

On Windows:

```bash
$ python -m venv venv
$ .\venv\Scripts\activate
```


## Installing

```bash
$ pip install -r requirements.txt
```


## Model DB
![image](https://github.com/VasylTurok/restaurant_kitchen_service/assets/127683195/774bd52f-41b7-48ee-af3b-2c09f3d832bb)




> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata data.json

```

>Superuser

- Username: admin
- Password: name

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 


## Site link


- 👉 [Restaurant Kitchen Service](https://restaurant-kitchen-service-vpi6.onrender.com/) - `Product page`

## Site 
![image](https://github.com/VasylTurok/restaurant_kitchen_service/assets/127683195/4c582f27-7e44-4366-9c13-27913d706e13)

![image](https://github.com/VasylTurok/restaurant_kitchen_service/assets/127683195/64e2a928-3ea7-4c02-8a66-b238a41981a0)

![image](https://github.com/VasylTurok/restaurant_kitchen_service/assets/127683195/fd97d7bf-fb26-4a93-964c-b328ab91a89c)

![image](https://github.com/VasylTurok/restaurant_kitchen_service/assets/127683195/277678bf-318a-41ff-957c-2e0dafa43ce1)

![image](https://github.com/VasylTurok/restaurant_kitchen_service/assets/127683195/ff2a6187-5829-445b-aebb-5658296fe3f4)

![image](https://github.com/VasylTurok/restaurant_kitchen_service/assets/127683195/d1f3e373-d812-45f8-b9d9-c13690bd02e4)

![image](https://github.com/VasylTurok/restaurant_kitchen_service/assets/127683195/d51cf991-ebf7-4af4-8aad-3ef0b0cb8966)

![image](https://github.com/VasylTurok/restaurant_kitchen_service/assets/127683195/51866b81-d3cb-43b9-a6bb-6aadf80b0db1)

![image](https://github.com/VasylTurok/restaurant_kitchen_service/assets/127683195/2d3ecd3b-b018-40aa-86ac-ec5429135b67)


## Test
Use `python manage.py test` to run tests.




