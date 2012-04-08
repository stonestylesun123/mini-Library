#! /usr/bin/python
# coding: utf-8

import wx
#import lib_manager

subUI = ['book_look_up', 'reader_look_up', 'book_manager', 'reader_manager', 'book_borrow', 'book_return']

class submanagerUI(wx.Panel):
    def __init__(self, parent, id, choice):
        wx.Panel.__init__(self, parent, id=-1, size=(300,300))
        self.setchoice(choice)
        
    def setchoice(self, choice):
        self.choice = choice
        self.change()

    def change(self):
        string = "sizer = self.%s()" % subUI[int(self.choice) - 1]
        exec(string)
        self.SetSizer(sizer)

    def book_look_up(self):
        vobx = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        cb1 = wx.ComboBox(self, -1, size=(125,26), choices=['按书号查询','按书名查询'])
        #tc1 = wx.TextCtrl(self, -1, size=(90, 26))
        #bt1 = wx.Button(self, -1, label='查询')
        hbox.Add(cb1, proportion=0, flag=wx.LEFT|wx.RIGHT, border=10)
        #hbox.Add(tc1, proportion=1, flag=wx.LEFT|wx.RIGHT, border=10)
        #hbox.Add(bt1, proportion=0, flag=wx.LEFT|wx.RIGHT, border=10)
        return hbox

    def reader_look_up(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        bt1 = wx.Button(self, -1, label='查询')
        hbox.Add(bt1, proportion=0, flag=wx.LEFT|wx.RIGHT, border=10)
        return hbox

    def book_manager(self):
        pass

    def reader_manager(self):
        pass

    def book_borrow(self):
        pass

    def book_return(self):
        pass
