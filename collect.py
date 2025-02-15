import numpy as np
import pandas as pd

import os
from datetime import datetime
from datetime import timedelta

from pykrx import stock
from pykrx import bond



def get_date(market='kospi', PATH='./data/kospi-individual'):
    '''
    [Description]
    - Get the date of start and end to collect.
    
    [Inputs]
    - market (str):
    - PATH   (str):
    
    [Outputs]
    - start  (str):
    - end    (str):
    '''
    
    years_collected = set([int(years[-8:-4]) for years in os.listdir(path=PATH)])
    last_year = max(years_collected)
    last_date_collected = pd.read_csv(f'{PATH}/{market}_close_{last_year}.csv', index_col='Unnamed: 0').index[-1]
    
    start = (datetime.strptime(last_date_collected, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
    end = datetime.today().strftime('%Y-%m-%d')
    
    return start, end