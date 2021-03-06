"""
flask-mongo-sessions
====================

Server-side sessions for Flask with MongoDB.

Documentation: https://flask-mongo-sessions.readthedocs.org/en/latest/
"""
from setuptools import setup


setup(
    name='flask-mongo-sessions',
    version='0.2.1',
    url='https://github.com/ivanyu/flask-mongo-sessions',
    license='MIT',
    author='Ivan Yurchenko',
    author_email='ivan0yurchenko@gmail.com',
    maintainer='Ivan Yurchenko',
    maintainer_email='ivan0yurchenko@gmail.com',
    description='Server-side sessions for Flask with MongoDB',
    long_description=__doc__,
    py_modules=['flask_mongo_sessions', 'flask_mongo_sessions.tests'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.8',
        'Flask-PyMongo',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords="flask mongodb pymongo flask-pymongo "
             "mongoengine flask-mongoengine",
    test_suite='flask_mongo_sessions.tests.suite',
)
