#! /usr/bin/python
# coding: utf-8

import wx
from library import library
from managerUI import managerUI

class LoginUI(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        self.InitUI()
        self.SetSize((200,157))
        self.SetMaxSize((200,157))
        self.SetMinSize((200,157))
        self.Centre()
        self.Show(True)

    def InitUI(self):
	menubar = wx.MenuBar()
        helpmenu = wx.Menu()
        helpmenu.Append(100, '&About')
        self.Bind(wx.EVT_MENU, self.OnAboutBox, id=100)
        menubar.Append(helpmenu, '&Help')
        self.SetMenuBar(menubar)

        panel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(4,2,5,10)

        self.st0 = wx.StaticText(panel, label='Identity')
        self.cb = wx.ComboBox(panel, -1, size=(90,26), choices=['student','manager'], value='manager')
        self.st1 = wx.StaticText(panel,label='ID')
        self.st2 = wx.StaticText(panel,label='Password')
        self.tc1 = wx.TextCtrl(panel, -1, '1001')
        self.tc2 = wx.TextCtrl(panel, -1, 'managerone',style = wx.TE_PASSWORD)
        self.bt1 = wx.Button(panel,-1,label='login')
        self.bt2 = wx.Button(panel,-1,label='quit')

        fgs.Add(self.st0, flag=wx.TOP, border=5)
        fgs.Add(self.cb)
        fgs.Add(self.st1,flag=wx.TOP,border=5)
        fgs.Add(self.tc1)
        fgs.Add(self.st2,flag=wx.TOP,border=5)
        fgs.AddMany([(self.tc2),(self.bt1),(self.bt2)])
        hbox.Add(fgs, proportion=0, flag=wx.EXPAND|wx.ALL, border=10)

        self.Bind(wx.EVT_BUTTON, self.login, self.bt1)
        self.Bind(wx.EVT_BUTTON, self.quit, self.bt2)

        panel.SetSizer(hbox)

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

    def login(self,e):
        identity = self.cb.GetValue()
        userid = self.tc1.GetValue()
        passd = self.tc2.GetValue()
        result = library.login_in(identity, userid, passd)
        if result:
            self.managerUI = managerUI(connection=result, parent=None, id=-1)
	    self.Show(False)
	    self.managerUI.Show(True)
	    self.Close()
        else:
            wx.MessageBox('Invalid ID or Wrong Password!', 'Error', wx.OK | wx.ICON_ERROR)
        

    def quit(self,e):
        self.Close()

def main():        
    app = wx.App()
    LoginUI(None, -1, 'Library')
    app.MainLoop()

if __name__ == '__main__':
    main()
