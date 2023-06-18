import wx

class MyFrame(wx.Frame):
  def __init__(self, parent, title):
    super(MyFrame, self).__init__(parent, title=title)
    self.panel = MyPanel(self)

class MyPanel(wx.Panel):
  def __init__(self, parent):
    super(MyPanel, self).__init__(parent)

    gridsizer = wx.GridSizer(4, 4, )

    for i in range(1, 17):
      btn = "Btn" + str(i)
      gridsizer.Add(wx.Button(self, label = btn), 0, wx.EXPAND)

    self.SetSizer(gridsizer)

class MyApp(wx.App):
  def OnInit(self):
    self.frame = MyFrame(parent=None, title="Main Window")
    self.frame.Show()
    return True

app = MyApp()
app.MainLoop()