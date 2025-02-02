import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # Создание панели Notebook
        self.notebook = wx.Notebook(self)

        # Создание первой вкладки
        panel1 = wx.Panel(self.notebook)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        text1 = wx.TextCtrl(panel1, value="Это первая вкладка", style=wx.TE_MULTILINE)
        vbox1.Add(text1, 1, wx.EXPAND | wx.ALL, 10)
        panel1.SetSizer(vbox1)
        
        # Создание второй вкладки
        panel2 = wx.Panel(self.notebook)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        text2 = wx.TextCtrl(panel2, value="Это вторая вкладка", style=wx.TE_MULTILINE)
        vbox2.Add(text2, 1, wx.EXPAND | wx.ALL, 10)
        panel2.SetSizer(vbox2)

        # Создание третьей вкладки
        panel3 = wx.Panel(self.notebook)
        vbox3 = wx.BoxSizer(wx.VERTICAL)
        text3 = wx.TextCtrl(panel3, value="Это третья вкладка", style=wx.TE_MULTILINE)
        vbox3.Add(text3, 1, wx.EXPAND | wx.ALL, 10)
        panel3.SetSizer(vbox3)

        # Добавление панелей во вкладки
        self.notebook.AddPage(panel1, "Вкладка 1")
        self.notebook.AddPage(panel2, "Вкладка 2")
        self.notebook.AddPage(panel3, "Вкладка 3")

        # Установка sizer для основного окна
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.notebook, 1, wx.EXPAND)
        self.SetSizer(main_sizer)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title="Пример с несколькими окнами во вкладках", size=(400, 300))
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
