import os, sys

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE)

from config import app_key, master_secret, mobile
from jsms import Jsms

jc = Jsms(app_key, master_secret)
