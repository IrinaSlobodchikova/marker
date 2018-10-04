import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def Marker_login(self, username, password):
        wd = self.app.wd
        self.app.open_marker_home_page()
        wd.find_element_by_css_selector("button.mainbtn").click()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").send_keys(username)
        time.sleep(5)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("password").send_keys(password)
        time.sleep(5)
        wd.find_element_by_css_selector("button.navbar-btn.mainbtn").click()

    def Marker_logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.headernav__uname").click()
        wd.find_element_by_link_text("Выйти из системы").click()

    def ensure_Marker_logout(self):
        wd = self.app.wd
        if self.is_logged_in_marker():
            self.Marker_logout()

    def is_logged_in_marker(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector("img.headernav__icon.notifyico")) > 0

    def is_logged_in_as_marker(self, username):
        wd = self.app.wd
        return self.get_logged_user_marker() == username

    def get_logged_user_marker(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.headernav__uname").click()
        wd.find_element_by_link_text("Личный кабинет").click()
        fulltext = wd.find_element_by_xpath("//ng-component/main/ng-component/div/div[2]/div/div[1]/div[1]/div/div[2]/span").text
        return wd.find_element_by_xpath("//ng-component/main/ng-component/div/div[2]/div/div[1]/div[1]/div/div[2]/span").text[11:len(fulltext)]

    def ensure_login_marker(self, username, password):
        wd = self.app.wd
        if self.is_logged_in_marker():
            if self.is_logged_in_as_marker(username):
                return
            else:
                self.Marker_logout()
        self.Marker_login(username, password)


    def sm_login(self, username, password):
        wd = self.app.wd
        self.app.open_sm_home_page()
        wd.find_element_by_css_selector("a.button.login").click()
        #if not self.is_logged_in_sm():
        wd.find_element_by_name("UserName").click()
        wd.find_element_by_name("UserName").clear()
        wd.find_element_by_name("UserName").click()
        wd.find_element_by_name("UserName").send_keys(username)
        time.sleep(5)
        wd.find_element_by_name("Password").click()
        wd.find_element_by_name("Password").clear()
        wd.find_element_by_name("UserName").click()
        wd.find_element_by_name("Password").send_keys(password)
        time.sleep(5)
        wd.find_element_by_xpath("//form[@id='form-login']//button[.='Войти']").click()


    def sm_logout(self):
        wd = self.app.wd
        baseUrlSM = self.app.baseUrlSM
        smlogout = self.app.smlogout
        #wd.maximize_window()
        wd.get(baseUrlSM + smlogout)


    def ensure_logout_sm(self):
        wd = self.app.wd
        if self.is_logged_in_sm():
            self.sm_logout()

    def is_logged_in_sm(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector("span.hdr_user-menu_name")) > 0

    def is_logged_in_as_sm(self, username):
        wd = self.app.wd
        return self.get_logged_user_sm() == username

    def get_logged_user_sm(self):
        wd = self.app.wd
        self.app.wait_smBlock(60)
        text1 = wd.find_element_by_css_selector("span.hdr_user-menu_name").get_attribute("textContent")
        return text1

    def ensure_login_sm(self, username, password):
        wd = self.app.wd
        self.app.wait_smBlock(60)
        if self.is_logged_in_sm():
            if self.is_logged_in_as_sm(username):
                return
            else:
                self.sm_logout()
        self.sm_login(username, password)

    def open_SM_page(self, page):
        wd = self.app.wd
        baseUrlSM = self.app.baseUrlSM
        wd.get(baseUrlSM + page)
        self.app.wait_smBlock(5)

    def is_marker(self):
        try:
            self.app.wd.current_url.startswith(self.app.baseUrlSM)
            return True
        except:
            return False

    def is_sm_blocked(self):
        try:
            text = self.app.wd.find_element_by_id("smBlock").value_of_css_property("display")
            if text == 'block':
             return True
        except:
            return False


    def is_sm_artef_blocked(self):
        try:
            text = self.app.wd.find_element_by_css_selector("div.dlg-content_loader.dlg-content_loader--center").value_of_css_property("display")
            if text == 'block':
             return True
        except:
            return False

