from partiel.auth import SimpleBasicAuth

banks = {
    "schema": {
        "country_namecode": {
            "type": "string"
        },
        "countrycode": {
            "type": "string"
        },
        "countryname": {
            "type": "string"
        },
        "id": {
            "type": "string"
        },
        "totalamt": {"type": "integer"},
        "totalcommamt": {"type": "integer"},
        "url": {"type": "string"}
    },
    "resource_methods": ["GET"],
    "item_methods": ["GET"],
}

# Version of the endpoint for admins
from copy import deepcopy
banks_schema = deepcopy(banks['schema'])
for key in banks_schema.keys():
    banks_schema[key]['readonly'] = False

admin_banks = {
    'url': '_admin/artist',
    'datasource': {
        'source': 'accounts',
    },
    'schema': banks_schema,
    'allowed_roles': ['super'],
    'allowed_item_roles': ['super'],
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PATCH', 'PUT', 'DELETE'],
    'authentication': SimpleBasicAuth
}
