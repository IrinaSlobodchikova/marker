



def test_sm_saved_request_monitoring_on_company_page(app):
    i1 = "Перейти в сохраненные запросы"
    reestr_ex = "Компании"
    text = "Запрос по странице компании %s"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipants)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    s = app.testhelpersm.find_in_container_number(6, 0)
    old_parametr = app.testhelpersm.get_artef_param(s[1])
    if app.testhelpersm.check_results() == '0':
        tr = 1
        while app.testhelpersm.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smParticipants)
            s = app.testhelpersm.find_in_container_number(6, 0)
            tr = tr + 1
    old_result = app.testhelpersm.check_results()
    cd2 = app.current_date_time().strftime('%d.%m.%Y %H:%M')
    cd3 = app.current_date_time().strftime('%H:%M')
    app.testhelpersm.save_requesr(cd2, text)
    #app.banner_link_button(30, i1)
    app.session.open_SM_page(app.smMonitorinds)
    assert (app.testhelpersm.monitoring_is_present(cd2, cd3, text, reestr_ex) == True)
    app.testhelpersm.click_on_monitoring_link(cd2, text)
    new_parametr = app.testhelpersm.get_artef_param(s[1])
    assert (old_parametr == new_parametr)
    new_result = app.testhelpersm.check_results()
    assert int(old_result) == int(new_result)

