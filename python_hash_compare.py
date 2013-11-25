'''
Script for comparing the speed of Python's various hashing functions.

@author: Chris Jarabek chris.jarabek@gmail.com
'''
import random, hashlib, time, os

total_time = 0
print "MD5"
print "---------------"
hashlib.md5("").hexdigest()
for i in range(10):
    blob = ''
    for j in range(1024 * 1024):
            blob += chr(random.randint(0, 255))
    path = './tmp.dat'
    f = open(path, 'w')
    f.write(blob)
    f.close
    data_bytes = open(path, 'rb').read()
    start = time.time()
    hashlib.md5(data_bytes).hexdigest()
    end = time.time()
    diff = (end - start)
    total_time += diff 
    print diff
print "Average: "
md5avg = total_time / 10
print md5avg

print "SHA1"
print "---------------"
hashlib.sha1("").hexdigest()
total_time = 0
for i in range(10):
    blob = ''
    for j in range(1024 * 1024):
            blob += chr(random.randint(0, 255))
    path = './tmp.dat'
    f = open(path, 'w')
    f.write(blob)
    f.close
    data_bytes = open(path, 'rb').read()
    start = time.time()
    hashlib.sha1(data_bytes).hexdigest()
    end = time.time()
    diff = (end - start)
    total_time += diff 
    print diff
print "Average: "
sha1avg = total_time / 10
print sha1avg

print "SHA256"
print "---------------"
hashlib.sha256("").hexdigest()
total_time = 0
for i in range(10):
    blob = ''
    for j in range(1024 * 1024):
            blob += chr(random.randint(0, 255))
    path = './tmp.dat'
    f = open(path, 'w')
    f.write(blob)
    f.close
    data_bytes = open(path, 'rb').read()
    start = time.time()
    hashlib.sha256(data_bytes).hexdigest()
    end = time.time()
    diff = (end - start)
    total_time += diff 
    print diff
print "Average: "
sha256avg = total_time / 10
print sha256avg

print "SHA512"
print "---------------"
hashlib.sha512("").hexdigest()
total_time = 0
for i in range(10):
    blob = ''
    for j in range(1024 * 1024):
            blob += chr(random.randint(0, 255))
    path = './tmp.dat'
    f = open(path, 'w')
    f.write(blob)
    f.close
    data_bytes = open(path, 'rb').read()
    start = time.time()
    hashlib.sha512(data_bytes).hexdigest()
    end = time.time()
    diff = (end - start)
    total_time += diff 
    print diff
print "Average: "
sha512avg = total_time / 10
print sha512avg