#! /usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

class library:
    @staticmethod
    def login():
        id_type = raw_input('Please input your identification(student/manager): ')
        id_number = raw_input('Please input your ID number: ')
        id_pass = raw_input('Please input your ID password: ')
        library.login_in(id_type, id_number, id_pass)
    @staticmethod
    def login_in(id_type, id_number, id_pass):
        con = mdb.connect('localhost', 'library', '123456', 'librarydb', charset='utf8')
        cur = con.cursor()
        if id_type == 'student':
            pass
        elif id_type == "manager":
            cur = con.cursor()
            cur.execute("SELECT Worker_id FROM Manager")
            managers = cur.fetchall()
            temp_id = int(id_number)
            temp_id = (temp_id,)
            if temp_id in managers:
                cur.execute("SELECT Worker_pass FROM Manager WHERE Worker_id=%s" % id_number)
                passwd = cur.fetchone()
                #print "passwd:",passwd
                temp_pass = (id_pass,)
                #print "temp_pass:",temp_pass
                if temp_pass == passwd:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

def main():
   library.login() 

if __name__ == "__main__":
    main()
