# teamscale-client-python [![Build Status](https://travis-ci.org/cqse/teamscale-client-python.svg?branch=master)](https://travis-ci.org/cqse/teamscale-client-python) [![PyPI version](https://badge.fury.io/py/teamscale-client.svg)](https://badge.fury.io/py/teamscale-client) [![Teamscale Project](https://img.shields.io/badge/teamscale-teamscale--client--python-brightgreen.svg)](https://demo.teamscale.com/activity.html#/teamscale-client-python)
A simple client to access Teamscale's REST API written in Python

Find the documentation here:  
http://cqse.github.io/teamscale-client-python

# Installation
Install via:
    
    pip install teamscale-client

# Development
We suggest the [PyCharm](https://www.jetbrains.com/pycharm/) IDE for development in this project.
We are happy to add additional service calls to the client. Please make sure you include a test, if you add a service call. To run them use:

    python setup.py test

Tests are written using the [responses library](https://pypi.org/project/responses/), to mock the requests passed to the server using the [requests api](http://docs.python-requests.org/en/master/).
