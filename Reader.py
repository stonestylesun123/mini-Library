#! /usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

class Reader:
    def __init__(self, Reader_id, Reader_name, Reader_gender, Reader_email, lended_book_count=0):
        self.Reader_id=Reader_id
        self.Reader_name=Reader_name
        self.Reader_gender=Reader_gender
        self.Reader_email=Reader_email
        self.lended_book_count=lended_book_count
