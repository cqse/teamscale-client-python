from setuptools import setup

setup(
    name="teamscale-client",
    version="9.2.0",
    author="Thomas Kinnen - CQSE GmbH",
    author_email="kinnen@cqse.eu",
    description=("A simple service client to interact with Teamscale's REST API."),
    license="Apache",
    keywords="rest api teamscale",
    url="https://github.com/cqse/teamscale-client-python",
    packages=['teamscale_client'],
    long_description="A simple service client to interact with Teamscale's REST API.",
    classifiers=[
        "Topic :: Utilities",
    ],
    install_requires=[
        'requests>=2.32.3',
        'configparser',
        'packaging'
    ],

    tests_require=[
        'pytest',
        'responses'
    ],
    setup_requires=["pytest-runner"]
)
