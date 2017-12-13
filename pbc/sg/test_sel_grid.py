import requests
import time
from pbc.sg.selenium import Grid


def test_sel_grid(selenium_precondition):
    grid = Grid()
    result = None
    counter = 0
    while counter < 10 and result != 5:
        response = requests.get('http://192.168.33.10:4444/grid/console')
        data = str(response.text)
        result = data.count('/grid/resources/org/openqa/grid/images/firefox.png')
        counter += 1
        response.close
        time.sleep(1)
    assert data.count('/grid/resources/org/openqa/grid/images/firefox.png') == 5
