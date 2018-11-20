



class testHelperMarker:

    def __init__(self, app):
        self.app = app

    def create_new_report(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//nav[@class='controlsnav']/div[5]/button").click()

    def create_participation_report_user(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//nav[@class='controlsnav']/div[4]/button").click()
        wd.find_element_by_xpath("//div[@class='mat-menu-content']/button[1]").click()

    def create_participation_report_group(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//nav[@class='controlsnav']/div[4]/button").click()
        wd.find_element_by_xpath("//div[@class='mat-menu-content']/button[2]").click()


    def refresh_page(self):
        wd = self.app.wd
        wd.refresh()

    def report_is_present(self):
        wd = self.app.wd
        if not ("Отчет по новым закупкам" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        if not ("Новые закупки" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        if not ("22:00 13 ноября 2018" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")

    def report_is_present_new(self):
        wd = self.app.wd
        rep_name = wd.find_element_by_css_selector("div.ngx-ellipsis-inner").text.rstrip()
        rep_type = wd.find_element_by_css_selector("div.tabledata__tag.bg1").text.rstrip()
        rep_date = wd.find_element_by_css_selector("div.tabledata__date.date-text").text.rstrip()
        return rep_name, rep_type, rep_date

    def report_is_present_participation(self):
        wd = self.app.wd
        rep_name = wd.find_element_by_css_selector("div.ngx-ellipsis-inner").text.rstrip()
        rep_type = wd.find_element_by_css_selector("div.tabledata__tag.bg2").text.rstrip()
        rep_date = wd.find_element_by_css_selector("div.tabledata__date.date-text").text.rstrip()
        return rep_name, rep_type, rep_date

    def create_planned_purchases_report(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//nav[@class='controlsnav']/div[5]/button").click()

    def report_is_present_date(self, cd2):
        wd = self.app.wd
        date = wd.find_element_by_css_selector("div.tabledata__date.date-text").text.rstrip()
        exp_date = cd2[11:15]
        cd2_hour = cd2[11:13]
        cd2_minute = cd2[14:16]
        exp_date2 = cd2_hour + ":" + str(int(cd2_minute) + 1)
        if date[0:5] == exp_date or date == exp_date2:
            return True
        return False