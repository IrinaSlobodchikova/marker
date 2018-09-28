


def test_sm_create_contact_report_all_in_dif_row_tel_mail(app):
    username = app.username
    password = app.password
    smParticipants = app.smParticipants
    smreports = app.smreports
    reestr_ex = "Компании"
    report_type_ex = "Контакты"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.session.ensure_login_sm(username, password)
    app.session.ensure_login_sm(username, password)
    app.session.open_SM_page(smParticipants)
    app.testhelpersm.find_region2()
    app.testhelpersm.check_results()
    app.testhelpersm.create_contact_report_all_in_dif_row_tel_mail()
    app.wait_smBlock(20)
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    #app.testhelpersm.get_report_list()
    app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert(app.status_is_changed(state_ex, 660) != "Ошибка")
    #app.testhelpersm.get_link()


def test_sm_create_contact_report_allinone_tel_mail(app):
    username = app.username
    password = app.password
    smParticipants = app.smParticipants
    smreports = app.smreports
    reestr_ex = "Компании"
    report_type_ex = "Контакты"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.session.ensure_login_sm(username, password)
    app.session.open_SM_page(smParticipants)
    app.testhelpersm.find_region2()
    app.testhelpersm.check_results()
    app.testhelpersm.create_contact_report_allinone_tel_mail()
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert(app.status_is_changed(state_ex, 660) != "Ошибка")
    #app.testhelpersm.get_link()


def test_sm_create_contact_report_result(app):
    username = app.username
    password = app.password
    smParticipants = app.smParticipants
    smreports = app.smreports
    reestr_ex = "Компании"
    report_type_ex = "Результаты поиска"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.session.ensure_login_sm(username, password)
    app.session.open_SM_page(smParticipants)
    app.testhelpersm.find_region2()
    app.testhelpersm.check_results()
    app.testhelpersm.create_contact_report_result()
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert(app.status_is_changed(state_ex, 660) != "Ошибка")
    #app.testhelpersm.get_link()


def test_sm_create_contact_report_statictic(app):
    username = app.username
    password = app.password
    smParticipants = app.smParticipants
    smreports = app.smreports
    reestr_ex = "Компании"
    report_type_ex = "Статистика"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.session.ensure_login_sm(username, password)
    app.session.open_SM_page(smParticipants)
    app.testhelpersm.find_region2()
    app.testhelpersm.check_results()
    app.testhelpersm.create_contact_report_statictic()
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert(app.status_is_changed(state_ex, 660) != "Ошибка")
    #app.testhelpersm.get_link()

#def test_sm_delete_contact_report_statictic(app):
#    username = app.username
#    password = app.password
#    smParticipants = app.smParticipants
#    smreports = app.smreports
#    app.session.ensure_login_sm(username, password)
#    app.session.open_SM_page(smreports)
#    app.testhelpersm.delete_report()