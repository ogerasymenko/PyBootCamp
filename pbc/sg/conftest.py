import pytest
from pbc.sg.selenium import Grid


@pytest.fixture(scope="session")
def selenium_precondition():
    grid = Grid()
    grid.download()
    grid.start_hub()
    grid.add_node()
    assert len(grid.send_command('pgrep java')) == 2
    yield grid.client
    grid.send_command('killall java')
    grid.close()