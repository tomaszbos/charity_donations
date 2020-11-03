# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'charity_db',
        'HOST': 'localhost',
        'PASSWORD': 'coderslab',
        'USER': 'postgres',
        'PORT': 5432,
    }
}

# Secret key
# https://docs.djangoproject.com/en/2.1/ref/settings/#secret-key

SECRET_KEY = 'ms@90hhw8%bkcv$b=&3gsmss%*05yo@oi#c56xe*a3(&s1fkz*'