import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "teamscale-client",
    version = "0.0.6",
    author = "Thomas Kinnen - CQSE GmbH",
    author_email = "kinnen@cqse.eu",
    description = ("A simple service client to interact with Teamscale's REST API."),
    license = "Apache",
    keywords = "rest api teamscale",
    url = "https://github.com/cqse/teamscale-client-python",
    packages=['teamscale_client'],
    long_description="A simple service client to interact with Teamscale's REST API.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    install_requires=[
          'simplejson',
          'requests>=2.0'
    ],

    tests_require=[
          'pytest',
          'responses'
    ],
    setup_requires=["pytest-runner"]
)
