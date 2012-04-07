#! /usr/bin/python
# -*- coding: utf-8 -*-
# @author:  huangxiaohui
# @version: V1.0
# @time:    2012-

# import MySQLdb module
import MySQLdb as mdb
import sys

# 设置编码utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

class lib_student:
    """
class lib_student
contains function
    1   look up book
        a. look up a book by it's ID
        b. look up a book by it's name
        c. look up a book by it's key words
    2   lookup personal information about oneself and the books he borrowed
    """
    def __init__(self, connection):
        """
    instructor function
    @param connection:  connection to MySQL
    @type connection:   MySQLdb.connect.cursor()
        """
        self.con = connection
        self.cur = self.con.cursor()
        self.cur.execute("SET NAMES utf8")
        self.con.commit()

    def lookup_Book_by_ID(self, Book_id):
        """
    look up a book by it's ID
    @param Book_id: the ID of a book
    @type Book_id:  string/integer
    @return data:   information about the book
    @rtype data:    list
        """
        command = u"""self.cur.execute("SELECT * FROM Book WHERE Book_id = %s")""" % Book_id
        #print command
        exec(command)
        data = self.cur.fetchone()
        data = list(data)
        data = self.change_str_from_mysql(data)
        return data
    
    def lookup_Book_by_NAME(self, Book_name):
        """
    look up a book by it's name
    @param Book_name:   the name of a book
    @type Book_name:    string
    @return data:       information about the book
    @rtype data:        list
        """
        command = u"""self.cur.execute("SELECT * FROM Book WHERE Book_name = %s")""" % Book_name
        #print command
        exec(command)
        data = self.cur.fetchone()
        data = list(data)
        data = self.change_str_from_mysql(data)
        return data

    def lookup_person_info(self, Reader_id):
        """
    look up personal information about oneself and the books borrowed
    @param Reader_id:   the ID of a reader
    @type Reader_id:    string/integer
    @return temp:       information that looked up from MySQL
    @rtype temp:        list
        """
        # 第一步获取读者信息
        command = u"""self.cur.execute("SELECT * FROM Reader WHERE Reader_id = %s")""" % Reader_id
        exec(command)
        Reader_info = list(self.cur.fetchone())
        Reader_info = self.change_str_from_mysql(Reader_info)
        # 第二步获取借书信息
        command = u"""self.cur.execute("SELECT * FROM Record WHERE R_id = %s")""" % Reader_id
        exec(command)
        Record_data = list(self.cur.fetchall())
        Record_info = []
        for i in range(len(Record_data)):
            temp = list(Record_data[i])
            Record_info.append(temp)
        # 第三步获取图书信息
        Book_info = []
        for i in range(len(Record_info)):
            Book_id = str(Record_info[i][2])
            command = u"""self.cur.execute("SELECT * FROM Book WHERE Book_id = %s")""" % Book_id
            exec(command)
            book = list(self.cur.fetchone())
            book = self.change_str_from_mysql(book)
            Book_info.append(book)
        temp = [Reader_info, Record_info, Book_info]
        return temp

    def lookup_Book_by_like(self, Book_info):
        """
    look up books that whose names contains the key words
    @param Book_info:   the key words that to be looked up 
    @type Book_info:    list[string,...]
    @return temp:       information abouts the books
    @rtyoe temp:        lst
        """
        command = u"""SELECT * FROM Book WHERE """
        for i in range(len(Book_info)):
            Book_info[i] = 'Book_name like "%' + Book_info[i] + '%"'
        string = " AND ".join(Book_info)
        command += string
        #print command
        self.cur.execute(command)
        data = self.cur.fetchall()
        temp = []
        for i in range(len(data)):
            temp.append(list(data[i]))
            temp[i] = self.change_str_from_mysql(temp[i])
        return temp

    def change_str_from_mysql(self, alist):
        """
    the function to change "^" to "'" and "`" to '"' about the data looked up from MySQL
    @param alist:   the data to be changed
    @type alist:    list
    @return alist:  the changed to be returned
    @rtype alist:   list
        """
        for i in range(len(alist)):
            alist[i] = str(alist[i])
        string = "##".join(alist)
        string = string.replace("^","'")
        string = string.replace("`",'"')
        alist = string.split("##")
        return alist

def main():
    """
the main function for testing
    """
    #con = mdb.connect('localhost', 'library', '123456', 'librarydb', charset='utf8')
    #mg = lib_student(con)
    #print "--------------------------------"
    #print "test lookup_Book_by_like()"
    #data = mg.lookup_Book_by_like(["aa",'sd'])
    #for i in data:
    #    print i

    #print "-------------------------------"
    #print "test lookup_person_info()"
    #data = mg.lookup_person_info(20090123)
    #for i in data:
    #    for j in i:
    #        print j,
    #    print "\n"
if __name__ == "__main__":
    main()
