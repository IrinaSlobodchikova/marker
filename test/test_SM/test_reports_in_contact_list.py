


def test_sm_create_report_covladeltsy(app):
    i1 = "Перейти в списки компаний"
    reestr_ex = "Компании"
    report_type_ex = "Совладельцы"
    state_ex = "Формируется"
    i2 = "Открыть отчеты"
    text = "список компаний %s"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipants)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smParticipants)
            app.testHelperSMSearch.find_in_container_number(6, 0, 0)
            app.testHelperSMSearch.press_search_button()
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%d.%m.%Y %H:%M')
    #app.testhelpersm.create_contact_list_10000(cd2, text)
    app.testhelpersm.create_purchases_company_list_50(cd2, text)
    app.banner_link_button(30, i1)
    assert(app.testhelpersm.contact_or_purchases_list_is_present(cd2, text) == True)
    app.testhelpersm.open_first_contact_list()
    cd3 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_report_covladeltsy()
    app.banner_link_button(30, i2)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd3) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 660) != "Ошибка")


def test_sm_create_report_affelir(app):
    i1 = "Перейти в списки компаний"
    reestr_ex = "Компании"
    report_type_ex = "Отчет по аффилированности"
    state_ex = "Формируется"
    i2 = "Открыть отчеты"
    text = "список компаний %s"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipants)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smParticipants)
            app.testHelperSMSearch.find_in_container_number(6, 0, 0)
            app.testHelperSMSearch.press_search_button()
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%d.%m.%Y %H:%M')
    #app.testhelpersm.create_contact_list_10000(cd2, text)
    app.testhelpersm.create_purchases_company_list_50(cd2, text)
    app.banner_link_button(30, i1)
    assert(app.testhelpersm.contact_or_purchases_list_is_present(cd2, text) == True)
    app.testhelpersm.open_first_contact_list()
    cd3 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_report_affelir()
    app.banner_link_button(30, i2)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd3) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 900) != "Ошибка")


def test_sm_create_report_contacts_from_contact_list_all_in_one_row(app):
    i1 = "Перейти в списки компаний"
    reestr_ex = "Компании"
    report_type_ex = "Контакты"
    state_ex = "Формируется"
    i2 = "Открыть отчеты"
    text = "список компаний %s"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipants)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smParticipants)
            app.testHelperSMSearch.find_in_container_number(6, 0, 0)
            app.testHelperSMSearch.press_search_button()
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%d.%m.%Y %H:%M')
    #app.testhelpersm.create_contact_list_10000(cd2, text)
    app.testhelpersm.create_purchases_company_list_50(cd2, text)
    app.banner_link_button(30, i1)
    assert(app.testhelpersm.contact_or_purchases_list_is_present(cd2, text) == True)
    app.testhelpersm.open_first_contact_list()
    cd3 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_contact_report_allinone_tel_mail()
    app.banner_link_button(30, i2)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd3) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 900) != "Ошибка")


def test_sm_create_report_contacts_from_contact_list_all_in_dif_row(app):
    i1 = "Перейти в списки компаний"
    reestr_ex = "Компании"
    report_type_ex = "Контакты"
    state_ex = "Формируется"
    i2 = "Открыть отчеты"
    text = "список компаний %s"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipants)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smParticipants)
            app.testHelperSMSearch.find_in_container_number(6, 0, 0)
            app.testHelperSMSearch.press_search_button()
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%d.%m.%Y %H:%M')
    #app.testhelpersm.create_contact_list_10000(cd2, text)
    app.testhelpersm.create_purchases_company_list_50(cd2, text)
    app.banner_link_button(30, i1)
    assert(app.testhelpersm.contact_or_purchases_list_is_present(cd2, text) == True)
    app.testhelpersm.open_first_contact_list()
    cd3 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_contact_report_all_in_dif_row_tel_mail()
    app.banner_link_button(30, i2)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd3) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 900) != "Ошибка")


def test_sm_create_report_result(app):
    i1 = "Перейти в списки компаний"
    reestr_ex = "Компании"
    report_type_ex = "Результаты поиска"
    state_ex = "Формируется"
    i2 = "Открыть отчеты"
    text = "список компаний %s"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipants)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smParticipants)
            app.testHelperSMSearch.find_in_container_number(6, 0, 0)
            app.testHelperSMSearch.press_search_button()
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%d.%m.%Y %H:%M')
    #app.testhelpersm.create_contact_list_10000(cd2, text)
    app.testhelpersm.create_purchases_company_list_50(cd2, text)
    app.banner_link_button(30, i1)
    assert(app.testhelpersm.contact_or_purchases_list_is_present(cd2, text) == True)
    app.testhelpersm.open_first_contact_list()
    cd3 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_contact_report_result()
    app.banner_link_button(30, i2)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd3) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 900) != "Ошибка")

