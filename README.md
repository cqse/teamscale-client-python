# teamscale-client-python [![PyPI version](https://badge.fury.io/py/teamscale-client.svg)](https://badge.fury.io/py/teamscale-client) [![Teamscale Project](https://img.shields.io/badge/teamscale-teamscale--client--python-brightgreen.svg)](https://demo.teamscale.com/activity.html#/teamscale-client-python)
A simple client to access Teamscale's REST API written in Python

Find the documentation here:
http://cqse.github.io/teamscale-client-python

> [!CAUTION]
> The Teamscale Python Client is **deprecated** since February 2024.
> If you need to interact with [Teamscale's REST API](https://docs.teamscale.com/reference/rest-api/) using Python (or any other programming language), we recommend that you generate an appropriate client from the OpenAPI specification accessible within Teamscale (_?_ > _API Reference_ > _OpenAPI specification_).
> This approach offers two benefits:
> You get full access to Teamscale's extensive REST API and you are not restricted to Python but can use a programming language of your choice.


# Installation

We recommend to use at least Python 3.7 for running the Teamscale Python Client.
Install from [PyPi](https://pypi.org/project/teamscale-client/):
    
    pip install teamscale-client

Alternatively, you can install from source by cloning the repository and executing:

    pip install .
    
# Setup & Usage
Copy the file `examples/.teamscale-client.config` into your home directory and update it to reflect your setup.
This way, you can easily create the `TeamscaleClient` from the configuration
file via a `TeamscaleClientConfig`.

To get an overview on common usage scenarios, please have a look
at the `examples` folder of this repository.

# Development

To install all required dependencies for running tests and developing
the client, create a new environment and execute:

    pip install -r requirements.txt

We are happy to add additional service calls to the client.
Please make sure you include a test, if you add a service call.
To run them use:

    python setup.py test

Tests are written using the [responses library](https://pypi.org/project/responses/),
to mock the requests passed to the server using the [requests api](http://docs.python-requests.org/en/master/).
