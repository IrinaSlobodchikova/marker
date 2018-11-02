


def test_sm_create_certificates_report_all_in_dif_row_tel_mail_postavchiki(app):
    reestr_ex = "Сертификаты"
    report_type_ex = "Контакты"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smCertificates)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smCertificates)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(7, 0, 0)
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smCertificates)
            app.testHelperSMSearch.find_in_container_number(7, 0, 0)
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_contact_report_all_in_dif_row_tel_mail()
    app.wait_smBlock(20)
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    #   app.testhelpersm.get_report_list()
    app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd2) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 3600) != "Ошибка")


def test_sm_create_certificates_report_result(app):
    reestr_ex = "Сертификаты"
    report_type_ex = "Результаты поиска"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smCertificates)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smCertificates)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(7, 0, 0)
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smCertificates)
            app.testHelperSMSearch.find_in_container_number(7, 0, 0)
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


