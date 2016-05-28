Setup:
_______________
    psql:
    sudo 		-i -u postgres
    psql		(launch into psql)
    \q 		(to exit out of psql)
    exit 		(exit shell session for psql)

    psql db (django):
    sudo su - postgres
    psql
    CREATE DATABASE myproject;
    CREATE USER myprojectuser WITH PASSWORD 'password';
    ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
    ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE myprojectuser SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
    \q
    exit

    [CREATE DJANGO SITE/APPS]

    DATABASES = {
        'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'myproject',
      'USER': 'myprojectuser',
      'PASSWORD': 'password',
      'HOST': 'localhost',
      'PORT': '',
        }
    }
    python manage.py: makemigrations
        migrate
        createsuperuser
        runserver
    django-admin startproject mysite
    django-admin startapp myapp



Django ORM:
_______________
    ModelName.objects.all()
    ModelName.objects.create()
    ModelName.objects.all()
    ModelName.objects.filter(property='valuee', anotherproperty='value', etc...)
    ModelName.objects.get(name="Apress")
    ModelName.objects.order_by("name")

    chaining:
    ModelName.objects.order_by("name").filter(property="value")

    slicing:
    ModelName.objects.order_by('name')[0:2]

    update multiple:
    Publisher.objects.filter(id=52).update(name='Apress Publishing')

    ModelName.objects.foo.delete()
