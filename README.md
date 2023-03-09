# teamscale-client-python [![Build Status](https://travis-ci.org/cqse/teamscale-client-python.svg?branch=master)](https://travis-ci.org/cqse/teamscale-client-python) [![PyPI version](https://badge.fury.io/py/teamscale-client.svg)](https://badge.fury.io/py/teamscale-client) [![Teamscale Project](https://img.shields.io/badge/teamscale-teamscale--client--python-brightgreen.svg)](https://demo.teamscale.com/activity.html#/teamscale-client-python)
A simple client to access Teamscale's REST API written in Python

Find the documentation here:
http://cqse.github.io/teamscale-client-python


# Installation

We recommend to use at least Python 3.7 for running the Teamscale Python Client.
Install from the [PyPi](https://pypi.org/project/teamscale-client/):
    
    pip install teamscale-client

Alternatively, you can install from source by cloning the repository and executing:

    pip install .
    
# Setup & Usage
Copy the file `examples/.teamscale-client.config` into your home directory and update it to reflect your setup.
This way, you can easily create the `TeamscaleClient` from the configuration
file via a `TeamscaleClientConfig`.

Please have a look at the `examples` folder of this repository to get an
overview on common usage scenarios.

# Development

To install all required dependencies for running tests and developing
the client, create a new environment and execute:

    pip install -r requirements.txt

We are happy to add additional service calls to the client. Please make sure you include a test, if you add a service call. To run them use:

    python setup.py test

Tests are written using the [responses library](https://pypi.org/project/responses/), to mock the requests passed to the server using the [requests api](http://docs.python-requests.org/en/master/).
