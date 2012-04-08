#! /usr/bin/python
# -*- coding: utf-8 -*-

import random
import string

def main():
    f = open('test','w')
    string_digits = string.letters + string.digits
    
    contents = []

    for i in range(10000):
        line = []
        line.append(str(i + 1))

        number = random.choice([3,4,5])
        Book_name = []
        for i in range(number):
            length = random.choice([3,4,5])
            temp = ""
            for i in range(length):
                temp += random.choice(string.lowercase)
            Book_name.append(temp)
        Book_name = " ".join(Book_name)
        line.append(Book_name)
        
        number = random.choice([1,2,3])
        Book_author = []
        for i in range(number):
            length = random.choice([3,4,5])
            temp = ""
            for i in range(length):
                temp += random.choice(string.uppercase)
            Book_author.append(temp)
        Book_author = " ".join(Book_author)
        line.append(Book_author)

        Book_publisher = random.choice(["Apress","O'reilly"])
        line.append(Book_publisher)

        Book_type = random.choice(["IT","Math","Culture","Medical","Traffic","Architecture"])
        line.append(Book_type)

        Book_amount = 10
        line.append(str(Book_amount))

        lended_amount = 0
        line.append(str(lended_amount))

        Book_remarks = "no remark!"
        line.append(Book_remarks)

        print line
        linestring = "##".join(line)
        
        contents.append(linestring)

    data = "\n".join(contents)
    f.write(data)
    f.close()

if __name__ == "__main__":
    main()
