

def test_marker_new_report(app):
    app.session.open_marker_page(app.newtenders)
    #app.wait_page_load2(60)
    app.session.ensure_login_marker(app.username, app.password)
    #app.wait_page_load2(60)
    app.session.open_marker_page(app.newtenders)
    app.wait_page_load2(60)
    cd2 = app.current_date_time()
    app.testhelper.create_new_report()
    #app.banner_link_button_marker(20)
    app.session.open_marker_page(app.reports)
    app.testhelper.refresh_page()
    exp_rep_name = "Отчет по новым закупкам"
    exp_rep_type = "Новые закупки"
    s = app.testhelper.report_is_present_new()
    assert s[0] == exp_rep_name
    assert s[1] == exp_rep_type
    #assert app.testhelper.report_is_present_date(cd2) == True



