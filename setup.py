#2to6/setup.py
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='twelve',
      version='0.1dev',
      author = "Joe Dallago",
      author_email = "jd.dallago@gmail.com",
      description='Extension of 2to3, that converts Python2 code to Six library conventions.',
      long_description=read('README'),
      packages=['twelve'],
      test_suite='twelve'
      )
