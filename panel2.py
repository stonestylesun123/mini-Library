#!/usr/bin/python
# coding: utf-8
# repository.py

import wx
import sys
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin

class Repository(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(450, 400))

        panel = wx.Panel(self, -1)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.VERTICAL)

        panel1 = wx.Panel(panel, -1)
        rightPanel = wx.Panel(panel, -1)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        bt1 = wx.Button(panel1, -1, label='图书查询')
        bt2 = wx.Button(panel1, -1, label='读者查询')
        bt3 = wx.Button(panel1, -1, label='图书管理')
        bt4 = wx.Button(panel1, -1, label='读者管理')
        bt5 = wx.Button(panel1, -1, label='借书处理')
        bt6 = wx.Button(panel1, -1, label='还书处理')
        bt7 = wx.Button(panel1, -1, label='退出系统')
        sizer.Add(bt1, flag=wx.ALL, border=5)
        sizer.Add(bt2, flag=wx.ALL, border=5)
        sizer.Add(bt3, flag=wx.ALL, border=5)
        sizer.Add(bt4, flag=wx.ALL, border=5)
        sizer.Add(bt5, flag=wx.ALL, border=5)
        sizer.Add(bt6, flag=wx.ALL, border=5)
        sizer.Add(bt7, flag=wx.ALL, border=5)
        #line = wx.StaticLine(panel)
        #sizer.Add(line, pos=(1, 0), span=(1, 7), flag=wx.EXPAND|wx.BOTTOM, border=10)

        panel1.SetSizer(sizer)
	#vbox.Add(Button, panel)
        rightPanel.SetSizer(vbox)

        hbox.Add(panel1, 0, wx.EXPAND | wx.RIGHT, 5)
        hbox.Add(rightPanel, 1, wx.EXPAND)
        hbox.Add((3, -1))

        panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)

app = wx.App()
Repository(None, -1, 'Repository')
app.MainLoop()
