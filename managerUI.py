#! /usr/bin/python
# coding: utf-8

import wx
from submanagerUI import submanagerUI

class managerUI(wx.Frame):
    def __init__(self, connection, parent=None, id=-1, title='Library'):
        wx.Frame.__init__(self, parent, id, title)

        self.connection=connection
        self.InitUI()
        self.SetSize((845,550))
        self.Centre()
        self.Show(True)
        self.SetTitle(title)

    def InitUI(self):
        menubar = wx.MenuBar()
        helpmenu = wx.Menu()
        helpmenu.Append(100, '&About')
        self.Bind(wx.EVT_MENU, self.OnAboutBox, id=100)
        menubar.Append(helpmenu, '&Help')
        self.SetMenuBar(menubar)

        self.panel = wx.Panel(self)
        self.upPanel = wx.Panel(self.panel, -1)
        self.downPanel = wx.Panel(self.panel, -1)
        self.subUI1 = submanagerUI(self.downPanel, -1, 1, self.connection)
        self.subUI2 = submanagerUI(self.downPanel, -1, 2, self.connection)
        self.subUI3 = submanagerUI(self.downPanel, -1, 3, self.connection)
        self.subUI4 = submanagerUI(self.downPanel, -1, 4, self.connection)
        self.subUI5 = submanagerUI(self.downPanel, -1, 5, self.connection)
        self.subUI6 = submanagerUI(self.downPanel, -1, 6, self.connection)
        vbox = wx.BoxSizer(wx.VERTICAL)

        sizer = wx.GridBagSizer(2, 7)
        bt1 = wx.Button(self.upPanel, 1, label='图书查询')
        bt2 = wx.Button(self.upPanel, 2, label='读者查询')
        bt3 = wx.Button(self.upPanel, 3, label='图书管理')
        bt4 = wx.Button(self.upPanel, 4, label='读者管理')
        bt5 = wx.Button(self.upPanel, 5, label='借书处理')
        bt6 = wx.Button(self.upPanel, 6, label='还书处理')
        bt7 = wx.Button(self.upPanel, 7, label='退出系统')
        sizer.Add(bt1, pos=(0, 0), flag=wx.ALL, border=15)
        sizer.Add(bt2, pos=(0, 1), flag=wx.ALL, border=15)
        sizer.Add(bt3, pos=(0, 2), flag=wx.ALL, border=15)
        sizer.Add(bt4, pos=(0, 3), flag=wx.ALL, border=15)
        sizer.Add(bt5, pos=(0, 4), flag=wx.ALL, border=15)
        sizer.Add(bt6, pos=(0, 5), flag=wx.ALL, border=15)
        sizer.Add(bt7, pos=(0, 6), flag=wx.ALL, border=15)
        line = wx.StaticLine(self.upPanel)
        sizer.Add(line, pos=(1, 0), span=(1, 7), flag=wx.EXPAND|wx.BOTTOM, border=10)
        self.upPanel.SetSizer(sizer)

        vbox.Add(self.upPanel, 0, wx.EXPAND | wx.RIGHT, 5)
        vbox.Add(self.downPanel, 1, wx.EXPAND)
        self.panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.ButtonEvent, bt1)
        self.Bind(wx.EVT_BUTTON, self.ButtonEvent, bt2)
        self.Bind(wx.EVT_BUTTON, self.ButtonEvent, bt3)
        self.Bind(wx.EVT_BUTTON, self.ButtonEvent, bt4)
        self.Bind(wx.EVT_BUTTON, self.ButtonEvent, bt5)
        self.Bind(wx.EVT_BUTTON, self.ButtonEvent, bt6)
        self.Bind(wx.EVT_BUTTON, self.ButtonEvent, bt7)
        self.Bind(wx.EVT_CLOSE, self.quit)

    def quit(self, e):
	self.Destroy()

    def ButtonEvent(self, e):
        panelid = e.GetId()
        for i in range(1,7):
            if not i == panelid:
                string = "self.subUI%d.Hide()" % i
                exec(string)
            else:
                string = "self.subUI%d.Show(True)" % i
                exec(string)

    def OnAboutBox(self, e):
        description = """a simple library manager system"""
        info = wx.AboutDialogInfo()

        info.SetIcon(wx.Icon('icon.png', wx.BITMAP_TYPE_PNG))
        info.SetName('Library System')
        info.SetVersion('1.0')
        info.SetDescription(description)
        info.SetCopyright('(c) 2012 Xiaohui Huang')
        #info.SetWebsite('')
        #info.SetLicence('')
        info.AddDeveloper('Xiaohui Huang')
        info.AddDocWriter('Xiaohui Huang')
        #info.AddArtist('')
        #info.AddTranslator('')

        wx.AboutBox(info)

if __name__ == '__main__':
    app = wx.App(redirect=False)
    managerUI(None, -1, 'Library')
    app.MainLoop()
