import wx

from copy_items import copy_items


class MyFrame(wx.Frame):
    def detect_text_entry(self, event):
        if event:
            self.my_btn.Enable()

    def on_clicked(self, event):
        from_val = self.text_ctrl_from.GetValue()
        to_val = self.text_ctrl_to.GetValue()
        copy_items(from_val, to_val)

    def __init__(self):
        super().__init__(parent=None, title='Bilder kopieren')
        panel = wx.Panel(self)

        self.text_ctrl_from = wx.TextCtrl(panel, pos=(10, 55))
        self.text_ctrl_from.SetHint('Von')
        self.text_ctrl_from.Bind(wx.EVT_TEXT, self.detect_text_entry)

        self.text_ctrl_to = wx.TextCtrl(panel, pos=(10, 105))
        self.text_ctrl_to.SetHint('Nach')
        self.text_ctrl_to.Bind(wx.EVT_TEXT, self.detect_text_entry)

        my_sizer = wx.BoxSizer(wx.VERTICAL)
        my_sizer.Add(self.text_ctrl_from, 0, wx.ALL | wx.EXPAND, 5)
        my_sizer.Add(self.text_ctrl_to, 0, wx.ALL | wx.EXPAND, 5)
        panel.SetSizer(my_sizer)

        self.my_btn = wx.Button(panel, label='Kopieren', pos=(10, 135))
        self.my_btn.Disable()

        self.my_btn.Bind(wx.EVT_BUTTON, self.on_clicked)

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
