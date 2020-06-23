""" This file looks for all .feature files in the current directory and makes them available for pytest """
from pytest_bdd import scenarios

scenarios('.')
