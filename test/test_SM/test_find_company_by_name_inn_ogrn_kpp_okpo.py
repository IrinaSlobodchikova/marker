

#	rostelecom@rt.ru

def test_sm_find_company_by_name_company(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipants)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("ростелеком")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0


def test_sm_find_company_by_name_zakazchiki(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("ростелеком")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0


def test_sm_find_company_by_name_poctavchiki(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("ростелеком")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0

def test_sm_find_company_by_inn_company(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipants)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("7707049388")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0


def test_sm_find_company_by_inn_zakazchiki(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("7707049388")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0


def test_sm_find_company_by_inn_poctavchiki(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("7707049388")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0

def test_sm_find_company_by_ogrn_company(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipants)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("1027700198767")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0


def test_sm_find_company_by_ogrn_zakazchiki(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("1027700198767")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0


def test_sm_find_company_by_ogrn_poctavchiki(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("1027700198767")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0

def test_sm_find_company_by_kpp_company(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipants)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("784001001")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0


def test_sm_find_company_by_kpp_zakazchiki(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("784001001")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0


def test_sm_find_company_by_kpp_poctavchiki(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("784001001")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0

def test_sm_find_company_by_okpo_company(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipants)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("17514186")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0


def test_sm_find_company_by_okpo_zakazchiki(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("17514186")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0


def test_sm_find_company_by_okpo_poctavchiki(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("17514186")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0

def test_sm_find_company_by_name_inn_ogrn_kpp_okpo_company(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipants)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("ростелеком 7707049388 1027700198767 784001001 17514186")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0


def test_sm_find_company_by_name_inn_ogrn_kpp_okpo_zakazchiki(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("ростелеком 7707049388 1027700198767 784001001 17514186")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0


def test_sm_find_company_by_name_inn_ogrn_kpp_okpo_poctavchiki(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.find_company_by_name("ростелеком 7707049388 1027700198767 784001001 17514186")
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0