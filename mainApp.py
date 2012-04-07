# -*- coding:UTF-8 -*- 
#!/user/bin/env python

import wx
from LoginUI import LoginUI
         
class App(wx.App):
    def OnInit(self):
        self.loginframe = LoginUI(None,-1,'Library')
        self.loginframe.Show()
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()
