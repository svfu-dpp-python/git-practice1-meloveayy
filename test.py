from tkinter import Widget
from unittest import TestCase

from main import button, label, win


def get_text(widget: Widget):
    config = widget.config()
    return config['text'][4]


class TestPractice(TestCase):

    def test_win_title(self):
        self.assertEqual(win.title(), "Учебный пример")

    def test_label_text(self):
        self.assertEqual(get_text(label), "Привет!")

    def test_button_text(self):
        self.assertEqual(get_text(button), "Нажми меня")
