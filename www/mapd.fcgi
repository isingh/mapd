#!/usr/bin/python2.6
import sys, os

# Add a custom Python path.
sys.path.insert(0, "/home/cancerko/.local/lib/python2.6/site-packages")
sys.path.insert(0, "/home/cancerko/.local/bin")
sys.path.insert(0, "/home/cancerko/code/")
sys.path.insert(0, '/home5/cancerko/.local/lib/python2.6/site-packages/flup-1.0.2-py2.6.egg')

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "mapd.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
