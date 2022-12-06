# TinyProject - Demo made with Django

This is a demo made to show how Django works.

## How to use

Clone the repository or download the source code.

Then, install the requirements using:

```bash
python -m pip install -r requirements.txt
```

After that, prepare the database with:

```bash
python manage.py migrate
```

Now, just run the development server with:

```bash
python manage.py runserver
```

Additionally, if you want to have access to the admin panel, run:

```bash
python3 manage.py createsuperuser
```

Finally, you can acess **http://localhost:8000/** and test the app.
