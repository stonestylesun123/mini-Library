#! /usr/bin/python
# -*- coding: utf-8 -*-

import random
import string

def main():
    f = open('test','w')
    first = open('firstname','r').read()
    first = str(first)
    first = first.split()
    last = open('lastname','r').read()
    last = str(last)
    last = last.split()
    start = '20090000'
    startstr = int(start)
    letter_digits = string.letters + string.digits
    
    contents = []

    for i in range(1000):
        line = []
        Reader_id = startstr + i
        Reader_id = str(Reader_id)
        line.append(Reader_id)

        Reader_name = ""
        length = random.choice([1,2])
        firstname = random.choice(first)
        Reader_name += firstname
        lastname = ""
        for i in range(length):
            temp = random.choice(last)
            lastname += temp
        Reader_name += lastname
        line.append(Reader_name)

        Reader_gender = random.choice(['M','W'])
        line.append(Reader_gender)

        Reader_email = ""
        email_length = random.choice([6,7,8,9,10,11,12])
        for i in range(email_length):
            Reader_email += random.choice(letter_digits)
        Reader_email += "@qq.com"
        line.append(Reader_email)

        line.append("0")
	line.append("1")
	line.append("no remark!")

        linestring = "##".join(line)
        #print linestring
        contents.append(linestring)

    data = "\n".join(contents)
    f.write(data)
    f.close()

if __name__ == "__main__":
    main()
