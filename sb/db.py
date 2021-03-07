import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SQLITE
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# POSTGRESQL
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'prueba',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
# MYSQL
MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
