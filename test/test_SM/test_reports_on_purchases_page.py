

def test_sm_create_contact_report_all_in_dif_row_tel_mail_postavchiki(app):
    reestr_ex = "Торги"
    report_type_ex = "Контакты"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(11, 0, 0)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smPurchases)
            app.testHelperSMSearch.find_in_container_number(11, 0, 0)
            app.testHelperSMSearch.press_search_button()
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


def test_sm_create_contact_report_all_in_dif_row_tel_mail_zakazchiki(app):
    reestr_ex = "Торги"
    report_type_ex = "Контакты"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(11, 0, 0)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smPurchases)
            app.testHelperSMSearch.find_in_container_number(11, 0, 0)
            app.testHelperSMSearch.press_search_button()
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_contact_report_all_in_dif_row_tel_mail_zakazchiki()
    app.wait_smBlock(20)
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    #   app.testhelpersm.get_report_list()
    app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd2) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 3600) != "Ошибка")


def test_sm_create_contact_report_allinone_tel_mail_postavchiki(app):
    reestr_ex = "Торги"
    report_type_ex = "Контакты"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(11, 0, 0)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smPurchases)
            app.testHelperSMSearch.find_in_container_number(11, 0, 0)
            app.testHelperSMSearch.press_search_button()
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_contact_report_allinone_tel_mail()
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd2) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 3600) != "Ошибка")
    #app.testhelpersm.get_link()


def test_sm_create_contact_report_allinone_tel_mail_zakazchiki(app):
    reestr_ex = "Торги"
    report_type_ex = "Контакты"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(11, 0, 0)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smPurchases)
            app.testHelperSMSearch.find_in_container_number(11, 0, 0)
            app.testHelperSMSearch.press_search_button()
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_contact_report_allinone_tel_mail_zakazchiki()
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd2) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 3600) != "Ошибка")


def test_sm_create_purchases_report_result(app):
    reestr_ex = "Торги"
    report_type_ex = "Результаты поиска"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(11, 0, 0)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smPurchases)
            app.testHelperSMSearch.find_in_container_number(11, 0, 0)
            app.testHelperSMSearch.press_search_button()
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


def test_sm_purchases_contact_report_statictic(app):
    reestr_ex = "Торги"
    report_type_ex = "Статистика"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(11, 0, 0)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testhelpersm.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smPurchases)
            app.testHelperSMSearch.find_in_container_number(11, 0, 0)
            app.testHelperSMSearch.press_search_button()
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.create_contact_report_statictic()
    app.banner_link_button(30, i)
    #app.session.open_SM_page(smreports)
    app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex)
    assert(app.testhelpersm.report_is_present_short(reestr_ex, report_type_ex, state_ex) == True)
    assert (app.testhelpersm.report_is_present_date(cd2) == True)
    if app.check_report_result == "True":
        assert(app.status_is_changed(state_ex, 900) != "Ошибка")
    #app.testhelpersm.get_link()

def test_sm_purchases_contact_report_Prices_zakazchik(app):
    reestr_ex = "Торги"
    report_type_ex = "Цены"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(11, 0, 0)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smPurchases)
            app.testHelperSMSearch.find_in_container_number(11, 0, 0)
            app.testHelperSMSearch.press_search_button()
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


def test_sm_purchases_contact_report_Prices_postavschik(app):
    reestr_ex = "Торги"
    report_type_ex = "Цены"
    state_ex = "Формируется"
    i = "Открыть отчеты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(11, 0, 0)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smPurchases)
            app.testHelperSMSearch.find_in_container_number(11, 0, 0)
            app.testHelperSMSearch.press_search_button()
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