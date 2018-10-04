


def test_sm_login(app):
    username = app.username
    password = app.password
    app.session.ensure_login_sm(username, password)
    user = app.session.get_logged_user_sm()
    assert username == user
