# Django Dockerization Project

## Abstract
The purpose of this article is to provide documentation for containerizing a Django project, which will facilitate various settings necessary for containerizing deployment throughout the django development process.

Interrelationships between projects:
```mermaid
graph LR;
Nginx-->UWSGI;
UWSGI-->Django;
Django-->PostGresSQL;
```

## Starting Method
```bash
docker compose build
docker compose up
```
- After starting, `0.0.0.0:80` can be visited for testing purposes.

## ENV environment variables
1. A `.env` file is manually generated or generated using dotenv (sensitive information can be thrown into the cloud).
2. The `docker-compose.yml` itself loads `.env` directly.
3. `from_env.py` will read the variables loaded by `docker-compose.yml` inside the container.

## Settings.py
### Variables used by Django runtime
	1. `IN_CONTAINER`
	2. `DEPLOY_STAGE`
	3. `DEBUG`
	4. `IN_CONTAINER`
	5. `IS_LOCAL`

### Database
- If the system determines that the project is started on the Host Machine, sqlite will be used as the database.
- Otherwise, the Database defined by docker-compose will be used.

### Static
- If `s3` is used, `django-storages` needs to be installed separately, and some variables that the project will use are already defined here.
	- See [GitHub - etianen/django-s3-storage: Django Amazon S3 file storage.](https://github.com/etianen/django-s3-storage)
- The default `STATIC_ROOT` directory is `static_root`.
- `CONTAINER_STORAGE_PATH` in .env is used as `STATIC_ROOT` when using containers.

## DockerFile
- Note that the Django admin parameter passed as an ARG needs to be set as an ENV separately before it can be used in ENTRYPOINT.
- CMD in Compose is executed immediately after the entrypoint in the Dockerfile.
	- See [[../Software Design/Docker/docker-CMS_ENTRYPOINTS|docker-CMS_ENTRYPOINTS]].

## startup.sh
- Migrations-related actions are executed here.
- A bash subshell is used to create an initial admin account.