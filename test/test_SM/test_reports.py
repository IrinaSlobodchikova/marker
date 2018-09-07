from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def test_sm_create_contact_report_all_in_dif_row_tel_mail(app):
    username = app.username
    password = app.password
    smParticipants = app.smParticipants
    smreports = app.smreports
    app.session.ensure_login_sm(username, password)
    app.session.open_SM_page(smParticipants)
    app.testhelpersm.find_region2()
    #app.testhelpersm.check_results()
    app.testhelpersm.create_contact_report_all_in_dif_row_tel_mail()
    app.session.open_SM_page(smreports)
    #app.testhelpersm.report_is_present()
    #app.testhelpersm.status_is_changed()
    #app.testhelpersm.get_link()


