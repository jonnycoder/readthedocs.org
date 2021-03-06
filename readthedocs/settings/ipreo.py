import os

from .dev import CommunityDevSettings


class IpreoSettings(CommunityDevSettings):

    ALLOW_PRIVATE_REPOS = True
    # DEBUG = False
    # TEMPLATE_DEBUG = False

    # HAYSTACK_CONNECTIONS = {
    #     'default': {
    #         'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
    #         'URL': 'http://127.0.0.1:9200/',
    #         'INDEX_NAME': 'readthedocs',
    #     },
    # }

    SLUMBER_API_HOST = 'http://ipreo-readthedocs.eastus.cloudapp.azure.com'
    PRODUCTION_DOMAIN = 'ipreo-readthedocs.eastus.cloudapp.azure.com'
    WEBSOCKET_HOST = 'ipreo-readthedocs.eastus.cloudapp.azure.com'

    # DOCKER_ENABLED = True
    # DOCKER_IMAGE = "rtfd-build:base"
    # DOCKER_SOCKET = "/var/run/docker.sock"
    # DOCKER_VERSION = "1.23"
    # DOCKER_LIMITS = {}

    @property
    def LOGGING(self):
        logging = super(CommunityDevSettings, self).LOGGING
        logging["readthedocs.projects.tasks"] = {
            'handlers': ['console', 'errorlog'],
            'level': 'DEBUG',
            'propagate': False,
        }
        logging[""] = {
            'handlers': ['console', 'errorlog'],
            'level': 'DEBUG',
        }
        return logging


IpreoSettings.load_settings(__name__)
