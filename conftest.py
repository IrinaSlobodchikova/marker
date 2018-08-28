import pytest
from fixture.application import Application
import json
import os.path


fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['dev_marker']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture

#@pytest.fixture(scope = "session", autouse=True)
#def db(request):
#    db_config = load_config(request.config.getoption("--target"))['db']
#    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'], check_ui=db_config['check_ui'])
#    def fin():
#        dbfixture.destroy()
#    request.addfinalizer(fin)
#    return dbfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


#@pytest.fixture
#def check_ui(request):
 #   return request.config.getoption("--check_ui")




def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    #parser.addoption("--check_ui", action="store_true")

