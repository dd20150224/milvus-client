import wx
from main_frame import MainFrame

class MyApp(wx.App):
  def OnInit(self):
    self.frame = MainFrame("Milvus Client")
    self.frame.Show()

    return True

app = MyApp()
app.MainLoop()
