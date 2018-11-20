

def test_marker_participation_report_user(app):
    app.session.open_marker_page(app.participation)
    #app.wait_page_load2(60)
    app.session.ensure_login_marker(app.username, app.password)
    #app.wait_page_load2(60)
    app.session.open_marker_page(app.participation)
    app.wait_page_load2(60)
    cd2 = app.current_date_time()
    app.testhelper.create_participation_report_user()
    #app.banner_link_button_marker(20)
    app.session.open_marker_page(app.reports)
    app.testhelper.refresh_page()
    exp_rep_name = "Отчет по закупкам в работе"
    exp_rep_type = "Участие"
    s = app.testhelper.report_is_present_participation()
    assert s[0] == exp_rep_name
    assert s[1] == exp_rep_type
    #assert app.testhelper.report_is_present_date(cd2) == True


def test_marker_participation_report_group(app):
    app.session.open_marker_page(app.participation)
    #app.wait_page_load2(60)
    app.session.ensure_login_marker(app.username, app.password)
    #app.wait_page_load2(60)
    app.session.open_marker_page(app.participation)
    app.wait_page_load2(60)
    cd2 = app.current_date_time()
    app.testhelper.create_participation_report_group()
    #app.banner_link_button_marker(20)
    app.session.open_marker_page(app.reports)
    app.testhelper.refresh_page()
    exp_rep_name = "Отчет по закупкам группы в работе"
    exp_rep_type = "Группа - участие"
    s = app.testhelper.report_is_present_participation()
    assert s[0] == exp_rep_name
    assert s[1] == exp_rep_type


