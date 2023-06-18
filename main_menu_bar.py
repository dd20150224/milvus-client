import wx

APP_EXIT = 1

class MainMenuBar(wx.MenuBar):
    """Create the menu bar."""
    def __init__(self, parent, *args, **kwargs):
        super(MainMenuBar, self).__init__(*args, **kwargs)

        # File menu
        fileMenu = wx.Menu()
        self.Append(fileMenu, '&File')
        # File - quit
        # quit_bmp =  wx.ArtProvider.GetBitmap(wx.ART_QUIT)
        # quit_menu_item = wx.MenuItem(file_menu, wx.ID_EXIT, )
        # parent.Bind(wx.EVT_MENU, parent.onQuit, id=wx.ID_EXIT)

        miExit = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
        miExit.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_QUIT))
        fileMenu.Append(miExit)
        parent.Bind(wx.EVT_MENU, parent.onQuit, miExit)
        #file_menu.Append(quit_menu_item)

