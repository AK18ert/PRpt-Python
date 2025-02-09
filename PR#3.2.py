import wx
import os

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Пример интерфейса с wxPython", size=(800, 600))
        
        # Создаем панель
        panel = wx.Panel(self)

        # Создаем верхнюю панель с кнопками и строкой информации
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.info_text = wx.StaticText(panel, label="Информация здесь")
        top_sizer.Add(self.info_text, 0, wx.ALL | wx.CENTER, 10)

        open_button = wx.Button(panel, label="Открыть")
        open_button.Bind(wx.EVT_BUTTON, self.on_open)
        top_sizer.Add(open_button, 0, wx.ALL | wx.CENTER, 5)

        refresh_button = wx.Button(panel, label="Обновить")
        refresh_button.Bind(wx.EVT_BUTTON, self.on_refresh)
        top_sizer.Add(refresh_button, 0, wx.ALL | wx.CENTER, 5)

        # Создаем sizer для основной панели
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Создаем виджет для показа файлов
        self.file_list = wx.ListBox(panel)
        self.load_files()  # Загружаем файлы из указанной директории
        self.file_list.Bind(wx.EVT_LISTBOX, self.on_file_select)
        
        main_sizer.Add(self.file_list, 1, wx.EXPAND | wx.ALL, 5)

        # Создаем пустые квадратные виджеты в центре
        center_grid = wx.GridSizer(2, 2, 10, 10)
        self.squares = []
        for _ in range(4):
            square = wx.Button(panel, label="")
            square.Bind(wx.EVT_BUTTON, self.on_square_click)
            center_grid.Add(square, 0, wx.EXPAND | wx.ALL, 5)

        main_sizer.Add(center_grid, 1, wx.EXPAND | wx.ALL, 5)

        # Создаем правую панель с кнопками
        right_panel = wx.Panel(panel)
        right_sizer = wx.BoxSizer(wx.VERTICAL)

        for i in range(5):
            button = wx.Button(right_panel, label=f"Кнопка {i + 1}")
            right_sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)

        right_panel.SetSizer(right_sizer)
        main_sizer.Add(right_panel, 0, wx.ALL | wx.CENTER, 5)

        # Объединяем все sizer'ы
        panel.SetSizer(wx.BoxSizer(wx.VERTICAL))
        panel.GetSizer().Add(top_sizer, 0, wx.EXPAND | wx.ALL, 5)
        panel.GetSizer().Add(main_sizer, 1, wx.EXPAND | wx.ALL, 5)

    def load_files(self):
        # Загружаем файлы из указанной директории (измените на нужную вам)
        directory = '.'  # Укажите нужную папку
        self.file_list.Clear()
        try:
            files = os.listdir(directory)
            for file in files:
                if os.path.isfile(os.path.join(directory, file)):
                    self.file_list.Append(file)
        except Exception as e:
            self.info_text.SetLabel(f"Ошибка: {str(e)}")

    def on_file_select(self, event):
        selected_file = self.file_list.GetStringSelection()
        self.info_text.SetLabel(f"Выбран файл: {selected_file}")

    def on_square_click(self, event):
        """Обрабатывает нажатие на квадрат."""
        button = event.GetEventObject()
        button.SetLabel("Нажато")

    def on_open(self, event):
        selected_file = self.file_list.GetStringSelection()
        if selected_file:
            try:
                os.startfile(selected_file)  # Открываем файл в соответствующем приложении
            except Exception as e:
                self.info_text.SetLabel(f"Не удалось открыть файл: {str(e)}")

    def on_refresh(self, event):
        self.load_files()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
