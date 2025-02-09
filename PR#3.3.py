import wx
import os

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Пример интерфейса с wxPython")
        
        # Создаем панель
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Создаем верхнюю панель с кнопками и строкой информации
        top_panel = wx.Panel(panel)
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.info_text = wx.StaticText(top_panel, label="Выберите файл для открытия")
        open_button = wx.Button(top_panel, label="Открыть файл")
        refresh_button = wx.Button(top_panel, label="Обновить")

        top_sizer.Add(open_button, 0, wx.ALL | wx.CENTER, 5)
        top_sizer.Add(refresh_button, 0, wx.ALL | wx.CENTER, 5)
        top_sizer.Add(self.info_text, 1, wx.ALL | wx.EXPAND | wx.CENTER, 5)

        top_panel.SetSizer(top_sizer)

        # Создаем боковую панель для файлов
        self.file_listbox = wx.ListBox(panel)
        self.update_file_list(".")

        # Создаем центральные квадратные виджеты
        center_panel = wx.GridSizer(2, 2, 10, 10)
        self.squares = []
        for i in range(4):
            square = wx.Panel(panel, size=(100, 100), style=wx.SUNKEN_BORDER)
            square.Bind(wx.EVT_LEFT_UP, self.on_square_click)
            center_panel.Add(square, 0, wx.EXPAND)
            self.squares.append(square)

        # Создаем правую панель с кнопками
        right_panel = wx.Panel(panel)
        right_sizer = wx.BoxSizer(wx.VERTICAL)
        
        for i in range(5):
            button = wx.Button(right_panel, label=f"Кнопка {i + 1}")
            right_sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)

        right_panel.SetSizer(right_sizer)

        # Компоновка всех панелей
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.file_listbox, 0, wx.EXPAND | wx.ALL, 5)
        hbox.Add(center_panel, 1, wx.EXPAND | wx.ALL, 5)
        hbox.Add(right_panel, 0, wx.EXPAND | wx.ALL, 5)

        vbox.Add(top_panel, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox, 1, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(vbox)

        # Обработчики событий
        open_button.Bind(wx.EVT_BUTTON, self.on_open_file)
        refresh_button.Bind(wx.EVT_BUTTON, self.on_refresh)

    def update_file_list(self, path):
        """Обновляет список файлов в указанной директории."""
        self.file_listbox.Clear()
        try:
            files = os.listdir(path)
            for file in files:
                self.file_listbox.Append(file)
            self.file_listbox.SetSize((-1, self.file_listbox.GetBestSize()[1]))
        except Exception as e:
            print(f"Ошибка при чтении директории: {e}")

    def on_open_file(self, event):
        """Обработчик события открытия файла."""
        selection = self.file_listbox.GetSelection()
        if selection != -1:
            file_name = self.file_listbox.GetString(selection)
            file_path = os.path.join(".", file_name)  # Измените путь на нужный
            os.startfile(file_path)  # Открывает файл с помощью стандартного приложения

    def on_refresh(self, event):
        """Обновляет список файлов."""
        self.update_file_list(".")

    def on_square_click(self, event):
        """Обработчик события клика по квадратному виджету."""
        square = event.GetEventObject()
        square.SetBackgroundColour(wx.Colour(255, 255, 0))  # Изменяем цвет фона на желтый
        square.Refresh()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.SetSize((800, 600))
    frame.Show()
    app.MainLoop()
