import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # Создание панели Notebook
        self.notebook = wx.Notebook(self)

        # Создание панели для первой вкладки
        panel1 = wx.Panel(self.notebook)

        # Создание виджетов
        self.text_ctrl = wx.TextCtrl(panel1, value="Введите текст здесь", style=wx.TE_MULTILINE)
        self.checkbox = wx.CheckBox(panel1, label="Выберите меня")
        self.button = wx.Button(panel1, label="Нажми меня")

        # Привязка события к кнопке
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)

        # Установка sizer для панели
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.text_ctrl, 1, wx.EXPAND | wx.ALL, 10)
        vbox.Add(self.checkbox, 0, wx.ALL, 10)
        vbox.Add(self.button, 0, wx.ALL | wx.ALIGN_CENTER, 10)

        panel1.SetSizer(vbox)

        # Добавление панели во вкладки
        self.notebook.AddPage(panel1, "Вкладка 1")

        # Установка sizer для основного окна
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.notebook, 1, wx.EXPAND)
        self.SetSizer(main_sizer)

    def on_button_click(self, event):
        # Обработчик события для кнопки
        text = self.text_ctrl.GetValue()
        checkbox_value = self.checkbox.GetValue()
        message = f"Текст: {text}\nВыбран: {checkbox_value}"
        wx.MessageBox(message, "Информация", wx.OK | wx.ICON_INFORMATION)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title="Пример интерфейса с несколькими виджетами", size=(400, 300))
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
