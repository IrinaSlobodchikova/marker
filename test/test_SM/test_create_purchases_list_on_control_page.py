

def test_sm_create_purchases_list(app):
    i = "Перейти в списки публикаций"
    text = "список торгов %s"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smKontrol)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(12, 0, 0)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smKontrol)
            app.testHelperSMSearch.find_in_container_number(12, 1, 0)
            app.testHelperSMSearch.press_search_button()
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%d.%m.%Y %H:%M')
    app.testhelpersm.create_contact_list_10000(cd2, text)
    #app.testhelpersm.create_purchases_company_list_50(cd2, text)
    app.banner_link_button(30, i)
    assert(app.testhelpersm.contact_or_purchases_list_is_present(cd2, text) == True)
