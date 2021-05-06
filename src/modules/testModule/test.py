from lib.sqlServer import sqlServerDB
from logs          import logDecorator as lD 

import json
import time
import pandas as pd
import numpy as np
from tqdm import tqdm

config  = json.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.modules.test'

@lD.log(logBase + '.main')
def main(logger, resultsDict):
    
    try:
        testConfig = json.load( open('../config/modules/testModule/test.json', 'r') )

    except Exception as e:
        logger.error(f'Unable to run main function under test module \n{str(e)}')

if __name__ == '__main__':

    pass