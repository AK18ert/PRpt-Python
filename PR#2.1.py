import wx
import os

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Пример интерфейса с wxPython')
        self.panel = wx.Panel(self)

        # Создаем верхнюю панель с кнопками и строкой информации
        self.top_panel = wx.Panel(self.panel)
        self.top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.button1 = wx.Button(self.top_panel, label='Кнопка 1')
        self.button2 = wx.Button(self.top_panel, label='Кнопка 2')
        self.info_text = wx.StaticText(self.top_panel, label='Информация здесь')
        
        self.top_sizer.Add(self.button1, 0, wx.ALL, 5)
        self.top_sizer.Add(self.button2, 0, wx.ALL, 5)
        self.top_sizer.Add(self.info_text, 1, wx.ALL | wx.EXPAND, 5)
        
        self.top_panel.SetSizer(self.top_sizer)

        # Создаем боковую панель для показа файлов
        self.file_panel = wx.Panel(self.panel)
        self.file_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.file_list = wx.ListBox(self.file_panel)
        self.load_files_button = wx.Button(self.file_panel, label='Загрузить файлы')
        
        self.file_sizer.Add(self.file_list, 1, wx.ALL | wx.EXPAND, 5)
        self.file_sizer.Add(self.load_files_button, 0, wx.ALL | wx.CENTER, 5)
        
        self.file_panel.SetSizer(self.file_sizer)

        # Создаем центральную панель с пустыми квадратами
        self.center_panel = wx.Panel(self.panel)
        self.center_sizer = wx.GridSizer(2, 2, 5, 5)  # 2x2 сетка
        
        for _ in range(4):
            square_panel = wx.Panel(self.center_panel, size=(100, 100))
            square_panel.SetBackgroundColour(wx.Colour(200, 200, 200))  # Серый цвет
            self.center_sizer.Add(square_panel, 0, wx.EXPAND | wx.ALL)
        
        self.center_panel.SetSizer(self.center_sizer)

        # Создаем общий sizer для основной панели
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.top_panel, 0, wx.EXPAND)
        main_sizer.Add(wx.StaticLine(self.panel), 0, wx.EXPAND | wx.ALL, 5)
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.file_panel, 1, wx.EXPAND | wx.ALL, 5)
        hbox.Add(self.center_panel, 2, wx.EXPAND | wx.ALL, 5)
        
        main_sizer.Add(hbox, 1, wx.EXPAND)

        self.panel.SetSizer(main_sizer)

        # Обработчик для кнопки загрузки файлов
        self.load_files_button.Bind(wx.EVT_BUTTON, self.on_load_files)

    def on_load_files(self, event):
        # Путь к папке (можете изменить на свой)
        folder_path = '.'  # Текущая папка
        files = os.listdir(folder_path)
        self.file_list.Clear()
        for file in files:
            self.file_list.Append(file)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
