#!/usr/bin/env python
# -*- coding: utf-8 -*-
DELIMITER = "\r\n"


def decode(data):
    processed, index = 0, data.find(DELIMITER)
    if index == -1:
        index = len(data)
    term = data[processed]
    if term == "*":
        return parse_multi_chunked(data)
    elif term == "$":
        return parse_chunked(data)
    elif term == "+":
        return parse_status(data)
    elif term == "-":
        return parse_error(data)
    elif term == ":":
        return parse_integer(data)


def parse_multi_chunked(data):
    index = data.find(DELIMITER)
    count = int(data[1:index])
    result = []
    start = index + len(DELIMITER)
    for i in range(count):
        chunk, length = parse_chunked(data, start)
        start = length + len(DELIMITER)
        result.append(chunk)
    return result


def parse_chunked(data, start=0):
    index = data.find(DELIMITER, start)
    if index == -1:
        index = start
    length = int(data[start + 1:index])
    if length == -1:
        if index + len(DELIMITER) == len(data):
            return None
        else:
            return None, index
    else:
        result = data[index + len(DELIMITER):index + len(DELIMITER) + length]
        return result if start == 0 else [result, index + len(DELIMITER) + length]


def parse_status(data):
    return [True, data[1:]]


def parse_error(data):
    return [False, data[1:]]


def parse_integer(data):
    return [int(data[1:])]


def encode(*args):
    "Pack a series of arguments into a value Redis command"
    result = []
    result.append("*")
    result.append(str(len(args)))
    result.append(DELIMITER)
    for arg in args:
        result.append("$")
        result.append(str(len(arg)))
        result.append(DELIMITER)
        result.append(arg)
        result.append(DELIMITER)
    return "".join(result)

if __name__ == '__main__':
    print(decode(encode("ping")))
    print((encode("set some value")))
    print(encode("foobar"))
