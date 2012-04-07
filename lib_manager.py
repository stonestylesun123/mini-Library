#! /usr/bin/python
# -*- coding: utf-8 -*-
# @author:  huangxiaohui
# @version: V1.0
# @time:    2012-


# import MySQLdb module
import MySQLdb as mdb
import sys

# 设置编码utf-8
reload(sys);
sys.setdefaultencoding('utf-8')

class lib_manager:
"""
clas lib_manager
contains function:
    1  lookup book
        a. look up a book by it's ID
        b. look up a book by it's name
    2  add books
    3  delete books
    4  lookup reader
    5  add reader
    6  delete reader
    7  borrow processing
    8  renew processing
    9  return processing
    10 borrow timeout processing
    11 recover borrow privilege
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
    @param Book_id: book ID
    @type Book_id:  string/integer
    @return data:        information about a book
    @rtype data:         list
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
    @param Book_name:   the name of the book looked up
    @type Book_name:    string
    @return data:       information about a book
    @rtype data:        list
        """
        command = u"""self.cur.execute("SELECT * FROM Book WHERE Book_name = %s")""" % Book_name
        #print command
        exec(command)
        data = self.cur.fetchone()
        data = list(data)
        data = self.change_str_from_mysql(data)
        return data

    def add_Book(self, Book_info):
        """
    add books into the MySQL 
    @param Book_info:   information about the book
    @type Book_info:    list
        """
        Book_info = self.change_str_to_mysql(Book_info)
        Book_info = tuple(Book_info)
        command = u"""self.cur.execute("INSERT INTO Book VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')")""" % Book_info
        #print command
        exec(command)

    def del_Book(self, Book_id):
        """
    delete books from MySQL
    @param Book_id: the ID of the book to delete
    @type Book_id:  string/integer
        """
        command = u"""self.cur.execute("DELETE FROM Book WHERE Book_id = %s")""" % Book_id
        #print command
        exec(command)

    def lookup_Reader(self, Reader_id):
        """
    look up a reader by his ID
    @param Reader_id:   the ID of the Reader to look up
    @type Reader_id:    string/integer
    @return data:       information about the reader
    @rtype data:        list
        """
        command = u"""self.cur.execute("SELECT * FROM Reader WHERE Reader_id = %s")""" % Reader_id
        #print command
        exec(command)
        data = self.cur.fetchone()
        data = list(data)
        data = self.change_str_from_mysql(data)
        return data

    def add_Reader(self, Reader_info):
        """
    add reader into MySQL
    @param Reader_info: information about a reader
    @type Reader_info:  list
        """
        Reader_info = self.change_str_to_mysql(Reader_info)
        Reader_info = tuple(Reader_info)
        command = u"""self.cur.execute('INSERT INTO Reader VALUES("%s", "%s", "%s", "%s", "%s")')""" % Reader_info
        #print command
        exec(command)
        
    def del_Reader(self, Reader_id):
        """
    delete reader from MySQL
    @param Reader_id:   the ID of a reader
    @type Reader_id:    string/integer
        """
        command = u"""self.cur.execute("DELETE FROM Reader WHERE Reader_id = %s")""" % Reader_id
        #print command
        exec(command)

    def borrow_book(self, Reader_id, Book_id):
        """
    borrow processing
    @param Reader_id:   the ID of the reader to borrow a book
    @type Reader_id:    string/integer
    @param Book_id:     the ID of the book to be borrowed
    @type Book_id:      string/integer
        """
        command = u"""self.cur.execute("SELECT Book_amount, lended_amount FROM Book WHERE Book_id = %s")""" % Book_id
        #print command
        exec(command)
        bookinfo = self.cur.fetchall()
        if bookinfo[0][0] - bookinfo[0][1] > 0:
            command = u"""self.cur.execute("SELECT lended_book_count FROM Reader WHERE Reader_id = %s")""" % Reader_id
            exec(command)
            readerinfo = self.cur.fetchone()
            if readerinfo[0] == 10:
                print "You hava already borrower 10 books yet!"
            else:
                # 借书出错回滚？
                import time
                import datetime
                Record_id = time.ctime()
                R_id = str(Reader_id)
                B_id = str(Book_id)
                startdate = datetime.datetime.now()
                enddate = startdate + datetime.timedelta(days = 30)
                startdate = str(startdate.year) + '-' + str(startdate.month) + '-' + str(startdate.day)
                enddate = str(enddate.year) + '-' + str(enddate.month) + '-' +str(enddate.day)
                is_renewed = 'False'
                command = u"""self.cur.execute("INSERT INTO Record VALUES('%s', '%s', '%s', '%s', '%s', '%s')")""" % (Record_id, R_id, B_id, startdate, enddate, is_renewed)
                exec(command)
                self.reader_borrow_or_return_a_book(Reader_id, Book_id, True)
        else:
            print "No Books remained!"

    def return_book(self, Reader_id, Book_id):
        """
    return book processing
    @param Reader_id:   the ID of the reader to return a book
    @type Reader_id:    string/integer
    @param Book_id:     the ID of the book to be returned
    @type Book_id:      string/integer
        """
        command = u"""self.cur.execute("SELECT * FROM Record WHERE R_id = %s AND B_id = %s")""" % (Reader_id, Book_id)
        exec(command)
        data = self.cur.fetchone()
        if data == "":
            print "Not such record! Check your input!"
        else:
            command = u"""self.cur.execute("DELETE FROM Record WHERE R_id = %s AND B_id = %s")""" % (Reader_id, Book_id)
            exec(command)
            self.reader_borrow_or_return_a_book(Reader_id, Book_id, False)

    def reader_borrow_or_return_a_book(self, Reader_id, Book_id, status):
        """
    processing the data about Reader, Book from MySQL when reader borrowing or returning a book
    @param Reader_id:   the ID of the reader
    @type Reader_id:    string/integer
    @param Book_id:     the ID of the book
    @type Book_id:      string/integer
    @param status:      the flag of borrowing/returning book, True means borrow, False means return
    @type status:       boolean
        """
        command = u"""self.cur.execute("SELECT lended_book_count FROM Reader WHERE Reader_id = %s")""" % Reader_id
        exec(command)
        data = self.cur.fetchone()
        data = int(data[0])
        if status:
            data += 1
        else:
            data -= 1
        command = u"""self.cur.execute("UPDATE Reader SET lended_book_count = %s WHERE Reader_id = %s")""" % (data, Reader_id)
        exec(command)

        command = u"""self.cur.execute("SELECT lended_amount FROM Book WHERE Book_id = %s")""" % Book_id
        exec(command)
        data = self.cur.fetchone()
        data = int(data[0])
        if status:
            data += 1
        else:
            data -= 1
        command = u"""self.cur.execute("UPDATE Book SET lended_amount = %s WHERE Book_id = %s")""" % (data, Book_id)
        exec(command)

    def change_str_from_mysql(self, alist):
        """
    the function to change "^" to "'" and "`" to '"' about the data looked up from MySQL
    @param alist:   the data to be changed
    @type alist:    list
    @return alist:  the changed data to be returned
    @rtype alist:   list
        """
        for i in range(len(alist)):
            alist[i] = str(alist[i])
        string = "##".join(alist)
        string = string.replace("^","'")
        string = string.replace("`",'"')
        alist = string.split("##")
        return alist

    def change_str_to_mysql(self, alist):
        """
    the function to change "'" to "^" and '"' to "`" about the data to be written into MySQL
    @param alist:   the data to be changed
    @type alist:    list
    @return alist:  the changed data to be returned
    @rtype alist:   list
        """
        for i in range(len(alist)):
            alist[i] = str(alist[i])
        string = "##".join(alist)
        string = string.replace("'","^")
        string = string.replace('"',"`")
        alist = string.split("##")
        return alist

def main():
    """
the main function for testing
    """
    #con = mdb.connect('localhost', 'library', '123456', 'librarydb', charset="utf8")
    #mg = lib_manager(con)
    #print "----------------------------"
    #print "test add_Reader()"
    #f = open('Reader_v1.0','r')
    #lines = f.readlines()
    #for i in lines:
    #    temp = i.split() 
    #    print temp
    #    mg.add_Reader(temp)

    #print "-----------------------------"
    #print "test lookup_Reader()"
    #rid = '20090453'
    #msg = mg.lookup_Reader(rid)
    #print msg
    #for i in msg:
    #    print i,

    #print "----------------------------"
    #print "test del_Reader()"
    #rid = "20090123"
    #mg.del_Reader(rid)

    #print "---------------------------"
    #print "test add_Book()"
    #f = open('Book_v1.0','r')
    #lines = f.readlines()
    #for i in lines:
    #    temp = i.split('##')
    #    temp[len(temp) -1] = temp[len(temp) - 1].rstrip()
    #    print temp
    #    mg.add_Book(temp)

    #print "--------------------------"
    #print "test lookup_Book_by_ID()"
    #bid = '5555'
    #msg = mg.lookup_Book_by_ID(bid)
    #print msg
    
    #print "-------------------------"
    #print "test del_Book()"
    #bid = '5553'
    #mg.del_Book(bid)

    #print "-------------------------"
    #print "test borrow_book()"
    #mg.borrow_book(20090002,3)
    
    #print "-----------------------"
    #print "test return_book()"
    #mg.return_book(20090002,2)

if __name__ == "__main__":
    main()
