import pymysql
import os
import atom
import django

pymysql.install_as_MySQLdb()
os.environ['DJANGO_SETTINGS_MODULE'] = 'atom.settings'
django.setup()
