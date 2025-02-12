import wx
import os

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Пример интерфейса', size=(800, 600))

        # Основной панель
        panel = wx.Panel(self)

        # Верхняя панель с кнопками и строкой информации
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.info_text = wx.StaticText(panel, label="Информация")
        top_sizer.Add(self.info_text, 0, wx.ALL | wx.CENTER, 5)

        self.button1 = wx.Button(panel, label='Кнопка 1')
        self.button1.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_BUTTON))
        top_sizer.Add(self.button1, 0, wx.ALL | wx.CENTER, 5)

        self.button2 = wx.Button(panel, label='Кнопка 2')
        self.button2.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_QUIT, wx.ART_BUTTON))
        top_sizer.Add(self.button2, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(top_sizer)

        # Основной sizer
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Виджет для показа файлов
        self.file_list = wx.ListBox(panel)
        self.load_files('/path/to/your/folder')  # Укажите путь к папке
        main_sizer.Add(self.file_list, 1, wx.EXPAND | wx.ALL, 5)

        # Пустые квадратные виджеты
        square_sizer = wx.GridSizer(2, 2, 5, 5)
        for i in range(4):
            square = wx.Panel(panel, size=(100, 100))
            square.SetBackgroundColour(wx.Colour(200, 200, 200))
            square.Bind(wx.EVT_LEFT_DOWN, self.on_square_click)
            square_sizer.Add(square, 0, wx.EXPAND)

        main_sizer.Add(square_sizer, 1, wx.EXPAND | wx.ALL, 5)

        # Виджет с кнопками справа
        button_sizer = wx.BoxSizer(wx.VERTICAL)
        for i in range(5):
            button = wx.Button(panel, label=f'Кнопка {i+1}')
            button.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_ADD_BOOKMARK, wx.ART_BUTTON))
            button.Bind(wx.EVT_BUTTON, self.on_button_click)
            button_sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)

        main_sizer.Add(button_sizer, 0, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(main_sizer)

    def load_files(self, folder):
        """Загружает файлы из указанной папки в ListBox."""
        if os.path.exists(folder):
            files = os.listdir(folder)
            self.file_list.AppendItems(files)

    def on_square_click(self, event):
        """Обработчик клика по квадратному виджету."""
        square = event.GetEventObject()
        square.SetBackgroundColour(wx.Colour(150, 150, 150))
        square.Refresh()

    def on_button_click(self, event):
        """Обработчик клика по кнопкам справа."""
        button = event.GetEventObject()
        print(f'Нажата {button.GetLabel()}')

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
