


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def Marker_login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("button.mainbtn").click()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector("button.navbar-btn.mainbtn").click()

    def Marker_logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.headernav__uname").click()
        wd.find_element_by_link_text("Выйти из системы").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.Marker_logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector("img.headernav__icon.notifyico")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.headernav__uname").click()
        wd.find_element_by_link_text("Личный кабинет").click()

        return wd.find_element_by_xpath("//ng-component/main/ng-component/div/div[2]/div/div[1]/div[1]/div/div[2]/span").text[10:-0]

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.Marker_logout()
        self.Marker_login(username, password)

