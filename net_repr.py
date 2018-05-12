#!/usr/bin/env python

import sys


def bin_ip(ip_addr):
    octets = ip_addr.split('.')
    if len(octets) != 4:
        print 'Invalid ip address', ip_addr
    else:
        rv = []
        for o in octets:
            rv.append(format(int(o), '08b'))
        return rv


def bin_cidr(prefix):
    prefix = int(prefix)
    if not (12 < prefix <= 32):
        print 'Invalid prefix', prefix
        return None
    else:
        # populate 32 bit netmask with prefix 1s and trailing 0s
        ones = prefix * '1'
        zeroes = (32 - prefix) * '0'
        return get_octets(ones + zeroes)


def get_octets(bits):
    rv = []
    offset = 0
    for i in xrange(len(bits)/8):
        step = (i + 1) * 8
        rv.append(bits[offset:step])
        offset = step
    return rv


def dot(octets):
    if octets:
        return '.'.join(octets)


if __name__ == '__main__':
    arg = sys.argv[1]
    ip = prefix = None
    if '/' in arg:
        ip, prefix = arg.split('/')
    elif '.' in arg:
        ip = arg
    else:
        prefix = arg
    if ip:
        ip_bits = bin_ip(ip)
        if ip_bits:
            print dot(ip_bits)
    if prefix:
        subnet_bits = bin_cidr(prefix)
        if subnet_bits:
            print dot(subnet_bits)
