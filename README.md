Installation
============

1.- Clone from repository

    ::
        git clone git@github.com:AlfredoAguilar/CostCenter.git

2.- Move to the folder where the PipFile is located

    ::
        cd .config_project/environ

3.- Make "conf.json" file
    ::
        touch conf.json

    ::
        Copy and paste this content
        -----------------------------------------------
        {
            "generals": {
            "settings": "BaseProject.settings.dev"
            }
        }
        ------------------------------------------------

4.- Move to

    ::
        cd dev/

5.- Make ".env" file

    ::
        touch .env

    ::
        Copy and paste this basic env config
        ----------------------------------------------------------------------------------
        DEBUG=True
        # DISABLE_EXISTING_LOGGERS=false,
        SECRET_KEY="csdcscdscGFDGtrgrgtrtgr#)xem2=jig6^#v97r)&t&_anbd294"
        # INTERNAL_IPS=
        ALLOWED_HOSTS=*
        ADMINS=[]
        DB_ENGINE=sqlite
        DATABASE_URL=postgres://apps:apps@localhost:5432/DBNAME
        REDIS_SERVER=redis://localhost:6379/1
        BACKEND_URL=redis+socket:///var/run/redis/redis.sock?db=3

        CACHE_TIMEOUT=14400
        CACHE_PREFIX=rotaw

        #EMAIL_URL=smtp://
        EMAIL_URL=smtp://
        DEFAULT_FROM_EMAIL=

        SENTRY_DSN=

        ENABLE_REMOTE_STORAGE=false
        BUCKET_NAME=core-service
        AWS_ACCESS_KEY_ID=fsdfsfs
        AWS_SECRET_ACCESS_KEY=ffffff
        CELERY_BROKER_URL=redis+socket:///var/run/redis/redis.sock?db=2
        CELERY_TIMEZONE=America/Mexico_City

        # Admin Vars
        ADMIN_SITE_HEADER="Site header"
        ADMIN_SITE_TITLE="Admin Title"
        ADMIN_SITE_INDEX_TITLE="Admin Index Title"


        # WebPage Vars
        PROJECT="PROJECT NAME"
        LOGIN_REDIRECT_URL=/PUT YOUR URL

        LOG_CONSOLE_LEVEL=INFO
        LOG_FILE_DJANGO_LEVEL=INFO

        SENDGRID_API_KEY=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
        EMAIL_BACKEND_SETTING=production
        EMAIL_FILE_PATH=.logs/file_emails
        SERVER_EMAIL=
        --------------------------------------------------------------------------------------

6.- Back to .config_project

    ::
        cd ..

7.- Install dependencies

    ::
        pipenv install

8.- Activate virtual enviroment

    ::
        pipenv shell

9.- Go back to the root of the project

    ::
        cd ...

10.- Make migrations

    ::
        python manage.py makemigrations

11.- Migrate to data base

    ::
        python manage.py migrate

12.- Run project

    ::
        python manage.py runserver