#! /usr/bin/python
# coding: utf-8

import wx

class managerUI(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        self.InitUI()
        self.SetSize((850,650))
        self.Centre()
        self.Show(True)
        self.SetTitle(title)

    def InitUI(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        sizer = wx.GridBagSizer(2, 7)
        bt1 = wx.Button(panel, -1, label='图书查询')
        bt2 = wx.Button(panel, -1, label='读者查询')
        bt3 = wx.Button(panel, -1, label='图书管理')
        bt4 = wx.Button(panel, -1, label='读者管理')
        bt5 = wx.Button(panel, -1, label='借书处理')
        bt6 = wx.Button(panel, -1, label='还书处理')
        bt7 = wx.Button(panel, -1, label='退出系统')
        sizer.Add(bt1, pos=(0, 0), flag=wx.ALL, border=15)
        sizer.Add(bt2, pos=(0, 1), flag=wx.ALL,border=15)
        sizer.Add(bt3, pos=(0, 2), flag=wx.ALL, border=15)
        sizer.Add(bt4, pos=(0, 3), flag=wx.ALL, border=15)
        sizer.Add(bt5, pos=(0, 4), flag=wx.ALL, border=15)
        sizer.Add(bt6, pos=(0, 5), flag=wx.ALL, border=15)
        sizer.Add(bt7, pos=(0, 6), flag=wx.ALL, border=15)
        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 7), flag=wx.EXPAND|wx.BOTTOM, border=10)
        vbox.Add(sizer)

        panel.SetSizer(vbox)

if __name__ == '__main__':
    app = wx.App(redirect=False)
    managerUI(None, -1, 'Library')
    app.MainLoop()
