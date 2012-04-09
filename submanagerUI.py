#! /usr/bin/python
# coding: utf-8

import wx
from lib_manager import lib_manager

subUI = ['book_look_up_UI', 'reader_look_up_UI', 'book_manager_UI', 'reader_manager_UI', 'book_borrow_UI', 'book_return_UI']

class submanagerUI(wx.Panel):
    def __init__(self, parent, id, choice, connection):
        wx.Panel.__init__(self, parent, id=-1, size=(845,500))
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
        sizer = wx.GridBagSizer(1,7)
        u1_st0 = wx.StaticText(self, -1, label="图书查询")
        u1_st0.SetForegroundColour('#3014D4')
        u1_st1 = wx.StaticText(self, -1, label="请选择查询方式")
        self.u1_cb1 = wx.ComboBox(self, -1, size=(115,26), choices=['按书号查询','按书名查询'])
        self.u1_tc1 = wx.TextCtrl(self, -1, size=(105, 26))
        u1_bt1 = wx.Button(self, 201, label='查询')
        u1_new_bt1 = wx.Button(self, 202, label='修改')
        u1_new_bt2 = wx.Button(self, 203, label='提交')
        sizer.Add(u1_st0, pos=(0,0), flag=wx.ALL, border=15)
        sizer.Add(u1_st1, pos=(0,1), flag=wx.ALL, border=15)
        sizer.Add(self.u1_cb1, pos=(0,2), flag=wx.ALL, border=12)
        sizer.Add(self.u1_tc1, pos=(0,3), flag=wx.ALL, border=12)
        sizer.Add(u1_bt1, pos=(0,4), flag=wx.ALL, border=9)
        sizer.Add(u1_new_bt1, pos=(0,5), flag=wx.ALL, border=9)
        sizer.Add(u1_new_bt2, pos=(0,6), flag=wx.ALL, border=9)
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
        self.u1_lookup = False
        self.u1_changed = False
        self.u1_handon = False
        self.Bind(wx.EVT_BUTTON, self.booklookup, u1_bt1)
        self.Bind(wx.EVT_BUTTON, self.booklookup, u1_new_bt1)
        self.Bind(wx.EVT_BUTTON, self.booklookup, u1_new_bt2)

        return vbox

    def booklookup(self, e):
        if e.GetId() == 201:
            if self.u1_handon:
                dial = wx.MessageDialog(None, 'Are you sure to quit without saving changes?', 'Question', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
                    
                ret = dial.ShowModal()
                if not ret == wx.ID_YES:
                    return 
                else: 
                    for i in range(1,8):
                        command = "self.u1_tc%d.Disable()" % (i + 3)
                        exec(command)
            choice = self.u1_cb1.GetValue()
            string = self.u1_tc1.GetValue()
            if string == "" or choice == "":
                wx.MessageBox('Invalid input!', 'Error', wx.OK | wx.ICON_ERROR)
            else:
                if choice == "按书号查询":
                    result = self.lib_manager.lookup_Book_by_ID(string)
                else:
                    result = self.lib_manager.lookup_Book_by_NAME(string)
                if result == None or result == False:
                    wx.MessageBox('Does not exist', 'Error', wx.OK | wx.ICON_ERROR)
                else:
                    print result
                    for i in range(len(result)):
                        command = """self.u1_tc%d.SetValue("%s")""" % ((i + 3), result[i])
                        exec(command)
                    self.u1_lookup = True
                    self.u1_changed = False
                    self.u1_handon = False
        if e.GetId() == 202:
            if not self.u1_lookup:
                wx.MessageBox('请先查询再修改', 'Error', wx.OK | wx.ICON_ERROR)
            else:
                for i in range(1,8):
                    command = "self.u1_tc%d.Enable()" % (i + 3)
                    exec(command)
                self.u1_changed = True
                self.u1_handon = True
        if e.GetId() == 203:
            if not self.u1_changed:
                wx.MessageBox('请先修改再提交', 'Error', wx.OK | wx.ICON_ERROR)
            elif not self.u1_lookup:
                wx.MessageBox('请先查询', 'Error', wx.OK | wx.ICON_ERROR)
            else:
                temp = []
                for i in range(8):
                    command = "tmp = self.u1_tc%d.GetValue()" % (i + 3)
                    exec(command)
                    temp.append(tmp)
                #print temp
                self.lib_manager.update_Book(temp)
                self.u1_handon = False

                for i in range(1,8):
                    command = "self.u1_tc%d.Disable()" % (i + 3)
                    exec(command)

    def reader_look_up_UI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        sizer = wx.GridBagSizer(1,6)
        u2_st0 = wx.StaticText(self, -1, label="读者查询")
        u2_st0.SetForegroundColour('#3014D4')
        u2_st1 = wx.StaticText(self, -1, label="请输入读者ID")
        self.u2_tc1 = wx.TextCtrl(self, -1, size=(120, 26))
        u2_bt1 = wx.Button(self, 301, label='查询')
        u2_new_bt1 = wx.Button(self, 302, label='修改')
        u2_new_bt2 = wx.Button(self, 303, label='提交')
        sizer.Add(u2_st0, pos=(0,0), flag=wx.ALL, border=18)
        sizer.Add(u2_st1, pos=(0,1), flag=wx.ALL, border=18)
        sizer.Add(self.u2_tc1, pos=(0,2), flag=wx.ALL, border=15)
        sizer.Add(u2_bt1, pos=(0,3), flag=wx.ALL, border=12)
        sizer.Add(u2_new_bt1, pos=(0,4), flag=wx.ALL, border=12)
        sizer.Add(u2_new_bt2, pos=(0,5), flag=wx.ALL, border=12)
        vbox.Add(sizer)
        line = wx.StaticLine(self)
        vbox.Add(line, proportion=0, flag=wx.ALL|wx.EXPAND, border=10)
        sizer2 = wx.GridBagSizer(5,4)
        u2_st2 = wx.StaticText(self, -1, label="查询结果：YES，yes，1表示有权限借书，其他表示没有权限")
        u2_st2.SetForegroundColour('#3014D4')
        u2_st3 = wx.StaticText(self, -1, label="id")
        self.u2_tc3 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u2_tc3.Disable()
        u2_st4 = wx.StaticText(self, -1, label="name")
        self.u2_tc4 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u2_tc4.Disable()
        u2_st5 = wx.StaticText(self, -1, label="gender")
        self.u2_tc5 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u2_tc5.Disable()
        u2_st6 = wx.StaticText(self, -1, label="email")
        self.u2_tc6 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u2_tc6.Disable()
        u2_st7 = wx.StaticText(self, -1, label="lended book amount")
        self.u2_tc7 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u2_tc7.Disable()
        u2_st8 = wx.StaticText(self, -1, label="get right to borrow")
        self.u2_tc8 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u2_tc8.Disable()
        u2_st9 = wx.StaticText(self, -1, label="remark")
        self.u2_tc9 = wx.TextCtrl(self, -1, size=(240, 26))
        self.u2_tc9.Disable()
        sizer2.Add(u2_st2, pos=(0,0), span=(1,2), flag=wx.ALL|wx.ALIGN_LEFT, border=5)
        sizer2.Add(u2_st3, pos=(1,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u2_tc3, pos=(1,1), flag=wx.ALL, border=5)
        sizer2.Add(u2_st4, pos=(1,2), flag=wx.ALL, border=5)
        sizer2.Add(self.u2_tc4, pos=(1,3), flag=wx.ALL, border=5)
        sizer2.Add(u2_st5, pos=(2,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u2_tc5, pos=(2,1), flag=wx.ALL, border=5)
        sizer2.Add(u2_st6, pos=(2,2), flag=wx.ALL, border=5)
        sizer2.Add(self.u2_tc6, pos=(2,3), flag=wx.ALL, border=5)
        sizer2.Add(u2_st7, pos=(3,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u2_tc7, pos=(3,1), flag=wx.ALL, border=5)
        sizer2.Add(u2_st8, pos=(3,2), flag=wx.ALL, border=5)
        sizer2.Add(self.u2_tc8, pos=(3,3), flag=wx.ALL, border=5)
        sizer2.Add(u2_st9, pos=(4,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u2_tc9, pos=(4,1), flag=wx.ALL, border=5)
        vbox.Add(sizer2, proportion=0, flag=wx.LEFT|wx.EXPAND, border=15)
        self.u2_lookup = False
        self.u2_changed = False
        self.u2_handon = False
        self.Bind(wx.EVT_BUTTON, self.readerlookup, u2_bt1)
        self.Bind(wx.EVT_BUTTON, self.readerlookup, u2_new_bt1)
        self.Bind(wx.EVT_BUTTON, self.readerlookup, u2_new_bt2)

        return vbox

    def readerlookup(self, e):
        if e.GetId() == 301:
            if self.u2_handon:
                dial = wx.MessageDialog(None, 'Are you sure to quit without saving changes?', 'Question', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
                ret = dial.ShowModal()
                if not ret == wx.ID_YES:
                    return
                else:
                    for i in range(1, 7):
                        command = "self.u2_tc%d.Disable()" % (i + 3)
                        exec(command)
            string = self.u2_tc1.GetValue()
            if string == "":
                wx.MessageBox('Invalid input!', 'Error', wx.OK | wx.ICON_ERROR)
            else:
                result = self.lib_manager.lookup_Reader(string)
                if result == None or result == False:
                    wx.MessageBox('Does not exist', 'Error', wx.OK | wx.ICON_ERROR)
                else:
                    print result
                    resultstr = ""
                    for i in range(len(result)):
                        if not i == 5:
                            command = """self.u2_tc%d.SetValue("%s")""" % ((i + 3), result[i])
                            exec(command)
                        else:
			    if result[i] == '1':
				result[i] = 'YES'
			    else:
				result[i] = 'NO'
                            command = """self.u2_tc%d.SetValue("%s")""" % ((i + 3), result[i])
                            exec(command)
                    self.u2_lookup = True
                    self.u2_changed = False
                    self.u2_handon = False
        if e.GetId() == 302:
            if not self.u2_lookup:
                wx.MessageBox('请先查询再修改', 'Error', wx.OK | wx.ICON_ERROR)
            else:
                for i in range(1,7):
                    command = "self.u2_tc%d.Enable()" % (i + 3)
                    exec(command)
                self.u2_changed = True
                self.u2_handon = True
        if e.GetId() == 303:
            if not self.u2_changed:
                wx.MessageBox('请先修改再提交', 'Error', wx.OK | wx.ICON_ERROR)
            elif not self.u2_lookup:
                wx.MessageBox('请先查询', 'Error', wx.OK | wx.ICON_ERROR)
            else:
                temp = []
                for i in range(7):
                    command = "tmp = self.u2_tc%d.GetValue()" % (i + 3)
                    exec(command)
                    if i == 5:
			if tmp == 'YES' or tmp == 'yes' or tmp == '1':
                            tmp = 1
			else:
			    tmp = 0
                    temp.append(tmp)

                self.lib_manager.update_Reader(temp)
                self.u2_handon = False

                for i in range(1,7):
                    command = "self.u2_tc%d.Disable()" % (i + 3)
                    exec(command)

    def book_manager_UI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        sizer = wx.GridBagSizer(1,7)
        u3_st0 = wx.StaticText(self, -1, label="图书管理")
        u3_st0.SetForegroundColour('#3014D4')
        u3_st1 = wx.StaticText(self, -1, label="请输入书号")
        self.u3_tc1 = wx.TextCtrl(self, -1, size=(105, 26))
        u3_bt1 = wx.Button(self, 401, label='查询')
        u3_new_bt1 = wx.Button(self, 402, label='删除图书')
        u3_new_bt2 = wx.Button(self, 403, label='编辑图书信息')
        u3_new_bt3 = wx.Button(self, 404, label='图书入库')
        sizer.Add(u3_st0, pos=(0,0), flag=wx.ALL, border=15)
        sizer.Add(u3_st1, pos=(0,1), flag=wx.ALL, border=15)
        sizer.Add(self.u3_tc1, pos=(0,2), flag=wx.ALL, border=12)
        sizer.Add(u3_bt1, pos=(0,3), flag=wx.ALL, border=9)
        sizer.Add(u3_new_bt1, pos=(0,4), flag=wx.ALL, border=9)
        sizer.Add(u3_new_bt2, pos=(0,5), flag=wx.ALL, border=9)
        sizer.Add(u3_new_bt3, pos=(0,6), flag=wx.ALL, border=9)
        vbox.Add(sizer)
        line = wx.StaticLine(self)
        vbox.Add(line, proportion=0, flag=wx.ALL|wx.EXPAND, border=10)
        sizer2 = wx.GridBagSizer(5,4)
        u3_st2 = wx.StaticText(self, -1, label="图书信息")
        u3_st2.SetForegroundColour('#3014D4')
        u3_st3 = wx.StaticText(self, -1, label="id")
        self.u3_tc3 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u3_tc3.Disable()
        u3_st4 = wx.StaticText(self, -1, label="name")
        self.u3_tc4 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u3_tc4.Disable()
        u3_st5 = wx.StaticText(self, -1, label="author")
        self.u3_tc5 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u3_tc5.Disable()
        u3_st6 = wx.StaticText(self, -1, label="publisher")
        self.u3_tc6 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u3_tc6.Disable()
        u3_st7 = wx.StaticText(self, -1, label="type")
        self.u3_tc7 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u3_tc7.Disable()
        u3_st8 = wx.StaticText(self, -1, label="amount")
        self.u3_tc8 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u3_tc8.Disable()
        u3_st9 = wx.StaticText(self, -1, label="lended_amount")
        self.u3_tc9 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u3_tc9.Disable()
        u3_st10= wx.StaticText(self, -1, label="remarks")
        self.u3_tc10= wx.TextCtrl(self, -1, size=(240, 26))
        self.u3_tc10.Disable()
        sizer2.Add(u3_st2, pos=(0,0), flag=wx.ALL, border=5)
        sizer2.Add(u3_st3, pos=(1,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u3_tc3, pos=(1,1), flag=wx.ALL, border=5)
        sizer2.Add(u3_st4, pos=(1,2), flag=wx.ALL, border=5)
        sizer2.Add(self.u3_tc4, pos=(1,3), flag=wx.ALL, border=5)
        sizer2.Add(u3_st5, pos=(2,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u3_tc5, pos=(2,1), flag=wx.ALL, border=5)
        sizer2.Add(u3_st6, pos=(2,2), flag=wx.ALL, border=5)
        sizer2.Add(self.u3_tc6, pos=(2,3), flag=wx.ALL, border=5)
        sizer2.Add(u3_st7, pos=(3,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u3_tc7, pos=(3,1), flag=wx.ALL, border=5)
        sizer2.Add(u3_st8, pos=(3,2), flag=wx.ALL, border=5)
        sizer2.Add(self.u3_tc8, pos=(3,3), flag=wx.ALL, border=5)
        sizer2.Add(u3_st9, pos=(4,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u3_tc9, pos=(4,1), flag=wx.ALL, border=5)
        sizer2.Add(u3_st10,pos=(4,2), flag=wx.ALL, border=5)
        sizer2.Add(self.u3_tc10,pos=(4,3), flag=wx.ALL, border=5)
        vbox.Add(sizer2, proportion=0, flag=wx.LEFT|wx.EXPAND, border=15)
        self.u3_lookup = False
        self.u3_edit = False
        self.u3_handon = False
        self.Bind(wx.EVT_BUTTON, self.bookmanage, u3_bt1)
        self.Bind(wx.EVT_BUTTON, self.bookmanage, u3_new_bt1)
        self.Bind(wx.EVT_BUTTON, self.bookmanage, u3_new_bt2)
	self.Bind(wx.EVT_BUTTON, self.bookmanage, u3_new_bt3)

        return vbox

    def bookmanage(self, e):
	if e.GetId() == 401:
	    string = self.u3_tc1.GetValue()
	    if string == "":
                wx.MessageBox('Invalid input!', 'Error', wx.OK | wx.ICON_ERROR)
            else:
		for i in range(8):
		    command = "self.u3_tc%d.Disable()" % (i + 3)
		    exec(command)
                result = self.lib_manager.lookup_Book_by_ID(string)
                if result == None or result == False:
                    wx.MessageBox('Does not exist', 'Error', wx.OK | wx.ICON_ERROR)
                else:
                    print result
                    for i in range(len(result)):
                        command = """self.u3_tc%d.SetValue("%s")""" % ((i + 3), result[i])
                        exec(command)
		    self.u3_lookup = True
	if e.GetId() == 402:
	    if not self.u3_lookup:
		wx.MessageBox('Select a book first!', 'Error', wx.OK | wx.ICON_ERROR)
	    else:
                dial = wx.MessageDialog(None, 'Are you sure to delete?', 'Question', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
                ret = dial.ShowModal()
		if ret == wx.ID_YES:
		    string = self.u3_tc3.GetValue()
		    self.lib_manager.del_Book(string)
		    self.u3_lookup = False
		    for i in range(8):
                        command = """self.u3_tc%d.SetValue("")""" % (i + 3)
                        exec(command)
		else:
		    return
	if e.GetId() == 403:
	    for i in range(8):
		command = """self.u3_tc%d.SetValue("")""" % (i + 3)
		exec(command)
		command = "self.u3_tc%d.Enable()" % (i + 3)
		exec(command)
	    self.u3_lookup = False
	    self.u3_edit = True
	if e.GetId() == 404:
	    if not self.u3_edit:
		wx.MessageBox('Editing first!', 'Error', wx.OK | wx.ICON_ERROR)
	    else:
                dial = wx.MessageDialog(None, 'Are you sure to add books?', 'Question', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
                ret = dial.ShowModal()
		if ret == wx.ID_YES:
                    temp = []
                    for i in range(8):
                    	command = "tmp = self.u3_tc%d.GetValue()" % (i + 3)
                    	exec(command)
                    	temp.append(tmp)
                    if temp[0] == "":
                        wx.MessageBox('Invalid input', 'Error', wx.OK | wx.ICON_ERROR)
			return
		    result = self.lib_manager.lookup_Book_by_ID(temp[0])
                    if not result == False:
                        wx.MessageBox('Invalid input or duplicate ID', 'Error', wx.OK | wx.ICON_ERROR)
			return
		    print temp
		    self.lib_manager.add_Book(temp)
		    self.u3_edit = False
		    for i in range(8):
                        command = """self.u3_tc%d.SetValue("")""" % (i + 3)
                        exec(command)
			command = "self.u3_tc%d.Disable()" % (i + 3)
			exec(command)     
		else:
		    return 
		
    def reader_manager_UI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        sizer = wx.GridBagSizer(1,7)
        u4_st0 = wx.StaticText(self, -1, label="读者查询")
        u4_st0.SetForegroundColour('#3014D4')
        u4_st1 = wx.StaticText(self, -1, label="请输入读者ID")
        self.u4_tc1 = wx.TextCtrl(self, -1, size=(120, 26))
        u4_bt1 = wx.Button(self, 501, label='查询')
        u4_new_bt1 = wx.Button(self, 502, label='删除读者')
        u4_new_bt2 = wx.Button(self, 503, label='编辑读者信息')
	u4_new_bt3 = wx.Button(self, 504, label='增加读者')
        sizer.Add(u4_st0, pos=(0,0), flag=wx.ALL, border=16)
        sizer.Add(u4_st1, pos=(0,1), flag=wx.ALL, border=16)
        sizer.Add(self.u4_tc1, pos=(0,2), flag=wx.ALL, border=13)
        sizer.Add(u4_bt1, pos=(0,3), flag=wx.ALL, border=10)
	sizer.Add(u4_new_bt1, pos=(0,4), flag=wx.ALL, border=10)
        sizer.Add(u4_new_bt2, pos=(0,5), flag=wx.ALL, border=10)
        sizer.Add(u4_new_bt3, pos=(0,6), flag=wx.ALL, border=10)
        vbox.Add(sizer)
        line = wx.StaticLine(self)
        vbox.Add(line, proportion=0, flag=wx.ALL|wx.EXPAND, border=10)
        sizer2 = wx.GridBagSizer(5,4)
        u4_st2 = wx.StaticText(self, -1, label="查询结果：YES，yes，1表示有权限借书，其他表示没有权限")
        u4_st2.SetForegroundColour('#3014D4')
        u4_st3 = wx.StaticText(self, -1, label="id")
        self.u4_tc3 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u4_tc3.Disable()
        u4_st4 = wx.StaticText(self, -1, label="name")
        self.u4_tc4 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u4_tc4.Disable()
        u4_st5 = wx.StaticText(self, -1, label="gender")
        self.u4_tc5 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u4_tc5.Disable()
        u4_st6 = wx.StaticText(self, -1, label="email")
        self.u4_tc6 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u4_tc6.Disable()
        u4_st7 = wx.StaticText(self, -1, label="lended book amount")
        self.u4_tc7 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u4_tc7.Disable()
        u4_st8 = wx.StaticText(self, -1, label="get right to borrow")
        self.u4_tc8 = wx.TextCtrl(self, -1, size=(180, 26))
        self.u4_tc8.Disable()
        u4_st9 = wx.StaticText(self, -1, label="remark")
        self.u4_tc9 = wx.TextCtrl(self, -1, size=(240, 26))
        self.u4_tc9.Disable()
        sizer2.Add(u4_st2, pos=(0,0), span=(1,2), flag=wx.ALL, border=5)
        sizer2.Add(u4_st3, pos=(1,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u4_tc3, pos=(1,1), flag=wx.ALL, border=5)
        sizer2.Add(u4_st4, pos=(1,2), flag=wx.ALL, border=5)
        sizer2.Add(self.u4_tc4, pos=(1,3), flag=wx.ALL, border=5)
        sizer2.Add(u4_st5, pos=(2,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u4_tc5, pos=(2,1), flag=wx.ALL, border=5)
        sizer2.Add(u4_st6, pos=(2,2), flag=wx.ALL, border=5)
        sizer2.Add(self.u4_tc6, pos=(2,3), flag=wx.ALL, border=5)
        sizer2.Add(u4_st7, pos=(3,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u4_tc7, pos=(3,1), flag=wx.ALL, border=5)
        sizer2.Add(u4_st8, pos=(3,2), flag=wx.ALL, border=5)
        sizer2.Add(self.u4_tc8, pos=(3,3), flag=wx.ALL, border=5)
        sizer2.Add(u4_st9, pos=(4,0), flag=wx.ALL, border=5)
        sizer2.Add(self.u4_tc9, pos=(4,1), flag=wx.ALL, border=5)
        vbox.Add(sizer2, proportion=0, flag=wx.LEFT|wx.EXPAND, border=15)
        self.u4_lookup = False
        self.u4_edit = False
        self.Bind(wx.EVT_BUTTON, self.readermanage, u4_bt1)
        self.Bind(wx.EVT_BUTTON, self.readermanage, u4_new_bt1)
        self.Bind(wx.EVT_BUTTON, self.readermanage, u4_new_bt2)
        self.Bind(wx.EVT_BUTTON, self.readermanage, u4_new_bt3)

        return vbox

    def readermanage(self, e):
	if e.GetId() == 501:
	    string = self.u4_tc1.GetValue()
	    if string == "":
                wx.MessageBox('Invalid input!', 'Error', wx.OK | wx.ICON_ERROR)
            else:
		for i in range(7):
		    command = "self.u4_tc%d.Disable()" % (i + 3)
		    exec(command)
                result = self.lib_manager.lookup_Reader(string)
                if result == None or result == False:
                    wx.MessageBox('Does not exist', 'Error', wx.OK | wx.ICON_ERROR)
                else:
                    print result
                    for i in range(len(result)):
                        if not i == 5:
                            command = """self.u4_tc%d.SetValue("%s")""" % ((i + 3), result[i])
                        else:
			    if result[i] == '1':
				result[i] = 'YSE'
			    else:
				result[i] = 'NO'
                            command = """self.u4_tc%d.SetValue("%s")""" % ((i + 3), result[i])
                        exec(command)
		    self.u4_lookup = True
	if e.GetId() == 502:
	    if not self.u4_lookup:
		wx.MessageBox('Select a reader first!', 'Error', wx.OK | wx.ICON_ERROR)
	    else:
                dial = wx.MessageDialog(None, 'Are you sure to delete?', 'Question', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
                ret = dial.ShowModal()
		if ret == wx.ID_YES:
		    string = self.u4_tc3.GetValue()
		    self.lib_manager.del_Reader(string)
		    self.u4_lookup = False
		    for i in range(7):
                        command = """self.u4_tc%d.SetValue("")""" % (i + 3)
                        exec(command)
		else:
		    return
	if e.GetId() == 503:
	    for i in range(7):
		command = """self.u4_tc%d.SetValue("")""" % (i + 3)
		exec(command)
		command = "self.u4_tc%d.Enable()" % (i + 3)
		exec(command)
	    self.u4_lookup = False
	    self.u4_edit = True
	if e.GetId() == 504:
	    if not self.u4_edit:
		wx.MessageBox('Editing first!', 'Error', wx.OK | wx.ICON_ERROR)
	    else:
                dial = wx.MessageDialog(None, 'Are you sure to add a reader?', 'Question', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
                ret = dial.ShowModal()
		if ret == wx.ID_YES:
                    temp = []
                    for i in range(7):
                    	command = "tmp = self.u4_tc%d.GetValue()" % (i + 3)
                    	exec(command)
                    	temp.append(tmp)
		    if temp[5] == "YSE" or temp[5] == "yes" or temp[5] == "1":
			temp[5] = "1"
		    else:
			temp[5] = "0"
		    print "temp[5]:",temp[5]
                    if temp[0] == "":
                        wx.MessageBox('Invalid input', 'Error', wx.OK | wx.ICON_ERROR)
			return
		    result = self.lib_manager.lookup_Reader(temp[0])
                    if not result == False:
                        wx.MessageBox('Invalid input or duplicate ID', 'Error', wx.OK | wx.ICON_ERROR)
			return
		    print temp
		    self.lib_manager.add_Reader(temp)
		    self.u4_edit = False
		    for i in range(7):
                        command = """self.u4_tc%d.SetValue("")""" % (i + 3)
                        exec(command)
			command = "self.u4_tc%d.Disable()" % (i + 3)
			exec(command)     
		else:
		    return
    def book_borrow_UI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        sizer = wx.GridBagSizer(1,7)
        u5_st = wx.StaticText(self, -1, label="借书处理")
        u5_st.SetForegroundColour('#3014D4')
        u5_st0 = wx.StaticText(self, -1, label="读者编号")
        self.u5_tc0 = wx.TextCtrl(self, -1, size=(120, 26))
        u5_st1 = wx.StaticText(self, -1, label="图书编号")
        self.u5_tc1 = wx.TextCtrl(self, -1, size=(120, 26))
        u5_bt0 = wx.Button(self, 601, label='借书处理')
        u5_bt1 = wx.Button(self, 602, label='清空信息')
        sizer.Add(u5_st, pos=(0,0), flag=wx.ALL, border=16)
        sizer.Add(u5_st0, pos=(0,1), flag=wx.ALL, border=16)
        sizer.Add(self.u5_tc0, pos=(0,2), flag=wx.ALL, border=13)
        sizer.Add(u5_st1, pos=(0,3), flag=wx.ALL, border=16)
        sizer.Add(self.u5_tc1, pos=(0,4), flag=wx.ALL, border=13)
        sizer.Add(u5_bt0, pos=(0,5), flag=wx.ALL, border=10)
        sizer.Add(u5_bt1, pos=(0,6), flag=wx.ALL, border=10)
        vbox.Add(sizer)
        line = wx.StaticLine(self)
        vbox.Add(line, proportion=0, flag=wx.ALL|wx.EXPAND, border=10)
        self.Bind(wx.EVT_BUTTON, self.bookborrow, u5_bt0)
        self.Bind(wx.EVT_BUTTON, self.bookborrow, u5_bt1)

        sizer2 = wx.GridBagSizer(12,5)
        u5_st2 = wx.StaticText(self, -1, label="读者已借阅图书")
        u5_st2.SetForegroundColour('#3014D4')
        u5_st3 = wx.StaticText(self, -1, label="ID")
        u5_st3.SetForegroundColour('#3014D4')
        u5_st4 = wx.StaticText(self, -1, label="Name                                    ")
        u5_st4.SetForegroundColour('#3014D4')
        u5_st5 = wx.StaticText(self, -1, label="Author                                  ")
        u5_st5.SetForegroundColour('#3014D4')
        u5_st6 = wx.StaticText(self, -1, label="Publisher                               ")
        u5_st6.SetForegroundColour('#3014D4')
        u5_st7 = wx.StaticText(self, -1, label="Type                                    ")
        u5_st7.SetForegroundColour('#3014D4')
        sizer2.Add(u5_st2, pos=(0,0), span=(1,1), flag=wx.ALL, border=1)
        sizer2.Add(u5_st3, pos=(1,0), flag=wx.ALL, border=1)
        sizer2.Add(u5_st4, pos=(1,1), flag=wx.ALL, border=1)
        sizer2.Add(u5_st5, pos=(1,2), flag=wx.ALL, border=1)
        sizer2.Add(u5_st6, pos=(1,3), flag=wx.ALL, border=1)
        sizer2.Add(u5_st7, pos=(1,4), flag=wx.ALL, border=1)
        for i in range(10):
            for j in range(5):
                command = "self.u5_%d_tc%d = wx.StaticText(self, -1, label='')" % (i,j)
                exec(command)
                command = "sizer2.Add(self.u5_%d_tc%d, pos=(%d,%d), flag=wx.ALL, border=1)" % (i,j,i+2,j)
                exec(command)
        vbox.Add(sizer2, proportion=0, flag=wx.ALL|wx.EXPAND, border=5)

        return vbox

    def bookborrow(self, e):
        if e.GetId() == 601:
            reader_id = self.u5_tc0.GetValue()
            book_id = self.u5_tc1.GetValue()
            if reader_id == "" or book_id == "":
                wx.MessageBox("Invalud input!", 'Error', wx.OK | wx.ICON_ERROR)
                return
            result = self.lib_manager.borrow_book(reader_id, book_id)
            if not result[0]:
                wx.MessageBox(result[1], 'Error', wx.OK | wx.ICON_ERROR)
                return
            else:
                wx.MessageBox("Borrow Success!", "Success!",wx.OK | wx.ICON_INFORMATION)
                temp = self.lib_manager.lookup_Record(reader_id)
                for i in range(len(temp)):
                    for j in range(5):
                        command = """self.u5_%d_tc%d.SetLabel("%s")""" % (i,j,temp[i][j])
                        exec(command)
        if e.GetId() == 602:    
            for i in range(2):
                command = "self.u5_tc%d.SetValue('')" % i
                exec(command)
            for i in range(10):
                for j in range(5):
                    command = "self.u5_%d_tc%d.SetLabel('')" % (i,j)
                    exec(command)

    def book_return_UI(self):
        pass
