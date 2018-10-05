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


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    environment = request.config.getoption("--environment")
    #check_report_result = request.config.getoption("--check_report_result")
    #web_config = load_config(request.config.getoption("--target"))['dev_marker']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, config=config, environment=environment,
                              check_report_result=config[environment]['check_report_result'],
                              baseUrlSM=config[environment]['baseUrlSM'],
                              baseUrlMarker=config[environment]['baseUrlMarker'],
                              username=config[environment]['username'],
                              password=config[environment]['password'],
                              dashboard=config['markertails']['dashboard'],
                              newtenders=config['markertails']['newtenders'],
                              participation=config['markertails']['participation'],
                              watch=config['markertails']['watch'],
                              market_potential=config['markertails']['market-potential'],
                              planned_purchases=config['markertails']['planned-purchases'],
                              company_list=config['markertails']['company_list'],
                              solutions=config['markertails']['solutions'],
                              reports=config['markertails']['reports'],
                              smParticipants=config['SMtails']['Participants'],
                              smParticipantsCustomers=config['SMtails']['ParticipantsCustomers'],
                              smParticipantsSuppliers=config['SMtails']['ParticipantsSuppliers'],
                              smPurchases=config['SMtails']['Purchases'],
                              smPrices=config['SMtails']['Prices'],
                              smCertificates=config['SMtails']['Certificates'],
                              smLicences=config['SMtails']['Licences'],
                              smKontrol=config['SMtails']['Kontrol'],
                              smreports=config['SMtails']['reports'],
                              smMonitorinds=config['SMtails']['Monitorinds'],
                              smcompany_list=config['SMtails']['company_list'],
                              smPurchases_list=config['SMtails']['Purchases_list'],
                              smNmckList=config['SMtails']['NmckList'],
                              smUser_History=config['SMtails']['User_History'],
                              smlogout=config['SMtails']['logout'],
                              smAdminUserInfo=config['AdminSMtails']['UserInfo'],
                              smAdminUpravlenie=config['AdminSMtails']['Upravlenie'],
                              smAdminShlyuz=config['AdminSMtails']['Shlyuz'],
                              smAdminAccessManager=config['AdminSMtails']['AccessManager'],
                              smAdminInstructions=config['AdminSMtails']['Instructions'],
                              smAdminNotifications=config['AdminSMtails']['Notifications'],
                              smAdminNews=config['AdminSMtails']['News'],
                              smAdminSessions=config['AdminSMtails']['Sessions'],
                              admindashboard=config['AdminMarkertails']['dashboard'],
                              adminfind_monitorings=config['AdminMarkertails']['find_monitorings'],
                              adminfind_users=config['AdminMarkertails']['find_users'],
                              adminfind_publication=config['AdminMarkertails']['find_publication'],
                              adminnews=config['AdminMarkertails']['news']
        )
    #fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture


# @pytest.fixture(scope = "session", autouse=True)
# def db(request):
#    db_config = load_config(request.config.getoption("--target"))['db']
#    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'], check_ui=db_config['check_ui'])
#    def fin():
#        dbfixture.destroy()
#    request.addfinalizer(fin)
#    return dbfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        if not fixture.session.is_marker:
            fixture.session.ensure_Marker_logout()
        else:
            fixture.session.ensure_logout_sm()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


# @pytest.fixture
# def check_ui(request):
#   return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--environment", action="store", default="dev")
    #parser.addoption("--check_report_result", action="store", default="True")
    #parser.addoption("--check_ui", action="store_true")
