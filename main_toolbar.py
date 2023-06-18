import wx

APP_CONNECTIONS = 1

class MainToolbar(wx.ToolBar):
    """Create tool bar."""
    def __init__(self, parent, *args, **kwargs):
        super(MainToolbar, self).__init__(parent, *args, **kwargs)

        # Connections
        iconHome = wx.ArtProvider.GetBitmap(wx.ART_GO_HOME)
        self.AddTool(APP_CONNECTIONS, 'Connections', wx.Bitmap(iconHome))
        self.Bind(wx.EVT_TOOL, parent.onConnections, id=APP_CONNECTIONS)

        # Quit 
        iconQuit =  wx.ArtProvider.GetBitmap(wx.ART_QUIT)
        self.AddTool(wx.ID_EXIT, 'Quit', wx.Bitmap(iconQuit))        
        self.SetToolShortHelp(wx.ID_EXIT, 'Quit')
        self.Bind(wx.EVT_TOOL, parent.onQuit, id=wx.ID_EXIT)

        self.Realize()