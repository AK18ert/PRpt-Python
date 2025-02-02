import wx
import os

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # Основной панельный sizer
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Панель для отображения информации
        self.info_panel = wx.Panel(self)
        self.info_text = wx.StaticText(self.info_panel, label="Выберите папку для отображения файлов")
        info_sizer = wx.BoxSizer(wx.HORIZONTAL)
        info_sizer.Add(self.info_text, 0, wx.ALL | wx.CENTER, 10)
        self.info_panel.SetSizer(info_sizer)

        # Панель для кнопок
        self.button_panel = wx.Panel(self)
        button_sizer = wx.BoxSizer(wx.VERTICAL)

        # Кнопки
        self.button1 = wx.Button(self.button_panel, label="Кнопка 1")
        self.button2 = wx.Button(self.button_panel, label="Кнопка 2")
        self.button3 = wx.Button(self.button_panel, label="Кнопка 3")
        
        # Привязка события к кнопкам
        self.button1.Bind(wx.EVT_BUTTON, self.on_button_click)
        self.button2.Bind(wx.EVT_BUTTON, self.on_button_click)
        self.button3.Bind(wx.EVT_BUTTON, self.on_button_click)

        # Добавление кнопок в sizer
        button_sizer.Add(self.button1, 0, wx.ALL | wx.EXPAND, 5)
        button_sizer.Add(self.button2, 0, wx.ALL | wx.EXPAND, 5)
        button_sizer.Add(self.button3, 0, wx.ALL | wx.EXPAND, 5)

        self.button_panel.SetSizer(button_sizer)

        # Панель для отображения файлов
        self.file_panel = wx.Panel(self)
        self.file_list = wx.ListBox(self.file_panel)
        
        # Установка sizer для панели файлов
        file_sizer = wx.BoxSizer(wx.VERTICAL)
        file_sizer.Add(self.file_list, 1, wx.EXPAND | wx.ALL, 10)
        self.file_panel.SetSizer(file_sizer)

        # Добавление всех панелей в основной sizer
        main_sizer.Add(self.info_panel, 0, wx.EXPAND)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.button_panel, 0, wx.EXPAND | wx.ALL, 10)
        hbox.Add(self.file_panel, 1, wx.EXPAND | wx.ALL, 10)
        
        main_sizer.Add(hbox, 1, wx.EXPAND)

        self.SetSizer(main_sizer)

    def on_button_click(self, event):
        # Обработчик нажатия кнопки
        button = event.GetEventObject()
        button_label = button.GetLabel()
        
        # Задайте путь к папке (замените на свою папку)
        folder_path = "C:/Users/User/Desktop"  # Укажите путь к вашей папке
        
        if button_label == "Кнопка 1":
            self.load_files(folder_path)

    def load_files(self, folder_path):
        # Загрузка файлов из указанной папки
        if os.path.exists(folder_path):
            files = os.listdir(folder_path)
            self.file_list.Clear()  # Очистка списка перед загрузкой новых файлов
            for file in files:
                self.file_list.Append(file)  # Добавление файла в список
            self.info_text.SetLabel(f"Файлы в папке: {folder_path}")
        else:
            wx.MessageBox("Указанная папка не существует.", "Ошибка", wx.OK | wx.ICON_ERROR)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title="Интерфейс", size=(600, 400))
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
