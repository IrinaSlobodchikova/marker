

def test_sm_link_smPurchases_Zakazschik(app):
    exp_result = "Торги и контракты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере (если 0 - случайный выбор))
    app.testHelperSMSearch.find_in_container_number(11, 2, 2)
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smPurchases)
            app.testHelperSMSearch.find_in_container_number(11, 0, 0)
            tr = tr + 1
    #первый параметр (номер строки, если 0 - случайный выбор), второй номер колонки в таблице
    s = app.testHelperSMSearch.get_one_table_parametr(0, 1)
    #app.testhelpersm.click_on_zakazschik_link_in_result_tab(s[1])
    app.session.open_href_page(s[0])
    s2 = app.testHelperSMSearch.compare_company_name()
    assert s[2] == s2[0]
    assert s[2] == s2[1]


def test_sm_link_smPurchases_Postavchik(app):
    exp_result = "Торги и контракты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере (если 0 - случайный выбор))
    app.testHelperSMSearch.find_in_container_number(11, 1, 2)
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smPurchases)
            app.testHelperSMSearch.find_in_container_number(11, 2, 2)
            tr = tr + 1
    #первый параметр (номер строки, если 0 - случайный выбор), второй номер колонки в таблице
    s = app.testHelperSMSearch.get_one_table_parametr(0, 4)
    #app.testhelpersm.click_on_zakazschik_link_in_result_tab(s[1])
    app.session.open_href_page(s[0])
    s2 = app.testHelperSMSearch.compare_company_name()
    assert s[2] == s2[0]
    assert s[2] == s2[1]


def test_sm_link_smParticipants_company(app):
    exp_result = "Торги и контракты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipants)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере (если 0 - случайный выбор))
    app.testHelperSMSearch.find_in_container_number(6, 0, 0)
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smParticipants)
            app.testHelperSMSearch.find_in_container_number(6, 0, 0)
            tr = tr + 1
    #первый параметр (номер строки, если 0 - случайный выбор), второй номер колонки в таблице
    s = app.testHelperSMSearch.get_one_table_parametr(0, 1)
    #app.testhelpersm.click_on_zakazschik_link_in_result_tab(s[1])
    app.session.open_href_page(s[0])
    s2 = app.testHelperSMSearch.compare_company_name()
    assert s[2] == s2[0]
    assert s[2] == s2[1]

def test_sm_link_smParticipantsCustomers_company(app):
    exp_result = "Торги и контракты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsCustomers)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере (если 0 - случайный выбор))
    app.testHelperSMSearch.find_in_container_number(3, 0, 0)
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smParticipantsCustomers)
            app.testHelperSMSearch.find_in_container_number(3, 0, 0)
            tr = tr + 1
    #первый параметр (номер строки, если 0 - случайный выбор), второй номер колонки в таблице
    s = app.testHelperSMSearch.get_one_table_parametr(0, 1)
    #app.testhelpersm.click_on_zakazschik_link_in_result_tab(s[1])
    app.session.open_href_page(s[0])
    s2 = app.testHelperSMSearch.compare_company_name()
    assert s[2] == s2[0]
    assert s[2] == s2[1]

def test_sm_link_smParticipantsSuppliers_company(app):
    exp_result = "Торги и контракты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsSuppliers)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере (если 0 - случайный выбор))
    app.testHelperSMSearch.find_in_container_number(4, 0, 0)
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smParticipantsSuppliers)
            app.testHelperSMSearch.find_in_container_number(4, 0, 0)
            tr = tr + 1
    #первый параметр (номер строки, если 0 - случайный выбор), второй номер колонки в таблице
    s = app.testHelperSMSearch.get_one_table_parametr(0, 1)
    #app.testhelpersm.click_on_zakazschik_link_in_result_tab(s[1])
    app.session.open_href_page(s[0])
    s2 = app.testHelperSMSearch.compare_company_name()
    assert s[2] == s2[0]
    assert s[2] == s2[1]

def test_sm_link_smPrices_company(app):
    exp_result = "Торги и контракты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPrices)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPrices)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере (если 0 - случайный выбор))
    app.testHelperSMSearch.find_in_container_number(5, 0, 0)
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smPrices)
            app.testHelperSMSearch.find_in_container_number(5, 0, 0)
            tr = tr + 1
    #первый параметр (номер строки, если 0 - случайный выбор), второй номер колонки в таблице
    s = app.testHelperSMSearch.get_one_table_parametr(0, 1)
    #app.testhelpersm.click_on_zakazschik_link_in_result_tab(s[1])
    app.session.open_href_page(s[0])
    s2 = app.testHelperSMSearch.compare_company_name()
    assert s[2] == s2[0]
    assert s[2] == s2[1]

def test_sm_link_smCertificates_Zayavitel(app):
    exp_result = "Торги и контракты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smCertificates)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smCertificates)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере (если 0 - случайный выбор))
    app.testHelperSMSearch.find_in_container_number(5, 0, 0)
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smCertificates)
            app.testHelperSMSearch.find_in_container_number(5, 0, 0)
            tr = tr + 1
    #первый параметр (номер строки, если 0 - случайный выбор), второй номер колонки в таблице
    s = app.testHelperSMSearch.get_one_table_parametr(0, 1)
    #app.testhelpersm.click_on_zakazschik_link_in_result_tab(s[1])
    app.session.open_href_page(s[0])
    s2 = app.testHelperSMSearch.compare_company_name()
    assert s[2] == s2[0]
    assert s[2] == s2[1]

def test_sm_link_smCertificates_Proizvoditel(app):
    exp_result = "Торги и контракты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smCertificates)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smCertificates)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере (если 0 - случайный выбор))
    app.testHelperSMSearch.find_in_container_number(5, 0, 0)
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smCertificates)
            app.testHelperSMSearch.find_in_container_number(5, 0, 0)
            tr = tr + 1
    #первый параметр (номер строки, если 0 - случайный выбор), второй номер колонки в таблице
    s = app.testHelperSMSearch.get_one_table_parametr(0, 2)
    #app.testhelpersm.click_on_zakazschik_link_in_result_tab(s[1])
    app.session.open_href_page(s[0])
    s2 = app.testHelperSMSearch.compare_company_name()
    assert s[2] == s2[0]
    assert s[2] == s2[1]

def test_sm_link_smCertificates_Organ_sertifikatsii(app):
    exp_result = "Торги и контракты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smCertificates)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smCertificates)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере (если 0 - случайный выбор))
    app.testHelperSMSearch.find_in_container_number(5, 0, 0)
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smCertificates)
            app.testHelperSMSearch.find_in_container_number(5, 0, 0)
            tr = tr + 1
    #первый параметр (номер строки, если 0 - случайный выбор), второй номер колонки в таблице
    s = app.testHelperSMSearch.get_one_table_parametr(0, 5)
    #app.testhelpersm.click_on_zakazschik_link_in_result_tab(s[1])
    app.session.open_href_page(s[0])
    s2 = app.testHelperSMSearch.compare_company_name()
    assert s[2] == s2[0]
    assert s[2] == s2[1]

def test_sm_link_smLicences(app):
    exp_result = "Торги и контракты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smLicences)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smLicences)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере (если 0 - случайный выбор))
    app.testHelperSMSearch.find_in_container_number(3, 0, 0)
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smLicences)
            app.testHelperSMSearch.find_in_container_number(3, 0, 0)
            tr = tr + 1
    #первый параметр (номер строки, если 0 - случайный выбор), второй номер колонки в таблице
    s = app.testHelperSMSearch.get_one_table_parametr(0, 1)
    #app.testhelpersm.click_on_zakazschik_link_in_result_tab(s[1])
    app.session.open_href_page(s[0])
    s2 = app.testHelperSMSearch.compare_company_name()
    assert s[2] == s2[0]
    assert s[2] == s2[1]

def test_sm_link_smKontrol_Zakazschik(app):
    exp_result = "Торги и контракты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smKontrol)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере (если 0 - случайный выбор))
    app.testHelperSMSearch.find_in_container_number(11, 0, 0)
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smKontrol)
            app.testHelperSMSearch.find_in_container_number(11, 0, 0)
            tr = tr + 1
    #первый параметр (номер строки, если 0 - случайный выбор), второй номер колонки в таблице
    s = app.testHelperSMSearch.get_one_table_parametr(0, 2)
    #app.testhelpersm.click_on_zakazschik_link_in_result_tab(s[1])
    app.session.open_href_page(s[0])
    s2 = app.testHelperSMSearch.compare_company_name()
    assert s[2] == s2[0]
    assert s[2] == s2[1]
    #Найти наименование заказчика, публикации, поставщика, стоимость заказчика, стоимость поставщика, период
    #кликнуть по ссылке заказчик
    # дождаться открытия ссылки в новом окне
    #проверить совпадения полей наименование заказчика из результатов - наименование компании


def test_sm_link_smKontrol_Postavchik(app):
    exp_result = "Торги и контракты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smKontrol)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    # Искать в контейнере (всего контейнеров + 1, номер контейнера(если 0 - случайный выбор), номер строки
    # в контейнере (если 0 - случайный выбор))
    app.testHelperSMSearch.find_in_container_number(11, 7, 0)
    if app.testHelperSMSearch.check_results() == '0':
        tr = 1
        while app.testHelperSMSearch.check_results() == '0' and tr < 20:
            app.session.open_SM_page(app.smKontrol)
            app.testHelperSMSearch.find_in_container_number(11, 0, 0)
            tr = tr + 1
    #первый параметр (номер строки, если 0 - случайный выбор), второй номер колонки в таблице
    s = app.testHelperSMSearch.get_one_table_parametr(0, 5)
    #app.testhelpersm.click_on_zakazschik_link_in_result_tab(s[1])
    app.session.open_href_page(s[0])
    s2 = app.testHelperSMSearch.compare_company_name()
    assert s[2] == s2[0]
    assert s[2] == s2[1]