import pyodbc
from logs import logDecorator as lD 
from typing import List
import json
import time

import jsonref
import pandas as pd
import numpy as np
from tqdm import tqdm

config  = jsonref.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.lib.sqlServer'

class sqlServerDB:

    @lD.log(logBase + '.sqlServerDB.__init__')
    def __init__(logger, self, configFile: str ='../config/lib/sqlServer/sqlServerConfig.json'):
        """
        Connect to the databse
        """

        try:
            sqlServerConfig = json.load( open(configFile, 'r') )
            connInfo        = sqlServerConfig['loginInfo']['connInfo']
            connString      = 'Driver={driver};Server={server};Trusted_Connection={trusted_connection};'.format(**connInfo)

            self.conn       = pyodbc.connect( connString )
            self.cursor     = self.conn.cursor()

        except Exception as e:
            logger.error('Unable to initialize sql server \n{}'.format(str(e)))

    @lD.log(logBase + '.sqlServerDB.disconnect')
    def disconnect(logger, self):
        """
        Disconnect from the database. If this fails, for instance
        if the connection instance doesn't exist, ignore the exception.
        """

        try:
            self.cursor.close()
            self.conn.close()
        
        except Exception as e:
            logger.error('Encounter disconnection error: {}'.format(str(e)))

    @lD.log(logBase + '.sqlServerDB.query')
    def query(logger, self, query: str, params: dict ={}) -> list:
        
        try:
            result       = self.cursor.execute(query).fetchall()
            
            self.disconnect()
            
            return result

        except Exception as e:
            logger.error('Unable to query: {} \n{}'.format(query, str(e)))