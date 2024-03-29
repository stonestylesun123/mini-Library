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
#"""
#clas lib_manager
#contains function:
#    1  lookup book
#        a. look up a book by it's ID
#        b. look up a book by it's name
#    2  add books
#    3  delete books
#    4  lookup reader
#    5  add reader
#    6  delete reader
#    7  borrow processing
#    8  renew processing
#    9  return processing
#    10 borrow timeout processing
#    11 recover borrow privilege
#"""

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
        if data == None:
            return False
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
        command = u"""self.cur.execute("SELECT * FROM Book WHERE Book_name = '%s'")""" % Book_name
        #print command
        exec(command)
        data = self.cur.fetchone()
        if data == None:
            return False
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

    def update_Book(self, Book_info):
        Book_info = self.change_str_to_mysql(Book_info)
        Book_id = Book_info[0]
        Book_info.remove(Book_id)
        Book_info.append(Book_id)
        Book_info = tuple(Book_info)
        command = u"""self.cur.execute("UPDATE Book SET Book_name='%s', Book_author='%s', Book_publisher='%s', Book_type='%s', Book_amount='%s', lended_amount='%s', Book_remarks='%s' WHERE Book_id='%s' ")""" % Book_info
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
        if data == None:
            return False
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
        command = u"""self.cur.execute('INSERT INTO Reader VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s")')""" % Reader_info
        print command
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

    def update_Reader(self, Reader_info):
        Reader_info = self.change_str_to_mysql(Reader_info)
        Reader_id = Reader_info[0]
        Reader_info.remove(Reader_id)
        Reader_info.append(Reader_id)
        Reader_info = tuple(Reader_info)
        command = u"""self.cur.execute("UPDATE Reader SET Reader_name='%s', Reader_gender='%s', Reader_email='%s', lended_book_count='%s', get_right_to_borrow='%s', Reader_remarks='%s' WHERE Reader_id='%s'")""" % Reader_info
        print command
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
        if bookinfo[0][0] - bookinfo[0][1] <= 0:
            return [0,"No books remained!"]
        command = u"""self.cur.execute("SELECT get_right_to_borrow,lended_book_count FROM Reader WHERE Reader_id = %s")""" % Reader_id
        exec(command)
        readerinfo = self.cur.fetchone()
        if readerinfo[0] == False:
            return [0,"You don't have the right to borrow book!"]
        if readerinfo[1] == 10:
            return [0,"You hava already borrowed 10 books yet!"]
        if self.is_record_existed(Reader_id, Book_id):
            return [0,"You hava already borrowed that book!"]
        else:
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
            return [1,'OK!']

    def return_book(self, Reader_id, Book_id):
        """
    return book processing
    @param Reader_id:   the ID of the reader to return a book
    @type Reader_id:    string/integer
    @param Book_id:     the ID of the book to be returned
    @type Book_id:      string/integer
        """
        command = u"""self.cur.execute("DELETE FROM Record WHERE R_id = %s AND B_id = %s")""" % (Reader_id, Book_id)
        exec(command)
        self.reader_borrow_or_return_a_book(Reader_id, Book_id, False)

    def is_record_existed(self, Reader_id, Book_id):
        command = u"""self.cur.execute("SELECT * FROM Record WHERE R_id = %s AND B_id = %s")""" % (Reader_id, Book_id)
        exec(command)
        data = self.cur.fetchone()
        if data == None:
            return False
        else:
            return True

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

    def get_right_to_borrow(self, Reader_id):
        command = """self.cur.execute("SELECT get_right_to_borrow FROM Reader WHERE Reader_id='%s'")""" % Reader_id
        exec(command)
        data = self.cur.fetchone()
        return data[0]

    def lookup_Record(self, Reader_id):
        command = """self.cur.execute("SELECT B_id FROM Record WHERE R_id='%s'")""" % Reader_id
        exec(command)
        data = self.cur.fetchall()
        books = []
        for i in range(len(data)):
            books.append(data[i][0])
        temp = []
        for i in books:
            temp.append(self.lookup_Book_by_ID(str(i)))
        #print temp
        return temp

    def set_right_to_borrow(self, Reader_id, status):
        if status == 'YES' or status == 'yes' or status == '1' or status == 1 or status == True:
            status == 1
        else:
            status == 0
        command = """self.cur.execute("UPDATE Reader SET get_right_to_borrow='%s' WHERE Reader_id='%s'")""" % (status, Reader_id)
        exec(command)

    def check_whether_outdate(self, Reader_id, Book_id):
        command = """self.cur.execute("SELECT enddate FROM Record WHERE R_id='%s' AND B_id='%s'")""" % (Reader_id, Book_id)
        exec(command)
        data = self.cur.fetchone()
        endtime = data[0]
        import datetime
        today = datetime.datetime.now()
        if endtime.year < today.year:
            return True
        elif endtime.year > today.year:
            return False
        elif endtime.month > today.month:
            return False
        elif endtime.month < today.month:
            return True
        elif endtime.day < today.day:
            return True
        else:
            return False

    def lookup_Record_date(self, Reader_id, Book_id):
        command = """self.cur.execute("SELECT startdate,enddate FROM Record WHERE R_id='%s' AND B_id='%s'")""" % (Reader_id, Book_id)
        exec(command)
        data = self.cur.fetchone()
        st = '-'.join([str(data[0].year),str(data[0].month),str(data[0].day)])
        et = '-'.join([str(data[1].year),str(data[1].month),str(data[1].day)])
        return [st, et]

    def lookup_Record_renewed(self, Reader_id, Book_id):
        command = """self.cur.execute("SELECT is_renewed FROM Record WHERE R_id='%s' AND B_id='%s'")""" % (Reader_id, Book_id)
        exec(command)
        data = self.cur.fetchone()
        if data[0]:
            return True
        else:
            return False

    def set_renewed(self, Reader_id, Book_id):
        command = """self.cur.execute("UPDATE Record SET is_renewed='1' WHERE R_id='%s' AND B_id='%s'")""" % (Reader_id, Book_id)
        exec(command)

    def set_Record_date(self, Reader_id, Book_id, startdate, enddate):
        command = """self.cur.execute("UPDATE Record SET startdate='%s',enddate='%s' WHERE R_id='%s' AND B_id='%s'")""" % (startdate, enddate, Reader_id, Book_id)
        exec(command)

    def renew_Record(self, Reader_id, Book_id):
        date = self.lookup_Record_date(Reader_id, Book_id)
        import datetime as dt
        temp = date[1].split('-')
        end = dt.date(int(temp[0]), int(temp[1]), int(temp[2]))
        ne = end + dt.timedelta(days=15)
        nes = str(ne.year) + '-' + str(ne.month) + '-' + str(ne.day)
        self.set_Record_date(Reader_id, Book_id, date[0], nes)
        self.set_renewed(Reader_id, Book_id)
	
    def punishment(self, Reader_id, right, remark):
	command = """self.cur.execute("UPDATE Reader SET get_right_to_borrow='%s', Reader_remarks='%s' WHERE Reader_id='%s'")""" % (right, remark, Reader_id)
	exec(command)

def main():
    """
the main function for testing
    """
    con = mdb.connect('localhost', 'library', '123456', 'librarydb', charset="utf8")
    mg = lib_manager(con)
    #mg.punishment('20090001', '0', 'no')
    #print "---------------------------"
    #print "test renew_Record()"
    #mg.renew_Record(20090001,123)

    #print "---------------------------"
    #print "test set_Record_date()"
    #mg.set_Record_date('20090001', '100', '2012-01-01', '2012-02-01')

    #print "----------------------------"
    #print "test lookup_Record_date()"
    #mg.lookup_Record_date(20090001,123)

    #print "---------------------------"
    #print "test set_renewed()"
    #mg.set_renewed(20090001, 124)

    #print "----------------------------"
    #print "test lookup_Record_renewed()"
    #print mg.lookup_Record_renewed(20090001,123)

    #print "----------------------------"
    #print "test add_Reader()"
    #f = open('Reader_v1.1','r')
    #lines = f.readlines()
    #for i in lines:
    #    temp = i.split('##') 
    #    temp[len(temp) - 1] = temp[len(temp) - 1].rstrip()
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
    #mg.return_book(20090001,999)

    #print "-----------------------"
    #print "test update_Book()"
    #Book_info = ['1', 'stonestyle', 'stone', 'stone inc', 'IT', '10', '0', 'no remark!']
    #mg.update_Book(Book_info)

    #print "-----------------------"
    #print "test update_Book()"
    #Reader_info = ['20090001', 'stone', 'M', 'stone@qq.com', '0', '1', 'no remark!']
    #mg.update_Reader(Reader_info)

    #print "----------------------"
    #print "test get_right_to_borrow()"
    #mg.get_right_to_borrow('20090001')

    #print "---------------------"
    #print "test lookup_Record()"
    #mg.lookup_Record('20090009')

    #print "--------------------"
    #print "test set_right_to_borrow()"
    #mg.set_right_to_borrow('20090022', 1)

    #print "-------------------"
    #print "test check_whether_outdate()"
    #print mg.check_whether_outdate('20090001', '100')

    #print "-------------------"
    #print "test is_record_existed()"
    #print mg.is_record_existed('20090001','1')
if __name__ == "__main__":
    main()
