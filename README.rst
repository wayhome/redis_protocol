===============================
Redis Protocol
===============================

.. image:: https://badge.fury.io/py/redis_protocol.png
    :target: http://badge.fury.io/py/redis_protocol
    
.. image:: https://travis-ci.org/youngking/redis_protocol.png?branch=master
        :target: https://travis-ci.org/youngking/redis_protocol

.. image:: https://pypip.in/d/redis_protocol/badge.png
        :target: https://crate.io/packages/redis_protocol?version=latest


Redis Protocol implemented by python

* Free software: BSD license
* Documentation: http://redis_protocol.rtfd.org.

Usage
--------
This is the protocol implemented followed by `redis protocol specification <http://redis.io/topics/protocol>`_.
I had used it in my `redis_proxy <https://github.com/youngking/redis_proxy>`_ project.

::

    >>> from redis_protocol import decode, encode
    >>> encode("ping")  # encode a request 
    ... '*1\r\n$4\r\nping\r\n'
    >>> decode('*1\r\n$4\r\nping\r\n') # decode a request body
    ... ["ping"]
    >>> decode("$6\r\nfoobar\r\n")  # decode a response
    ... "foobar"


parse redis protocol stream  
-------
parse redis protocol stream to redis commands

example :

::
data = '*3\r\n$3\r\nSET\r\n$15\r\nmemtier-8232902\r\n$2\r\nxx\r\n*3\r\n$3\r\nSET\r\n$15\r\nmemtier-8232902\r\n$2\r\nxx\r\n*3\r\n$3\r\nSET\r\n$15\r\nmemtier-7630684\r\n$3\r\nAAA\r\n'
print parse_stream(data)


