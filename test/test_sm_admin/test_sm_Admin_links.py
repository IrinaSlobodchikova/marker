
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




def test_sm_link_smAdminUpravlenie(app):
    app.session.open_SM_page(app.smAdminUpravlenie)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smAdminUpravlenie)
    exp_result = "Пользователи"
    assert (app.testhelpersm.ensure_link_work() == exp_result)

def test_sm_link_smAdminShlyuz(app):
    exp_result = "Пользователи"
    app.session.open_SM_page(app.smAdminShlyuz)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smAdminShlyuz)
    assert (app.testhelpersm.ensure_link_work() == exp_result)

def test_sm_link_smAdminAccessManager(app):
    exp_result = "Пользователи"
    app.session.open_SM_page(app.smAdminAccessManager)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smAdminAccessManager)
    assert (app.testhelpersm.ensure_link_work() == exp_result)

def test_sm_link_smAdminInstructions(app):
    exp_result = "Редактирование инструкций"
    app.session.open_SM_page(app.smAdminInstructions)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smAdminInstructions)
    assert (app.testhelpersm.ensure_link_work() == exp_result)

def test_sm_link_smAdminNotifications(app):
    exp_result = "Редактирование уведомлений"
    app.session.open_SM_page(app.smAdminNotifications)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smAdminNotifications)
    assert (app.testhelpersm.ensure_link_work() == exp_result)

def test_sm_link_smAdminNews(app):
    exp_result = "Редактирование новостей"
    app.session.open_SM_page(app.smAdminNews)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smAdminNews)
    assert (app.testhelpersm.ensure_link_work() == exp_result)

def test_sm_link_smAdminSessions(app):
    exp_result = "Сессии пользователей"
    app.session.open_SM_page(app.smAdminSessions)
    app.session.ensure_login_sm(app.username, app.password)
    app.session.open_SM_page(app.smAdminSessions)
    assert (app.testhelpersm.ensure_link_work() == exp_result)

