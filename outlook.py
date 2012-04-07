#! /usr/bin/python
# -*- coding: utf-8 -*-
# @author:  huangxiaohui
# @version: V1.0
# @time:    2012-

import wx
import library

class outlook(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(outlook, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        helpmenu = wx.Menu()
        helpmenu.Append(100, '&About')
        self.Bind(wx.EVT_MENU, self.OnAboutBox, id=100)
        menubar.Append(helpmenu, '&Help')
        self.SetMenuBar(menubar)

        self.SetSize((300,200))
        self.SetTitle('library')
        self.Centre()
        self.Show(True)

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

def main():

    ex = wx.App()
    outlook(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()
