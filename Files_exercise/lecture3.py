import re

phonenum=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

search=phonenum.findall("my number is 123-456-2345-123-123-2342.")

print(search[0])