#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_redis_protocol
----------------------------------

Tests for `redis_protocol` module.
"""

import unittest
from nose.tools import eq_

from redis_protocol import decode, encode, parse_stream


class TestRedis_protocol(unittest.TestCase):

    def setUp(self):
        pass

    def test_ping(self):
        eq_(decode("*1\r\n$4\r\nping"), ["ping"])
        eq_(decode(encode("ping")), ["ping"])

    def test_set(self):
        eq_(decode("*3\r\n$3\r\nSET\r\n$5\r\nmykey\r\n$7\r\nmyvalue\r\n"), ['SET', 'mykey', 'myvalue'])

    def test_response(self):
        eq_(decode("$6\r\nfoobar\r\n"), "foobar")

    def test_none(self):
        eq_(decode("$-1\r\n"), None)

    def test_none_response(self):
        eq_(decode("*3\r\n$3\r\nfoo\r\n$-1\r\n$3\r\nbar\r\n"), ["foo", None, "bar"])

    def test_parse_tream(self):
        data = '*3\r\n$3\r\nSET\r\n$15\r\nmemtier-8232902\r\n$2\r\nxx\r\n' \
               '*3\r\n$3\r\nSET\r\n$15\r\nmemtier-8232902\r\n$2\r\nxx\r\n' \
               '*3\r\n$3\r\nSET\r\n$15\r\nmemtier-7630684\r\n$3\r\nAAA\r\n'
        eq_(parse_stream(data), ['SET memtier-8232902 xx', 'SET memtier-8232902 xx', 'SET memtier-7630684 AAA'])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
