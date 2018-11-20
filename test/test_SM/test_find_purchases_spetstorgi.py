
#global l
#l = ('0', 'За весь период', 'Сегодня', 'Вчера', 'Последние 7 дней', 'Текущий месяц', 'Прошлый месяц', 'Текущий квартал',
#            'Прошлый квартал', 'Текущий год', 'Прошлый год', 'Выбрать период...')
#	rostelecom@rt.ru

def test_sm_find_purchases_by_text_first_publish_today_spetstorgi(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    index = 2
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    index = 2
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(2)
    app.testHelperSMSearch.press_search_button()
    new_result_spetctorgi = app.testHelperSMSearch.check_results()
    index = 2
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(3)
    app.testHelperSMSearch.press_search_button()
    new_result_without_spetctorgi = app.testHelperSMSearch.check_results()
    assert int(new_result_spetctorgi) != 0
    assert int(new_result_without_spetctorgi) != 0
    assert int(new_result_spetctorgi) < int(old_result)
    assert int(new_result_without_spetctorgi) < int(old_result)



def test_sm_find_purchases_by_text_first_publish_yestoday_spetstorgi(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    index = 3
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    index = 3
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(2)
    app.testHelperSMSearch.press_search_button()
    new_result_spetctorgi = app.testHelperSMSearch.check_results()
    index = 3
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(3)
    app.testHelperSMSearch.press_search_button()
    new_result_without_spetctorgi = app.testHelperSMSearch.check_results()
    assert int(new_result_spetctorgi) != 0
    assert int(new_result_without_spetctorgi) != 0
    assert int(new_result_spetctorgi) < int(old_result)
    assert int(new_result_without_spetctorgi) < int(old_result)


def test_sm_find_purchases_by_text_first_publish_last_7_days_spetstorgi(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    index = 4
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    index = 4
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(2)
    app.testHelperSMSearch.press_search_button()
    new_result_spetctorgi = app.testHelperSMSearch.check_results()
    index = 4
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(3)
    app.testHelperSMSearch.press_search_button()
    new_result_without_spetctorgi = app.testHelperSMSearch.check_results()
    assert int(new_result_spetctorgi) != 0
    assert int(new_result_without_spetctorgi) != 0
    assert int(new_result_spetctorgi) < int(old_result)
    assert int(new_result_without_spetctorgi) < int(old_result)

def test_sm_find_purchases_by_text_first_publish_current_month_spetstorgi(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    index = 5
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    index = 5
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(2)
    app.testHelperSMSearch.press_search_button()
    new_result_spetctorgi = app.testHelperSMSearch.check_results()
    index = 5
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(3)
    app.testHelperSMSearch.press_search_button()
    new_result_without_spetctorgi = app.testHelperSMSearch.check_results()
    assert int(new_result_spetctorgi) != 0
    assert int(new_result_without_spetctorgi) != 0
    assert int(new_result_spetctorgi) < int(old_result)
    assert int(new_result_without_spetctorgi) < int(old_result)

def test_sm_find_purchases_by_text_first_publish_prev_month_spetstorgi(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    index = 6
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    index = 6
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(2)
    app.testHelperSMSearch.press_search_button()
    new_result_spetctorgi = app.testHelperSMSearch.check_results()
    index = 6
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(3)
    app.testHelperSMSearch.press_search_button()
    new_result_without_spetctorgi = app.testHelperSMSearch.check_results()
    assert int(new_result_spetctorgi) != 0
    assert int(new_result_without_spetctorgi) != 0
    assert int(new_result_spetctorgi) < int(old_result)
    assert int(new_result_without_spetctorgi) < int(old_result)

def test_sm_find_purchases_by_text_first_publish_current_kvartal_spetstorgi(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    index = 7
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    index = 7
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(2)
    app.testHelperSMSearch.press_search_button()
    new_result_spetctorgi = app.testHelperSMSearch.check_results()
    index = 7
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(3)
    app.testHelperSMSearch.press_search_button()
    new_result_without_spetctorgi = app.testHelperSMSearch.check_results()
    assert int(new_result_spetctorgi) != 0
    assert int(new_result_without_spetctorgi) != 0
    assert int(new_result_spetctorgi) < int(old_result)
    assert int(new_result_without_spetctorgi) < int(old_result)

def test_sm_find_purchases_by_text_first_publish_prev_kvartal_spetstorgi(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    index = 8
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    index = 8
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(2)
    app.testHelperSMSearch.press_search_button()
    new_result_spetctorgi = app.testHelperSMSearch.check_results()
    index = 8
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(3)
    app.testHelperSMSearch.press_search_button()
    new_result_without_spetctorgi = app.testHelperSMSearch.check_results()
    assert int(new_result_spetctorgi) != 0
    assert int(new_result_without_spetctorgi) != 0
    assert int(new_result_spetctorgi) < int(old_result)
    assert int(new_result_without_spetctorgi) < int(old_result)

def test_sm_find_purchases_by_first_publish_current_year_spetstorgi(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    index = 9
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    index = 9
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(2)
    app.testHelperSMSearch.press_search_button()
    new_result_spetctorgi = app.testHelperSMSearch.check_results()
    index = 9
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(3)
    app.testHelperSMSearch.press_search_button()
    new_result_without_spetctorgi = app.testHelperSMSearch.check_results()
    assert int(new_result_spetctorgi) != 0
    assert int(new_result_without_spetctorgi) != 0
    assert int(new_result_spetctorgi) < int(old_result)
    assert int(new_result_without_spetctorgi) < int(old_result)

def test_sm_find_purchases_by_text_first_publish_prev_year_spetstorgi(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    index = 10
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    index = 10
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(2)
    app.testHelperSMSearch.press_search_button()
    new_result_spetctorgi = app.testHelperSMSearch.check_results()
    index = 10
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(3)
    app.testHelperSMSearch.press_search_button()
    new_result_without_spetctorgi = app.testHelperSMSearch.check_results()
    assert int(new_result_spetctorgi) != 0
    assert int(new_result_without_spetctorgi) != 0
    assert int(new_result_spetctorgi) < int(old_result)
    assert int(new_result_without_spetctorgi) < int(old_result)

def test_sm_find_purchases_by_text_first_publish_for_all_period_spetstorgi(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    index = 1
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    index = 1
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(2)
    app.testHelperSMSearch.press_search_button()
    new_result_spetctorgi = app.testHelperSMSearch.check_results()
    index = 1
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(3)
    app.testHelperSMSearch.press_search_button()
    new_result_without_spetctorgi = app.testHelperSMSearch.check_results()
    assert int(new_result_spetctorgi) != 0
    assert int(new_result_without_spetctorgi) != 0
    assert int(new_result_spetctorgi) < int(old_result)
    assert int(new_result_without_spetctorgi) < int(old_result)

def test_sm_find_purchases_by_text_first_publish_select_period_spetstorgi(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    index = 11
    app.testHelperSMSearch.select_first_publish_date(index, 1)
    app.testHelperSMSearch.select_spetstorgi(1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    app.testHelperSMSearch.select_spetstorgi(2)
    app.testHelperSMSearch.press_search_button()
    new_result_spetctorgi = app.testHelperSMSearch.check_results()
    app.testHelperSMSearch.select_spetstorgi(3)
    app.testHelperSMSearch.press_search_button()
    new_result_without_spetctorgi = app.testHelperSMSearch.check_results()
    assert int(new_result_spetctorgi) != 0
    assert int(new_result_without_spetctorgi) != 0
    assert int(new_result_spetctorgi) < int(old_result)
    assert int(new_result_without_spetctorgi) < int(old_result)