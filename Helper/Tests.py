from Helper import *
import pytest
from Order import *
from datetime import datetime
import mock


# Tests with pytest

# Helper.py - main file
def test_cmd_generator_kick():
    # given
    parms = ["Kolejarz123", "Trolling"]
    choice = "2"
    # when
    result = cmd_generator(parms, choice)
    # then
    assert result == "/kick_driver Kolejarz123 Trolling"


def test_cmd_generator_sklad():
    # given
    parms = ["im_", "m2", "5", "10", "test"]
    choice = "1"
    # when
    result = cmd_generator(parms, choice)
    # then
    assert result == "/sp Im_M2:5 n:10,test"


def test_menu():
    with mock.patch("builtins.input", return_value="1"):
        assert menu() == "1"


def test_get_parms_helper():
    with mock.patch("builtins.input", return_value="answer"):
        assert get_params("Test", 1) == "answer"


class TestFile_Test:
    def test_init(self):
        test = File_test("test_helper.txt")
        assert isinstance(test, File_test)
        assert test.file_name == "test_helper.txt"

    def test_file_exist(self):
        test = File_test("test_helper.txt")
        assert test.file_exist() != False

    def test_display_list(self):
        test = File_test("test_helper.txt")
        assert test.display_list() == (
        [['Test1', 'przyklad', 'przykladowe', 'przyklady', 'test33'], ['Test2', 'Witam', 'Pozdrawiam']],
        [['przyklad', 'przykladowe > Siema', 'przyklady', 'test33'], ['Witam', 'Pozdrawiam']])

    def test_pick_object(self):
        test = File_test("test_helper.txt")
        # dla 0.0
        with mock.patch("builtins.input", return_value="0.0"):
            assert test.pick_object() == "przyklad"

        with mock.patch("builtins.input", return_value="0.10"):
            assert test.pick_object() == False

        with mock.patch("builtins.input", return_value="Łoś"):
            assert test.pick_object() == False

