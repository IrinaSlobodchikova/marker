

def test_sm_create_contact_list(app):
    username = app.username
    password = app.password
    smParticipants = app.smParticipants
    smreports = app.smreports
    i = "Перейти в списки компаний"
    app.session.ensure_login_sm(username, password)
    app.session.ensure_login_sm(username, password)
    app.session.open_SM_page(smParticipants)
    app.testhelpersm.find_region2()
    app.testhelpersm.check_results()
    #app.testhelpersm.get_old_contact_list()
    cd2 = app.current_date_time().strftime('%d.%m.%Y %H:%M')
    #app.testhelpersm.create_contact_list_10000(cd2)
    app.testhelpersm.create_contact_list_50(cd2)
    app.banner_link_button(30, i)
    assert(app.testhelpersm.contact_list_is_present(cd2) == True)
    #app.testhelpersm.get_link()


#def test_sm_delete_contact_list(app):
#    username = app.username
#    password = app.password
#    smcompany_list = app.smcompany_list
#    app.session.ensure_login_sm(username, password)
#    app.session.open_SM_page(smcompany_list)
#    app.testhelpersm.delete_first_contact_list()