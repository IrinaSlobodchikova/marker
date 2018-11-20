



def test_sm_saved_request_monitoring_on_zakazchiki_page(app):
    i1 = "Перейти в сохраненные запросы"
    reestr_ex = "Заказчики"
    text = "Запрос по странице заказчики %s"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsCustomers)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    s = app.testHelperSMSearch.find_in_container_number(3, 0, 0)
    app.testHelperSMSearch.press_search_button()
    old_parametr = app.testHelperSMSearch.get_artef_param(s[1])
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smParticipantsCustomers)
            s = app.testHelperSMSearch.find_in_container_number(3, 0, 0)
            app.testHelperSMSearch.press_search_button()
            tr = tr + 1
    old_result = app.testHelperSMSearch.check_results()
    cd2 = app.current_date_time().strftime('%d.%m.%Y %H:%M')
    cd3 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.save_requesr(cd2, text)
    #app.banner_link_button(30, i1)
    app.session.open_SM_page(app.smMonitorinds)
    assert (app.testhelpersm.monitoring_is_present(cd2, cd3, text, reestr_ex) == True)
    app.testhelpersm.click_on_monitoring_link(cd2, text)
    new_parametr = app.testHelperSMSearch.get_artef_param(s[1])
    assert (old_parametr == new_parametr)
    new_result = app.testHelperSMSearch.check_results()
    assert int(old_result) == int(new_result)

