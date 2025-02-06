import wx
import os

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Пример интерфейса с wxPython", size=(800, 600))

        # Создаем панель
        panel = wx.Panel(self)

        # Создаем верхнюю панель с кнопками и строкой информации
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.info_text = wx.StaticText(panel, label="Информация")
        top_sizer.Add(self.info_text, 0, wx.ALL | wx.CENTER, 5)

        button1 = wx.Button(panel, label="Кнопка 1")
        button2 = wx.Button(panel, label="Кнопка 2")
        top_sizer.Add(button1, 0, wx.ALL | wx.CENTER, 5)
        top_sizer.Add(button2, 0, wx.ALL | wx.CENTER, 5)

        # Создаем боковую панель для отображения файлов
        self.file_list = wx.ListBox(panel)
        self.load_files(".")

        # Центральная панель с пустыми квадратами
        center_sizer = wx.GridSizer(2, 2, 5, 5)
        self.squares = []
        for i in range(4):
            square = wx.Button(panel, label="")
            square.Bind(wx.EVT_BUTTON, self.on_square_click)
            center_sizer.Add(square, 0, wx.EXPAND)
            self.squares.append(square)

        # Правая панель с кнопками
        right_sizer = wx.BoxSizer(wx.VERTICAL)
        for i in range(5):
            button = wx.Button(panel, label=f"Кнопка {i + 3}")
            right_sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)

        # Основной sizer
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(top_sizer, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.file_list, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(center_sizer, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(right_sizer, 0, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(main_sizer)

        # Установка обработчиков событий
        button1.Bind(wx.EVT_BUTTON, self.on_button1_click)
        button2.Bind(wx.EVT_BUTTON, self.on_button2_click)

    def load_files(self, path):
        """Загружает файлы из указанной директории в список."""
        try:
            files = os.listdir(path)
            self.file_list.Clear()
            for file in files:
                self.file_list.Append(file)
            self.file_list.Bind(wx.EVT_LISTBOX_DCLICK, self.on_file_double_click)
        except Exception as e:
            print(f"Ошибка при загрузке файлов: {e}")

    def on_file_double_click(self, event):
        """Открывает файл при двойном клике."""
        selected_file = self.file_list.GetStringSelection()
        if selected_file:
            full_path = os.path.join(".", selected_file)  # Укажите путь к файлу
            os.startfile(full_path)  # Для Windows; для других ОС используйте другой метод

    def on_square_click(self, event):
        """Обрабатывает нажатие на квадрат."""
        button = event.GetEventObject()
        button.SetLabel("Нажато")

    def on_button1_click(self, event):
        """Обработчик для кнопки 1."""
        self.info_text.SetLabel("Кнопка 1 нажата")

    def on_button2_click(self, event):
        """Обработчик для кнопки 2."""
        self.info_text.SetLabel("Кнопка 2 нажата")


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
