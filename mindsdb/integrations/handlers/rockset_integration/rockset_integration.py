from mindsdb.integrations.libs.const import HANDLER_CONNECTION_ARG_TYPE as ARG_TYPE
from collections import OrderedDict
import requests
import json

from ..mysql_handler import Handler as MySQLHandler, connection_args, connection_args_example


class RocksetIntegration(MySQLHandler):
    """
    This handler handles connection and execution of the Rockset integration
    """
    name = 'rockset'

    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self.host = self.connection_data['host']


connection_args = OrderedDict(
    user={
        'type': ARG_TYPE.STR,
        'description': 'The user name used to authenticate with the OceanBase server.'
    },
    password={
        'type': ARG_TYPE.STR,
        'description': 'The password to authenticate the user with the OceanBase server.'
    },
    database={
        'type': ARG_TYPE.STR,
        'description': 'The database name to use when connecting with the OceanBase server.'
    },
    host={
        'type': ARG_TYPE.STR,
        'description': 'The host name or IP address of the OceanBase server. '
    },
    port={
        'type': ARG_TYPE.INT,
        'description': 'The TCP/IP port of the OceanBase server. Must be an integer.'
    }
)

connection_args_example = OrderedDict(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='password',
    database='database'
)
