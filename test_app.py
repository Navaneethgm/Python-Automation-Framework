from lunch_zype import lauch_app
from button_isdisplayed import is_displayed

def test_lunch_app():
    result = lauch_app()
    assert result == True


def test_is_displayed():
    result = is_displayed()
    assert result == True