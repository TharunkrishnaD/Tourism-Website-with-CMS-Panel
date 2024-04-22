import imp
import os
import sys


#sys.path.insert(0, os.path.dirname(__file__))

#wsgi = imp.load_source('wsgi', 'manage.py')
#application = wsgi.application


from vacation_feast_Website.wsgi import application
