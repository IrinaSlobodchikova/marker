

def test_login(app):
    username = app.username
    password = app.password
    app.session.ensure_login_marker(username, password)
    user = app.session.get_logged_user_marker()
    assert username == user

