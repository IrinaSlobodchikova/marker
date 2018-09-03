

#def test_marker_login(app):
#    username = app.username
#    password = app.password
#    app.session.ensure_login_marker(username, password)
#    user = app.session.get_logged_user_marker()
#    assert username == user

def test_marker_login(app):
    username = app.username
    password = app.password
    app.sessionSM.sm_login(username, password)
    user = app.sessionSM.get_logged_user_sm()
    assert username == user
