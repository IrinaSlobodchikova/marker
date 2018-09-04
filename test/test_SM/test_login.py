


def test_marker_login(app):
    username = app.username
    password = app.password
    app.session.sm_login(username, password)
    user = app.session.get_logged_user_sm()
    assert username == user
