


def test_sm_find_purchases_by_text_data_okonchaniya_today(app):
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
    l = ('Сегодня', 'Завтра', 'Следующие 7 дней', 'До конца месяца', 'До конца квартала', 'До конца года',
         'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_okonchaniya(l[0])
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0

def test_sm_find_purchases_by_text_data_okonchaniya_tomorrow(app):
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
    l = ('Сегодня', 'Завтра', 'Следующие 7 дней', 'До конца месяца', 'До конца квартала', 'До конца года',
         'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_okonchaniya(l[1])
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0

def test_sm_find_purchases_by_text_data_okonchaniya_next_7_days(app):
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
    l = ('Сегодня', 'Завтра', 'Следующие 7 дней', 'До конца месяца', 'До конца квартала', 'До конца года',
         'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_okonchaniya(l[2])
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0

def test_sm_find_purchases_by_text_data_okonchaniya_till_end_of_month(app):
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
    l = ('Сегодня', 'Завтра', 'Следующие 7 дней', 'До конца месяца', 'До конца квартала', 'До конца года',
         'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_okonchaniya(l[3])
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0

def test_sm_find_purchases_by_text_data_okonchaniya_till_end_of_kvartal(app):
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
    l = ('Сегодня', 'Завтра', 'Следующие 7 дней', 'До конца месяца', 'До конца квартала', 'До конца года',
         'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_okonchaniya(l[4])
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0

def test_sm_find_purchases_by_text_data_okonchaniya_till_end_of_year(app):
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
    l = ('Сегодня', 'Завтра', 'Следующие 7 дней', 'До конца месяца', 'До конца квартала', 'До конца года',
         'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_okonchaniya(l[5])
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0

def test_sm_find_purchases_by_text_data_okonchaniya_for_all_period(app):
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
    l = ('Сегодня', 'Завтра', 'Следующие 7 дней', 'До конца месяца', 'До конца квартала', 'До конца года',
         'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_okonchaniya(l[6])
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0

def test_sm_find_purchases_by_text_data_okonchaniya_selected_period(app):
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
    l = ('Сегодня', 'Завтра', 'Следующие 7 дней', 'До конца месяца', 'До конца квартала', 'До конца года',
         'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_okonchaniya(l[7])
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) > 0