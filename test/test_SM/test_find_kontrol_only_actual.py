
#global l
#l = ('Сегодня', 'Вчера', 'Последние 7 дней', 'Текущий месяц', 'Прошлый месяц', 'Текущий квартал',
#            'Прошлый квартал', 'Текущий год', 'Прошлый год', 'Выбрать период...')
#	rostelecom@rt.ru

def test_sm_find_kontrol_by_text_data_nachala_today_actual(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smKontrol)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    l = ('Сегодня', 'Вчера', 'Последние 7 дней', 'Текущий месяц', 'Прошлый месяц', 'Текущий квартал',
            'Прошлый квартал', 'Текущий год', 'Прошлый год', 'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_nachala(l[0], 1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    app.testHelperSMSearch.select_data_nachala(l[0], 1)
    app.testHelperSMSearch.select_actual_only()
    app.testHelperSMSearch.press_search_button()
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) != 0
    assert int(old_result) != 0
    assert int(old_result) > int(new_result)

def test_sm_find_kontrol_by_text_data_nachala_yestoday_actual(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smKontrol)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    l = ('Сегодня', 'Вчера', 'Последние 7 дней', 'Текущий месяц', 'Прошлый месяц', 'Текущий квартал',
            'Прошлый квартал', 'Текущий год', 'Прошлый год', 'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_nachala(l[1], 1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    app.testHelperSMSearch.select_data_nachala(l[1], 1)
    app.testHelperSMSearch.select_actual_only()
    app.testHelperSMSearch.press_search_button()
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) != 0
    assert int(old_result) != 0
    assert int(old_result) > int(new_result)

def test_sm_find_kontrol_by_text_data_nachala_last_7_days_actual(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smKontrol)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    l = ('Сегодня', 'Вчера', 'Последние 7 дней', 'Текущий месяц', 'Прошлый месяц', 'Текущий квартал',
            'Прошлый квартал', 'Текущий год', 'Прошлый год', 'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_nachala(l[2], 1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    app.testHelperSMSearch.select_data_nachala(l[2], 1)
    app.testHelperSMSearch.select_actual_only()
    app.testHelperSMSearch.press_search_button()
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) != 0
    assert int(old_result) != 0
    assert int(old_result) > int(new_result)

def test_sm_find_kontrol_by_text_data_nachala_current_month_actual(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smKontrol)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    l = ('Сегодня', 'Вчера', 'Последние 7 дней', 'Текущий месяц', 'Прошлый месяц', 'Текущий квартал',
            'Прошлый квартал', 'Текущий год', 'Прошлый год', 'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_nachala(l[3], 1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    app.testHelperSMSearch.select_data_nachala(l[3], 1)
    app.testHelperSMSearch.select_actual_only()
    app.testHelperSMSearch.press_search_button()
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) != 0
    assert int(old_result) != 0
    assert int(old_result) > int(new_result)

def test_sm_find_kontrol_by_text_data_nachala_prev_month_actual(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smKontrol)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    l = ('Сегодня', 'Вчера', 'Последние 7 дней', 'Текущий месяц', 'Прошлый месяц', 'Текущий квартал',
            'Прошлый квартал', 'Текущий год', 'Прошлый год', 'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_nachala(l[4], 1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    app.testHelperSMSearch.select_data_nachala(l[4], 1)
    app.testHelperSMSearch.select_actual_only()
    app.testHelperSMSearch.press_search_button()
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) != 0
    assert int(old_result) != 0
    assert int(old_result) > int(new_result)

def test_sm_find_kontrol_by_text_data_nachala_current_kvartal_actual(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smKontrol)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    l = ('Сегодня', 'Вчера', 'Последние 7 дней', 'Текущий месяц', 'Прошлый месяц', 'Текущий квартал',
            'Прошлый квартал', 'Текущий год', 'Прошлый год', 'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_nachala(l[5], 1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    app.testHelperSMSearch.select_data_nachala(l[5], 1)
    app.testHelperSMSearch.select_actual_only()
    app.testHelperSMSearch.press_search_button()
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) != 0
    assert int(old_result) != 0
    assert int(old_result) > int(new_result)

def test_sm_find_kontrol_by_text_data_nachala_prev_kvartal_actual(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smKontrol)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    l = ('Сегодня', 'Вчера', 'Последние 7 дней', 'Текущий месяц', 'Прошлый месяц', 'Текущий квартал',
            'Прошлый квартал', 'Текущий год', 'Прошлый год', 'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_nachala(l[6], 1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    app.testHelperSMSearch.select_data_nachala(l[6], 1)
    app.testHelperSMSearch.select_actual_only()
    app.testHelperSMSearch.press_search_button()
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) != 0
    assert int(old_result) != 0
    assert int(old_result) > int(new_result)


def test_sm_find_kontrol_by_text_data_current_year_actual(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smKontrol)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    l = ('Сегодня', 'Вчера', 'Последние 7 дней', 'Текущий месяц', 'Прошлый месяц', 'Текущий квартал',
            'Прошлый квартал', 'Текущий год', 'Прошлый год', 'За весь период', 'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_nachala(l[7], 1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    app.testHelperSMSearch.select_data_nachala(l[7], 1)
    app.testHelperSMSearch.select_actual_only()
    app.testHelperSMSearch.press_search_button()
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) != 0
    assert int(old_result) != 0
    assert int(old_result) > int(new_result)

def test_sm_find_kontrol_by_text_data_nachala_prev_year_actual(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smKontrol)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    l = ('Сегодня', 'Вчера', 'Последние 7 дней', 'Текущий месяц', 'Прошлый месяц', 'Текущий квартал',
            'Прошлый квартал', 'Текущий год', 'Прошлый год', 'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_nachala(l[8], 1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    app.testHelperSMSearch.select_data_nachala(l[8], 1)
    app.testHelperSMSearch.select_actual_only()
    app.testHelperSMSearch.press_search_button()
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) != 0
    assert int(old_result) != 0
    assert int(old_result) > int(new_result)

def test_sm_find_kontrol_by_text_data_nachala_for_all_period_actual(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smKontrol)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    l = ('Сегодня', 'Вчера', 'Последние 7 дней', 'Текущий месяц', 'Прошлый месяц', 'Текущий квартал',
            'Прошлый квартал', 'Текущий год', 'Прошлый год', 'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_nachala(l[9], 1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    app.testHelperSMSearch.select_data_nachala(l[9], 1)
    app.testHelperSMSearch.select_actual_only()
    app.testHelperSMSearch.press_search_button()
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) != 0
    assert int(old_result) != 0
    assert int(old_result) > int(new_result)

def test_sm_find_kontrol_by_text_data_nachala_select_period_actual(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smKontrol)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    app.testHelperSMSearch.expand_show_hide()
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    #s = app.testhelpersm.find_in_container_number(6, 0, 0)
    app.testHelperSMSearch.enter_text_in_seach_field("колбаса")
    l = ('Сегодня', 'Вчера', 'Последние 7 дней', 'Текущий месяц', 'Прошлый месяц', 'Текущий квартал',
            'Прошлый квартал', 'Текущий год', 'Прошлый год', 'За весь период', 'Выбрать период...')
    app.testHelperSMSearch.select_data_nachala(l[10], 1)
    app.testHelperSMSearch.press_search_button()
    #if app.testhelpersm.check_results() == '0':
    #    tr = 1
    #    while app.testhelpersm.check_results() == '0' and tr < 20:
    #        app.session.open_SM_page(app.smParticipants)
    #        s = app.testhelpersm.find_in_container_number(6, 0, 0)
    #        tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    app.testHelperSMSearch.select_actual_only()
    app.testHelperSMSearch.press_search_button()
    new_result = app.testHelperSMSearch.check_results()
    assert int(new_result) != 0
    assert int(old_result) != 0
    assert int(old_result) > int(new_result)