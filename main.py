# -*- coding: utf-8 -*-
# ref: https://zero-cheese.com/6986/

import wx
import sys,os

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # express by bit
        bitmap = wx.Image('gazou.png').ConvertToBitmap()
        # position image control
        self.image = wx.StaticBitmap(parent=self,
                                     bitmap=bitmap,
                                     size=bitmap.GetSize()
                                     )
        self.image.SetBackgroundColour('white')
        button = wx.Button(self, -1, 'Open_File')

        box_sizer = wx.BoxSizer(wx.VERTICAL)
        box_sizer.Add(self.image, 1, wx.EXPAND)
        box_sizer.Add(button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.SetSizer(box_sizer)

        button.Bind(wx.EVT_BUTTON, self.OnBrowse)

    def OnBrowse(self, event):
        with wx.FileDialog(self, 'Select Image File',
                           wildcard='PNG files (*.png)|*.png',
                           style=wx.FD_OPEN) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                bitmap = wx.Image(dialog.GetPaths()[0]).ConvertToBitmap()
                self.image.SetBitmap(bitmap)
                self.Layout()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, id=-1, title="wxPython")
        panel = MyPanel(self)
        self.Show()

    # def create_status_bar(self):
    #     sb = self.CreateStatusBar(number = 4)
    #     sb.SetStatusWidths([-1, -1, -1, -1]) # set as ratio
    #     sb.SetStatusText('H', 0)
    #     sb.SetStatusText('E', 1)
    #     sb.SetStatusText('LL', 2)
    #     sb.SetStatusText('O', 3)
    #
    # def create_menu_bar(self):
    #     # make menu of "file"
    #     f_menu = wx.Menu()
    #     f_menu.Append(-1, 'new', 'make new file')
    #     f_menu.Append(-1, 'save')
    #     exit = f_menu.Append(-1, 'exit')

        # s_menu = wx.Menu()
        # s_menu.Append(-1, 'change the size')
        # s_menu.Append(-1, 'gray image')
        #
        # m_bar = wx.MenuBar()
        # m_bar.Append(f_menu, 'file')
        # m_bar.Append(s_menu, 'edit')
        # self.SetMenuBar(m_bar)
        #
        # self.Bind(wx.EVT_MENU, self.OnExit, exit)

    def OnExit(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()