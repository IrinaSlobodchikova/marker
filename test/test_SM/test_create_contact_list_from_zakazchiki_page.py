

def test_sm_create_contact_list(app):
    i = "Перейти в списки компаний"
    text = "список компаний %s"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsCustomers)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(3, 0, 0)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smParticipantsCustomers)
            app.testHelperSMSearch.find_in_container_number(3, 0, 0)
            app.testHelperSMSearch.press_search_button()
            tr = tr + 1
    #app.testhelpersm.get_old_contact_list()
    cd2 = app.current_date_time().strftime('%d.%m.%Y %H:%M')
    app.testhelpersm.create_contact_list_10000(cd2, text)
    #app.testhelpersm.create_purchases_company_list_50(cd2, text)
    app.banner_link_button(30, i)
    assert(app.testhelpersm.contact_or_purchases_list_is_present(cd2, text) == True)
    #app.testhelpersm.get_link()


#def test_sm_delete_contact_list(app):
#    app.session.ensure_login_sm(app.username, app.password)
#    app.session.open_SM_page(app.smcompany_list)
#    app.testhelpersm.delete_first_contact_list()