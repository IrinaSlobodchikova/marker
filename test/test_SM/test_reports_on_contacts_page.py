


def test_sm_create_contact_report_all_in_dif_row_tel_mail(app):
    reestr_ex = "Компании"
    report_type_ex = "Контакты"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    app.testhelpersm.find_in_container_number(6, 0)
    if app.testhelpersm.check_results() == '0':
        tr = 1
        while app.testhelpersm.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smParticipants)
            app.testhelpersm.find_in_container_number(6, 0)
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_contact_report_all_in_dif_row_tel_mail()
    app.wait_smBlock(20)
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    #app.testhelpersm.get_report_list()
    app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd2) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 660) != "Ошибка")
    #app.testhelpersm.get_link()


def test_sm_create_contact_report_allinone_tel_mail(app):
    reestr_ex = "Компании"
    report_type_ex = "Контакты"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    app.testhelpersm.find_in_container_number(6, 0)
    if app.testhelpersm.check_results() == '0':
        tr = 1
        while app.testhelpersm.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smParticipants)
            app.testhelpersm.find_in_container_number(6, 0)
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%H:%M')
    cd2 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_contact_report_allinone_tel_mail()
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd2) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 660) != "Ошибка")
    #app.testhelpersm.get_link()


def test_sm_create_contact_report_result(app):
    reestr_ex = "Компании"
    report_type_ex = "Результаты поиска"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    app.testhelpersm.find_in_container_number(6, 0)
    if app.testhelpersm.check_results() == '0':
        tr = 1
        while app.testhelpersm.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smParticipants)
            app.testhelpersm.find_in_container_number(6, 0)
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_contact_report_result()
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd2) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 660) != "Ошибка")
    #app.testhelpersm.get_link()


def test_sm_create_contact_report_statictic(app):
    reestr_ex = "Компании"
    report_type_ex = "Статистика"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    app.testhelpersm.find_in_container_number(6, 0)
    if app.testhelpersm.check_results() == '0':
        tr = 1
        while app.testhelpersm.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smParticipants)
            app.testhelpersm.find_in_container_number(6, 0)
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_contact_report_statictic()
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd2) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 660) != "Ошибка")
    #app.testhelpersm.get_link()

#def test_sm_delete_contact_report_statictic(app):
#    app.session.ensure_login_sm(app.username, app.password)
#    app.session.open_SM_page(app.smreports)
#    app.testhelpersm.delete_report()