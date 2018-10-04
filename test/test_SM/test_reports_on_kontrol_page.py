


def test_sm_create_kontrol_report_result(app):
    reestr_ex = "Контроль"
    report_type_ex = "Результаты поиска"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    app.testhelpersm.find_in_container_number(11, 0)
    if app.testhelpersm.check_results() == '0':
        tr = 1
        while app.testhelpersm.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smKontrol)
            app.testhelpersm.find_in_container_number(11, 0)
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_contact_report_result()
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd2) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 900) != "Ошибка")
    #app.testhelpersm.get_link()




def test_sm_kontrol_contact_report_Prices_zakazchik(app):
    reestr_ex = "Контроль"
    report_type_ex = "Цены"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    app.testhelpersm.find_in_container_number(11, 0)
    if app.testhelpersm.check_results() == '0':
        tr = 1
        while app.testhelpersm.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smKontrol)
            app.testhelpersm.find_in_container_number(11, 0)
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_report_prices_zakazchik()
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd2) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 900) != "Ошибка")


def test_sm_kontrol_contact_report_Prices_postavschik(app):
    reestr_ex = "Контроль"
    report_type_ex = "Цены"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    app.testhelpersm.find_in_container_number(11, 0)
    if app.testhelpersm.check_results() == '0':
        tr = 1
        while app.testhelpersm.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smKontrol)
            app.testhelpersm.find_in_container_number(11, 0)
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_report_prices_postavschik()
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    #app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd2) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 900) != "Ошибка")