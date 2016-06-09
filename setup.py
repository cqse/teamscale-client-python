from setuptools import setup

setup(
    name="teamscale-client",
    version="1.3.0",
    author="Thomas Kinnen - CQSE GmbH",
    author_email="kinnen@cqse.eu",
    description=("A simple service client to interact with Teamscale's REST API."),
    license="Apache",
    keywords="rest api teamscale",
    url="https://github.com/cqse/teamscale-client-python",
    packages=['teamscale_client'],
    long_description="A simple service client to interact with Teamscale's REST API.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    install_requires=[
          'simplejson',
          'requests>=2.0',
          'jsonpickle'
    ],

    tests_require=[
          'pytest',
          'responses'
    ],
    setup_requires=["pytest-runner"]
)
