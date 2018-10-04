

def test_sm_create_purchases_list(app):
    i = "Перейти в списки публикаций"
    text = "список торгов %s"
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    # первый параметр количество контейнеров
    # второй парамерт конкретный контейнер
    app.testhelpersm.find_in_container_number(12, 0)
    if app.testhelpersm.check_results() == '0':
        tr = 1
        while app.testhelpersm.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smKontrol)
            app.testhelpersm.find_in_container_number(12, 1)
            tr = tr + 1
    cd2 = app.current_date_time().strftime('%d.%m.%Y %H:%M')
    app.testhelpersm.create_contact_list_10000(cd2, text)
    #app.testhelpersm.create_purchases_list_50(cd2, text)
    app.banner_link_button(30, i)
    assert(app.testhelpersm.contact_or_purchases_list_is_present(cd2, text) == True)
