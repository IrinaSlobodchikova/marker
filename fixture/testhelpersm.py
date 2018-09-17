




class testHelperSM:

    def __init__(self, app):
        self.app = app

    def find_region(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='mCSB_2_container']/ul/li[2]/label")
        wd.find_element_by_xpath("//form[@id='frmSearch']//button[.='Поиск']")

    def find_region2(self):
        wd = self.app.wd
        self.app.wait_smBlock(20)
        wd.find_element_by_xpath("//div[@id='aggregatesPlaceholder']/table/tbody/tr/td[2]/div/div/div[1]/span[2]").click()
        wd.find_element_by_xpath("//div[@id='mCSB_6_container']/div/ul/li[20]/label").click()
        wd.find_element_by_id("aggSearchText").click()
        wd.find_element_by_id("aggSearchText").clear()
        wd.find_element_by_id("aggSearchText").send_keys("ростов")
        wd.find_element_by_id("aggSearch").click()
        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[6]/label").click()
        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[6]/span[3]").click()
        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[6]/label").click()
        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[7]/label").click()
        wd.find_element_by_xpath("//div[@id='mainAggDlgContent']//button[.='Применить фильтр']").click()
        self.app.wait_smBlock(20)
        wd.find_element_by_xpath("//form[@id='frmSearch']//button[.='Поиск']").click()




    def check_results(self):
        if self.results_is_not_null():
            result = self.get_total_results()
            return int(result)
        else:
            return int(0)


    def results_is_not_null(self):
        return int(self.get_total_results()) > 0


    def get_total_results(self):
        wd = self.app.wd
        results = wd.find_element_by_xpath("//div[@class='panel_header']/h2").get_attribute("textContent")
        return wd.find_element_by_xpath("//div[@class='panel_header']/h2").get_attribute("textContent")[12:len(results)]
        #убрать пробелы перевести в инт

    def create_contact_report_all_in_dif_row_tel_mail(self):
        wd = self.app.wd
        wd.maximize_window()
        self.app.wait_smBlock(20)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Контакты']").click()
        #self.app.wait_smBlock(10)
        wd.find_element_by_xpath("//label[@for='cb-3']").click()
        if not wd.find_element_by_id("cb-3").is_selected():
            wd.find_element_by_id("cb-3").click()
        wd.find_element_by_xpath("//div[@id='divReportContactsSettings']//button[.='Сформировать']").click()

    def create_contact_report_allinone_tel_mail(self):
        wd = self.app.wd
        self.app.wait_smBlock(20)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Контакты']").click()
        #self.app.wait_smBlock(5)
        wd.find_element_by_xpath("//label[@for='cb-3']").click()
        if not wd.find_element_by_id("cb-3").is_selected():
            wd.find_element_by_id("cb-3").click()
        #Найти как кликнуть rb-1
        wd.find_element_by_id("rb-1").click()
        wd.find_element_by_xpath("//div[@id='divReportContactsSettings']//button[.='Сформировать']").click()

    def create_contact_report_result(self):
        wd = self.app.wd
        self.app.wait_smBlock(20)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Результаты']").click()
        wd.find_element_by_xpath("//div[@id='divReportSearchResultsSettings']//button[.='Сформировать']").click()

    def create_contact_report_statictic(self):
        wd = self.app.wd
        #добавить выбор чекбоксов
        self.app.wait_smBlock(20)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Статистика']").click()
        wd.find_element_by_xpath("//div[@id='divReportStatisticsSettings']//button[.='Сформировать']").click()

    def create_contact_list(self):
        wd = self.app.wd
        self.app.wait_smBlock(20)
        wd.find_element_by_xpath("//li[@id='UpdateList']//p[.='Добавить']").click()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").click()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").clear()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").send_keys("список компаний123")
        wd.find_element_by_xpath("//div[@id='addOrUpdateEntitiesListSearchDlg']//button[.='Сохранить']").click()

    def report_is_present(self):
        pass

    def contact_from_contact_rep_is_present(self):
        wd = self.app.wd
        pass