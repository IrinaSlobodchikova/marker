

#	rostelecom@rt.ru

def test_sm_find_company_by_email_company(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipants)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_email("rostelecom@rt.ru")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0


def test_sm_find_company_by_email_zakazchiki(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_email("rostelecom@rt.ru")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0


def test_sm_find_company_by_email_poctavchiki(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_email("rostelecom@rt.ru")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0