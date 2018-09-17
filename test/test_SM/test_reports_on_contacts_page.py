


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


def test_sm_create_contact_report_allinone_tel_mail(app):
    username = app.username
    password = app.password
    smParticipants = app.smParticipants
    smreports = app.smreports
    app.session.ensure_login_sm(username, password)
    app.session.open_SM_page(smParticipants)
    app.testhelpersm.find_region2()
    #app.testhelpersm.check_results()
    app.testhelpersm.create_contact_report_allinone_tel_mail()
    app.session.open_SM_page(smreports)
    #app.testhelpersm.report_is_present()
    #app.testhelpersm.status_is_changed()
    #app.testhelpersm.get_link()


def test_sm_create_contact_report_result(app):
    username = app.username
    password = app.password
    smParticipants = app.smParticipants
    smreports = app.smreports
    app.session.ensure_login_sm(username, password)
    app.session.open_SM_page(smParticipants)
    app.testhelpersm.find_region2()
    #app.testhelpersm.check_results()
    app.testhelpersm.create_contact_report_result()
    app.session.open_SM_page(smreports)
    #app.testhelpersm.report_is_present()
    #app.testhelpersm.status_is_changed()
    #app.testhelpersm.get_link()


def test_sm_create_contact_report_statictic(app):
    username = app.username
    password = app.password
    smParticipants = app.smParticipants
    smreports = app.smreports
    app.session.ensure_login_sm(username, password)
    app.session.open_SM_page(smParticipants)
    app.testhelpersm.find_region2()
    #app.testhelpersm.check_results()
    app.testhelpersm.create_contact_report_statictic()
    app.session.open_SM_page(smreports)
    #app.testhelpersm.report_is_present()
    #app.testhelpersm.status_is_changed()
    #app.testhelpersm.get_link()

def test_sm_create_contact_list(app):
    username = app.username
    password = app.password
    smParticipants = app.smParticipants
    smreports = app.smreports
    app.session.ensure_login_sm(username, password)
    app.session.open_SM_page(smParticipants)
    app.testhelpersm.find_region2()
    #app.testhelpersm.check_results()
    app.testhelpersm.create_contact_list()
    app.session.open_SM_page(smreports)
    #app.testhelpersm.report_is_present()
    #app.testhelpersm.status_is_changed()
    #app.testhelpersm.get_link()