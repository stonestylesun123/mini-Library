#! /usr/bin/python
# coding: utf-8

import wx
from lib_manager import lib_manager

subUI = ['book_look_up_UI', 'reader_look_up_UI', 'book_manager_UI', 'reader_manager_UI', 'book_borrow_UI', 'book_return_UI']

class submanagerUI(wx.Panel):
    def __init__(self, parent, id, choice):
        wx.Panel.__init__(self, parent, id=-1, size=(850,400))
        self.setchoice(choice)
        self.lib_manager = lib_manager

    def setchoice(self, choice):
        self.choice = choice
        self.change()

    def change(self):
        string = "sizer = self.%s()" % subUI[int(self.choice) - 1]
        exec(string)
        self.SetSizer(sizer)

    def book_look_up_UI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        sizer = wx.GridBagSizer(1,5)
        u1_st0 = wx.StaticText(self, -1, label="图书查询")
        u1_st0.SetForegroundColour('#3014D4')
        u1_st1 = wx.StaticText(self, -1, label="请选择查询方式")
        self.u1_cb1 = wx.ComboBox(self, -1, size=(125,26), choices=['按书号查询','按书名查询'])
        self.u1_tc1 = wx.TextCtrl(self, -1, size=(120, 26))
        u1_bt1 = wx.Button(self, -1, label='查询')
        u1_tc2 = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        sizer.Add(u1_st0, pos=(0,0), flag=wx.ALL, border=18)
        sizer.Add(u1_st1, pos=(0,1), flag=wx.ALL, border=18)
        sizer.Add(self.u1_cb1, pos=(0,2), flag=wx.ALL, border=15)
        sizer.Add(self.u1_tc1, pos=(0,3), flag=wx.ALL, border=15)
        sizer.Add(u1_bt1, pos=(0,4), flag=wx.ALL, border=12)
        vbox.Add(sizer)
        line = wx.StaticLine(self)
        vbox.Add(line, proportion=0, flag=wx.ALL|wx.EXPAND, border=10)
        vbox.Add(u1_tc2, proportion=2,flag=wx.ALL|wx.EXPAND, border=15 )
        self.Bind(wx.EVT_BUTTON, self.booklookup, u1_bt1)

        return vbox

    def booklookup(self, e):
        choice = self.u1_cb1.GetValue()
        string = self.u1_tc1.GetValue()
        if string == "" or choice == "":
            wx.MessageBox('Invalid input!', 'Error', wx.OK | wx.ICON_ERROR)
        else:
	    pass

    def reader_look_up_UI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        sizer = wx.GridBagSizer(1,4)
        st1 = wx.StaticText(self, -1, label="请选择查询方式")
        cb1 = wx.ComboBox(self, -1, size=(125,26), choices=['按书号查询','按书名查询'])
        tc1 = wx.TextCtrl(self, -1, size=(120, 26))
        bt1 = wx.Button(self, -1, label='查询')
        tc2 = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        sizer.Add(st1, pos=(0,0), flag=wx.ALL, border=18)
        sizer.Add(cb1, pos=(0,1), flag=wx.ALL, border=15)
        sizer.Add(tc1, pos=(0,2), flag=wx.ALL, border=15)
        sizer.Add(bt1, pos=(0,3), flag=wx.ALL, border=12)
        vbox.Add(sizer)
        line = wx.StaticLine(self)
        vbox.Add(line, proportion=0, flag=wx.ALL|wx.EXPAND, border=15)
        vbox.Add(tc2, proportion=2,flag=wx.ALL|wx.EXPAND, border=15 )
        return vbox

    def book_manager_UI(self):
        pass

    def reader_manager_UI(self):
        pass

    def book_borrow_UI(self):
        pass

    def book_return_UI(self):
        pass
