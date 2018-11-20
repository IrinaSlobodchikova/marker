

def test_marker_login(app):
    username = app.username
    password = app.password
    app.session.open_marker_page(app.newtenders)
    app.session.ensure_login_marker(username, password)
    user = app.session.get_logged_user_marker()
    assert username == user


