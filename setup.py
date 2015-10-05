from setuptools import setup

install_requires = [
    "Flask==0.10.1",
    "Flask-SQLAlchemy==2.0",
    "itsdangerous==0.24",
    "Jinja2==2.8",
    "linecache2==1.0.0",
    "MarkupSafe==0.23",
    "nose==1.3.7",
    "psycopg2==2.6.1",
    "six==1.9.0",
    "SQLAlchemy==1.0.8",
    "traceback2==1.4.0",
    "Werkzeug==0.10.4",
]

setup(
    name='readsapi',
    version='0.0.0',

    description='A JSON Home implementation of a better GoodReads API',
    long_description=open("README.md").read(),
    license='MIT',
    url='https://github.com/ceaess/readsapi',

    author='Cea Stapleton',
    author_email='todo',

    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
    ],

    packages=["readsapi"],

    install_requires=install_requires,
)
