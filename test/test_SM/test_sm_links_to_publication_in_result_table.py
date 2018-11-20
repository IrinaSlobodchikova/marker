

def test_sm_link_smPurchases_publication(app):
    exp_result = "Торги и контракты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере если 0 - случайный выбор)
    app.testHelperSMSearch.find_in_container_number(11, 2, 3)
    app.testHelperSMSearch.press_search_button()
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smPurchases)
            app.testHelperSMSearch.find_in_container_number(11, 1, 0)
            app.testHelperSMSearch.press_search_button()
            tr = tr + 1
    #первый параметр (номер строки, если 0 - случайный выбор), второй номер колонки в таблице
    s = app.testHelperSMSearch.get_one_table_parametr(0, 3)
    app.session.open_href_page(s[4])
    s2 = app.testHelperSMSearch.compare_lot()
    assert s[3] == s2[0] or s[3] == s2[1]
    assert s[8] == s2[2]
    assert s[0] == s2[3] or s[5] == s2[3]
    assert s[1] == s2[4]
    assert s[0] == s2[5]
    assert s[6] == s2[6]
    assert s[5] == s2[7]
    #zakazchik_summ, zakazchik, href_zakazchik, publication_name, href_publication, poctavschik_summ, poctavschik, href_poctavschik,  period
    #current_text_in_header, short_name_text, period, price, customer, customer_price, seller, seller_price

    #Найти наименование заказчика, публикации, поставщика, стоимость заказчика, стоимость поставщика, период
    #кликнуть по ссылке наименование публикации
    # дождаться открытия ссылки в новом окне
    #проверить совпадения полей наименование заказчика, публикации, поставщика, стоимость заказчика, стоимость поставщика, период


