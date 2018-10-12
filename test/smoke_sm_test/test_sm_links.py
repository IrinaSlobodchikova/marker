
#def test_link(app):
#    smParticipants = app.smParticipants
#    smParticipantsCustomers = app.smParticipantsCustomers
#    smParticipantsSuppliers = app.smParticipantsSuppliers
#    smPurchases = app.smPurchases
#    smPrices = app.smPrices
#    smCertificates = app.smCertificates
#    smLicences = app.smLicences
#    smKontrol = app.smKontrol
#    smreports = app.smreports
#    smMonitorinds = app.smMonitorinds
#    smcompany_list = app.smcompany_list
#    smPurchases_list = app.smPurchases_list
#    smNmckList = app.smNmckList
#    smUser_History = app.smUser_History
#    for i in list[smParticipants, smParticipantsCustomers, smParticipantsSuppliers, smPurchases, smPrices, smCertificates,
#                  smLicences, smKontrol, smreports,
#             smMonitorinds, smcompany_list, smPurchases_list, smNmckList, smUser_History]:
#        if i == "smParticipants":
#            exp_result = "Деятельность компании"
#            test_sm_link_smParticipants(app, i, exp_result)
#        elif i == "smParticipantsCustomers":
#            exp_result = "Заказчики"
#            test_sm_link_smParticipants(app, i, exp_result)
#        elif i == smParticipantsSuppliers:
#            exp_result = "Поставщики"
#            test_sm_link_smParticipants(app, i, exp_result)
#        elif i == smPurchases:
#            exp_result = "Торги и контракты"
#            test_sm_link_smParticipants(app, i, exp_result)
#        elif i == smPrices:
#            exp_result = "Цены контрактов"
#            test_sm_link_smParticipants(app, i, exp_result)
#        elif i == smCertificates:
#            exp_result = "Сертификаты"
#            test_sm_link_smParticipants(app, i, exp_result)
#        elif i == smLicences:
#            exp_result = "Лицензии"
#            test_sm_link_smParticipants(app, i, exp_result)
#        elif i == smKontrol:
#            exp_result = "Контроль"
#            test_sm_link_smParticipants(app, i, exp_result)






def test_sm_link_smParticipants(app):
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipants)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipants)
    exp_result = "Деятельность компании"
    assert (app.testhelpersm.ensure_link_work() == exp_result)

def test_sm_link_smParticipantsCustomers(app):
    exp_result = "Заказчики"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsCustomers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsCustomers)
    assert (app.testhelpersm.ensure_link_work() == exp_result)

def test_sm_link_smParticipantsSuppliers(app):
    exp_result = "Поставщики"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smParticipantsSuppliers)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smParticipantsSuppliers)
    assert (app.testhelpersm.ensure_link_work() == exp_result)

def test_sm_link_smPurchases(app):
    exp_result = "Торги и контракты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPurchases)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases)
    assert (app.testhelpersm.ensure_link_work() == exp_result)

def test_sm_link_smPrices(app):
    exp_result = "Цены контрактов"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smPrices)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPrices)
    assert (app.testhelpersm.ensure_link_work() == exp_result)

def test_sm_link_smCertificates(app):
    exp_result = "Сертификаты"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smCertificates)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smCertificates)
    assert (app.testhelpersm.ensure_link_work() == exp_result)

def test_sm_link_smLicences(app):
    exp_result = "Лицензии"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smLicences)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smLicences)
    assert (app.testhelpersm.ensure_link_work() == exp_result)

def test_sm_link_smKontrol(app):
    exp_result = "Контроль"
    app.session.open_SM_page(app.smKontrol)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smKontrol)
    assert (app.testhelpersm.ensure_link_work() == exp_result)

#другие линки
def test_sm_link_smreports(app):
    exp_result = "Отчетов:"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smreports)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smreports)
    assert (app.testhelpersm.ensure_link_type2_work() == exp_result)

def test_sm_link_smMonitorinds(app):
    exp_result = "Сохранен"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smMonitorinds)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smMonitorinds)
    assert (app.testhelpersm.ensure_link_type2_work() == exp_result)

def test_sm_link_smcompany_list(app):
    exp_result = "Списки к"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smcompany_list)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smcompany_list)
    assert (app.testhelpersm.ensure_link_type2_work() == exp_result)

def test_sm_link_smPurchases_list(app):
    exp_result = "Списки т"
    app.session.open_SM_page(app.smPurchases_list)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smPurchases_list)
    assert (app.testhelpersm.ensure_link_type2_work() == exp_result)

def test_sm_link_smNmckList(app):
    exp_result = "Обоснова"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smNmckList)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smNmckList)
    assert (app.testhelpersm.ensure_link_type2_work() == exp_result)

def test_sm_link_smUser_History(app):
    exp_result = "История"
    app.testhelpersm.refresh_page()
    app.session.open_SM_page(app.smUser_History)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smUser_History)
    assert (app.testhelpersm.ensure_link_type2_work() == exp_result)