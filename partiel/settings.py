import os
from .banks.domain import banks, admin_banks

DEFAULT_SETTINGS = {
    'SERVICE_NAME': 'partiel',
    'SERVICE_ENV': os.getenv('SERVICE_ENV', 'dev'),
    'ADMIN_PASSWORD': os.getenv('ADMIN_PASSWORD', ''),

    'MONGO_URI': os.getenv('MONGO_URI', 'mongodb://localhost/python_partiel'),

    'DOMAIN': {
        'banks': banks,
        'admin_banks': admin_banks
    }
}
