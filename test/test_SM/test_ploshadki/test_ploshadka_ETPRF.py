


def test_sm_etprf_include_eic_yestoday(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    name = 'ETPRF'
    app.testHelperSMSearch.select_first_publish_date(3, 0)
    app.testHelperSMSearch.find_torgovaya_ploschadka(name)
    app.testHelperSMSearch.press_search_button()
    assert app.testHelperSMSearch.check_results() != '0'
    assert int(app.testHelperSMSearch.check_results()) > 100


def test_sm_etprf_without_eic_yestoday(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    name = 'ETPRF'
    app.testHelperSMSearch.select_first_publish_date(3, 0)
    app.testHelperSMSearch.find_torgovaya_ploschadka(name)
    app.testHelperSMSearch.find_in_container_number(11, 2, 1)
    app.testHelperSMSearch.find_in_container_number(11, 6, 3)
    app.testHelperSMSearch.find_in_container_number(11, 6, 4)
    app.testHelperSMSearch.press_search_button()
    assert app.testHelperSMSearch.check_results() != '0'
    assert int(app.testHelperSMSearch.check_results()) > 30



def test_sm_etprf_include_eic_yestoday_today(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    name = 'ETPRF'
    app.testHelperSMSearch.select_first_publish_date(11, 0)
    app.testHelperSMSearch.find_torgovaya_ploschadka(name)
    app.testHelperSMSearch.press_search_button()
    assert app.testHelperSMSearch.check_results() != '0'
    assert int(app.testHelperSMSearch.check_results()) > 100



def test_sm_etprf_without_eic_yestoday_today(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    name = 'ETPRF'
    app.testHelperSMSearch.select_first_publish_date(11, 0)
    app.testHelperSMSearch.find_torgovaya_ploschadka(name)
    app.testHelperSMSearch.find_in_container_number(11, 2, 1)
    app.testHelperSMSearch.find_in_container_number(11, 6, 3)
    app.testHelperSMSearch.find_in_container_number(11, 6, 4)
    app.testHelperSMSearch.press_search_button()
    assert app.testHelperSMSearch.check_results() != '0'
    assert int(app.testHelperSMSearch.check_results()) > 30


def test_sm_etprf_include_eic_7_days(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    name = 'ETPRF'
    app.testHelperSMSearch.select_first_publish_date(4, 0)
    app.testHelperSMSearch.find_torgovaya_ploschadka(name)
    app.testHelperSMSearch.press_search_button()
    assert app.testHelperSMSearch.check_results() != '0'
    assert int(app.testHelperSMSearch.check_results()) > 600


def test_sm_etprf_without_eic_7_days(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    name = 'ETPRF'
    app.testHelperSMSearch.select_first_publish_date(4, 0)
    app.testHelperSMSearch.find_torgovaya_ploschadka(name)
    app.testHelperSMSearch.find_in_container_number(11, 2, 1)
    app.testHelperSMSearch.find_in_container_number(11, 6, 3)
    app.testHelperSMSearch.find_in_container_number(11, 6, 4)
    app.testHelperSMSearch.press_search_button()
    assert app.testHelperSMSearch.check_results() != '0'
    assert int(app.testHelperSMSearch.check_results()) > 120


def test_sm_etprf_include_eic_current_month(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    name = 'ETPRF'
    app.testHelperSMSearch.select_first_publish_date(5, 0)
    app.testHelperSMSearch.find_torgovaya_ploschadka(name)
    app.testHelperSMSearch.press_search_button()
    assert app.testHelperSMSearch.check_results() != '0'
    assert int(app.testHelperSMSearch.check_results()) > int(app.testHelperSMSearch.current_date_time_day())*100


def test_sm_etprf_without_eic_current_month(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    name = 'ETPRF'
    app.testHelperSMSearch.select_first_publish_date(5, 0)
    app.testHelperSMSearch.find_torgovaya_ploschadka(name)
    app.testHelperSMSearch.find_in_container_number(11, 2, 1)
    app.testHelperSMSearch.find_in_container_number(11, 6, 3)
    app.testHelperSMSearch.find_in_container_number(11, 6, 4)
    app.testHelperSMSearch.press_search_button()
    assert app.testHelperSMSearch.check_results() != '0'
    assert int(app.testHelperSMSearch.check_results()) > int(app.testHelperSMSearch.current_date_time_day())*20


def test_sm_etprf_include_eic_prev_month(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    name = 'ETPRF'
    app.testHelperSMSearch.select_first_publish_date(6, 0)
    app.testHelperSMSearch.find_torgovaya_ploschadka(name)
    app.testHelperSMSearch.press_search_button()
    assert app.testHelperSMSearch.check_results() != '0'
    assert int(app.testHelperSMSearch.check_results()) > 3500


def test_sm_etprf_without_eic_prev_month(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    name = 'ETPRF'
    app.testHelperSMSearch.select_first_publish_date(6, 0)
    app.testHelperSMSearch.find_torgovaya_ploschadka(name)
    app.testHelperSMSearch.find_in_container_number(11, 2, 1)
    app.testHelperSMSearch.find_in_container_number(11, 6, 3)
    app.testHelperSMSearch.find_in_container_number(11, 6, 4)
    app.testHelperSMSearch.press_search_button()
    assert app.testHelperSMSearch.check_results() != '0'
    assert int(app.testHelperSMSearch.check_results()) > 600