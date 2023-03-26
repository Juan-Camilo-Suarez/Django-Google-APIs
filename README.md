# Django-Google-APIs
[code on gitlab](https://gitlab.com/juancamilosuarez3/django-google-apis)


![map1](https://user-images.githubusercontent.com/71409094/227764112-91f29f35-91de-4d77-ae64-aa894a39f24c.png)
![map2](https://user-images.githubusercontent.com/71409094/227764116-0ff348fc-dfba-4136-9068-71989bc9e675.png)




## 1. Introduction
### 1.1 Description

This project is a web application that leverages Google APIs to provide users with various functionalities, such as location-based search. The project uses Django, a Python-based web framework, and PostgreSQL, a scalable database management system, for the backend development. The frontend development uses HTML and JavaScript to create an intuitive user interface, which includes forms, maps, and search results. The project also includes configuring OAuth 2.0 authentication and enabling the Google Maps JavaScript API and Google Places API. Finally, ReCAPTCHA is used to ensure the security of the application by preventing automated software from interacting with the app.

In summary, the project involves setting up and integrating various Google APIs, configuring Python and Django for backend development, creating an intuitive user interface using HTML and JavaScript for frontend development, and ensuring the security of the app using ReCAPTCHA.

### 1.2 Main features
* Connect Django with MySQL with Docker
* Use Recapcha
* Connect Django with Google Apis
* Front end development such as HTML and JavaScript
### 1.3 Limitations & Unknowns
* Recapchat
* Google Apis

## 2. Installing and running the project
1. Create a virtual environment:\
```python -m venv venv```
2. Activate virtual environment:\
```venv\Scripts\activate.bat``` - для Windows \
```source venv/bin/activate``` - для Linux и MacOS
3. Install poetry:\
```pip install poetry  ```
4. Enter the virtual environment:\
   ``` poetry shell  ```
5. Install dependencies:\
   ``` poetry install  ```
6. Installing pre-commit hooks to run linters before commit:\
```pre-commit install```
7. Install PostgreSQL from Docker:\
   ```docker-compose up -d```
8. Apply migrations to database:\
```python manage.py migrate```
9. Server start:\
```python manage.py runserver```
