BROKER_URL = 'redis://localhost/0'
CELERY_RESULT_BACKEND = 'redis://localhost/0'

CELERY_IMPORTS = ('application.tasks', )

CELERY_TIMEZONE = 'Australia/Sydney'
CELERY_ENABLE_UTC = True

CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
CELERYD_HIJACK_ROOT_LOGGER = False
