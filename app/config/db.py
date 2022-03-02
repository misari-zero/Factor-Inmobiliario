import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': '3008',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

HEROKU = {
    'default': {
        'ENGINE': 'django.db.backends.pg2',
        'NAME': 'db',
        'USER': 'eoteoiqlgbelxr',
        'PASSWORD': 'fc614bab3184b80c0f39e851c6c7c882b54b71de75ded7b2ea2c07db9c99471a',
        'HOST': 'ec2-34-233-157-9.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}
