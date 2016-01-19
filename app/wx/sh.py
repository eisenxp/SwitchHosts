# -*- coding: utf-8 -*-
#
# author: oldj
# blog: http://oldj.net
#

import wx, wx.html2, os, _winreg


class MyBrowser(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, None, -1, "SwitchHosts!", size=(300, 300))
        # 这里需要打开所有权限
        self.key = _winreg.OpenKey(
                _winreg.HKEY_CURRENT_USER,
                r"SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BROWSER_EMULATION",
                0,
                _winreg.KEY_ALL_ACCESS
        )
        try:
            # 设置注册表 sh.exe 值为 11000(IE11)
            _winreg.SetValueEx(self.key, 'sh.exe', 0, _winreg.REG_DWORD, 0x00002af8)
        except:
            # 设置出现错误
            print('error in set value!')
        self.browser = wx.html2.WebView.New(self, style=0)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, evt):
        print('close')
        # 用完取消注册表设置
        _winreg.DeleteValue(self.key, 'sh.exe')
        # 关闭打开的注册表
        _winreg.CloseKey(self.key)
        evt.Skip()


if __name__ == '__main__':
    app = wx.App()
    frame = MyBrowser()
    # frame.browser.LoadURL(os.path.realpath("main.html"))
    frame.browser.LoadURL("http://vuejs.org/examples/")
    frame.Show()
    app.MainLoop()
