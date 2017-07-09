Hotels
======

A simple app which creates, shows, updates hotel's rooms booking.
Uses tornado as framework and PostgreSQL as database.


Installation
------------

To setup environment please use next command::

    make setup


Testing
-------

To run unit tests please use next command::

    make test


Running
-------

To launch app please use next command::

    python app.py --host=<host> --port=<port> --dbhost=<DB host> --dbport=<DB port> --dbuser=<DB user> --dbpass=<DB user pass> --dbname=<DB name>
