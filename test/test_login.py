

def test_login(app):
    app.session.get_logged_user()