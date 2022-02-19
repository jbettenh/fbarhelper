from fbarhelper import __version__
import fbarhelper.main as main


def test_version():
    assert __version__ == '0.1.0'


def test_menu_printer():
    test_menu = {
        1: 'Import',
        2: 'Balance',
        3: 'Show max',
        3: 'Exit',
    }
    main.print_menu(test_menu)
    assert True
