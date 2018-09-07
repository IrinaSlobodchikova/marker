

def test_search_by_number(app):
    username = app.username
    password = app.password
    baseURL = app.baseUrlMarker
    app.session.ensure_login_marker(username, password)
    app.testhelper.get_page()
    app.testhelper.send_number_of_tender()
    app.testhelper.select_first()



