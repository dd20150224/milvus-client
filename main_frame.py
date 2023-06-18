import wx

from main_menu_bar import MainMenuBar
from main_toolbar import MainToolbar
from main_status_bar import MainStatusBar

class MainFrame(wx.Frame):
  def __init__(self, title):
    super(MainFrame, self).__init__(None)
    self.Title = title
    self.Size = (800, 600)
    self.SetMenuBar(MainMenuBar(self))
    self.ToolBar = MainToolbar(self)
    self.status_bar = MainStatusBar(self).status_bar
    self.Center()
    self.Show()

  def onQuit(self, event):
    del event
    wx.CallAfter(self.Destroy)

  def onConnections(self, event):
    del event
    print("onConnections")
    