#! /usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

class Book:
    def __init__(self, Book_id, Book_name, Book_author, Book_publisher, Book_type, Book_amount, lended_amount=0, Book_remarks="no remarks!"):
        self.Book_id=Book_id
        self.Book_name=Book_name
        self.Book_author=Book_author
        self.Book_publisher=Book_publisher
        self.Book_type=Book_type
        self.Book_amount=Book_amount
        self.lended_amount=lended_amount
        self.Book_remarks=Book_remarks
