import os,sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__))))

from transfer import data
def relay():
    print('data will be relayed now')
transfer.data()