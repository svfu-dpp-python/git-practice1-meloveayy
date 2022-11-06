from unittest import TestCase
from main import button, entry, label, win


class TestPractice(TestCase):
    def test_buttons_master_is_win(self):
        self.assertIs(button.master, win)

    def test_entrys_master_is_win(self):
        self.assertIs(entry.master, win)

    def test_labels_master_is_win(self):
        self.assertIs(label.master, win)
