#! /usr/bin/python
# coding: utf-8

import wx
from lib_manager import lib_manager

subUI = ['book_look_up_UI', 'reader_look_up_UI', 'book_manager_UI', 'reader_manager_UI', 'book_borrow_UI', 'book_return_UI']

class submanagerUI(wx.Panel):
    def __init__(self, parent, id, choice, connection):
        wx.Panel.__init__(self, parent, id=-1, size=(850,400))
        self.setchoice(choice)
	self.connection = connection
        self.lib_manager = lib_manager(self.connection)

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
        sizer.Add(u1_st0, pos=(0,0), flag=wx.ALL, border=18)
        sizer.Add(u1_st1, pos=(0,1), flag=wx.ALL, border=18)
        sizer.Add(self.u1_cb1, pos=(0,2), flag=wx.ALL, border=15)
        sizer.Add(self.u1_tc1, pos=(0,3), flag=wx.ALL, border=15)
        sizer.Add(u1_bt1, pos=(0,4), flag=wx.ALL, border=12)
        vbox.Add(sizer)
        line = wx.StaticLine(self)
        vbox.Add(line, proportion=0, flag=wx.ALL|wx.EXPAND, border=10)
        sizer2 = wx.GridBagSizer(5,4)
        u1_st2 = wx.StaticText(self, -1, label="查询结果")
        u1_st2.SetForegroundColour('#3014D4')
        u1_st3 = wx.StaticText(self, -1, label="id")
        self.u1_tc3 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u1_tc3.Disable()
        u1_st4 = wx.StaticText(self, -1, label="name")
        self.u1_tc4 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u1_tc4.Disable()
        u1_st5 = wx.StaticText(self, -1, label="author")
        self.u1_tc5 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u1_tc5.Disable()
        u1_st6 = wx.StaticText(self, -1, label="publisher")
        self.u1_tc6 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u1_tc6.Disable()
        u1_st7 = wx.StaticText(self, -1, label="type")
        self.u1_tc7 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u1_tc7.Disable()
        u1_st8 = wx.StaticText(self, -1, label="amount")
        self.u1_tc8 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u1_tc8.Disable()
        u1_st9 = wx.StaticText(self, -1, label="lended_amount")
        self.u1_tc9 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u1_tc9.Disable()
        u1_st10= wx.StaticText(self, -1, label="remarks")
        self.u1_tc10= wx.TextCtrl(self, -1, size=(240, 26))
        self.u1_tc10.Disable()
        sizer2.Add(u1_st2, pos=(0,0), flag=wx.ALL, border=5)
        sizer2.Add(u1_st3, pos=(1,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u1_tc3, pos=(1,1), flag=wx.ALL, border=5)
        sizer2.Add(u1_st4, pos=(1,2), flag=wx.ALL, border=5)
        sizer2.Add(self.u1_tc4, pos=(1,3), flag=wx.ALL, border=5)
        sizer2.Add(u1_st5, pos=(2,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u1_tc5, pos=(2,1), flag=wx.ALL, border=5)
        sizer2.Add(u1_st6, pos=(2,2), flag=wx.ALL, border=5)
        sizer2.Add(self.u1_tc6, pos=(2,3), flag=wx.ALL, border=5)
        sizer2.Add(u1_st7, pos=(3,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u1_tc7, pos=(3,1), flag=wx.ALL, border=5)
        sizer2.Add(u1_st8, pos=(3,2), flag=wx.ALL, border=5)
        sizer2.Add(self.u1_tc8, pos=(3,3), flag=wx.ALL, border=5)
        sizer2.Add(u1_st9, pos=(4,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u1_tc9, pos=(4,1), flag=wx.ALL, border=5)
        sizer2.Add(u1_st10,pos=(4,2), flag=wx.ALL, border=5)
        sizer2.Add(self.u1_tc10,pos=(4,3), flag=wx.ALL, border=5)
        vbox.Add(sizer2, proportion=0, flag=wx.LEFT|wx.EXPAND, border=15)
        self.Bind(wx.EVT_BUTTON, self.booklookup, u1_bt1)

        return vbox

    def booklookup(self, e):
        choice = self.u1_cb1.GetValue()
        string = self.u1_tc1.GetValue()
        print string
        if string == "" or choice == "":
            wx.MessageBox('Invalid input!', 'Error', wx.OK | wx.ICON_ERROR)
        else:
            if choice == "按书号查询":
                result = self.lib_manager.lookup_Book_by_ID(string)
            else:
                result = self.lib_manager.lookup_Book_by_NAME(string)
            if result == None:
                wx.MessageBox('Does not exist', 'Error', wx.OK | wx.ICON_ERROR)
            else:
                firstline = ['id','name','author','publisher','type','amount','lended_amount','remarks']
                resultstr = ""
                for i in range(len(result)):
                    command = """self.u1_tc%d.SetValue("%s")""" % ((i + 3), result[i])
                    exec(command)

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
