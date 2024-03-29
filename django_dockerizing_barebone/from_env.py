import os

# General Settings
APP_NAME = os.environ.get('APP_NAME', 'app')
DEPLOY_STAGE = os.environ.get('DEPLOY_STAGE', 'local')
IS_DEBUG = (os.environ.get('IS_DEBUG', 'True') == 'True')

# Container Settings
IN_CONTAINER = os.environ.get('IN_CONTAINER', False)
if IN_CONTAINER:
    CONTAINER_STORAGE_PATH = os.environ.get('CONTAINER_STORAGE_PATH', '')

# Database Settings
DATABASE_DB_NAME = os.environ.get('DATABASE_DB_NAME', 'for-development')
DATABASE_USER = os.environ.get('DATABASE_USER', 'devel')
DATABASE_PASSWD = os.environ.get('DATABASE_PASSWD', 'for-development')
DATABASE_URI = os.environ.get('DATABASE_URI', 'localhost')
DATABASE_READ_URI = os.environ.get('DATABASE_READ_URI', 'localhost')
DATABASE_URI_PORT = os.environ.get('DATABASE_URI_PORT', 5432)

# S3 Settings
AWS_S3_REGION = os.environ.get('AWS_S3_REGION')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = os.environ.get('AWS_S3_ENDPOINT_URL')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': f'max-age={os.environ.get("AWS_S3_CACHE_CONTROL_MAX_AGE")}',
}
AWS_LOCATION = 'django'
