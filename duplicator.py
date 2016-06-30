#!/usr/bin/env python3

fhr = open('README.md', 'r')
fhw = open('/tmp/asdf.duplicated', 'w')
for line in fhr:
    fhw.write(line)
    print(line)
fhr.close()
fhw.close()
