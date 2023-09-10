from collections import namedtuple


ExternalConfig = namedtuple(
    'ExternalConfig', (
        'host',
        'port',
        'password'
))
