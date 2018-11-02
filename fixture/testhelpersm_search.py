import re
#import datetime
from random import randrange
import time
from fixture.testhelpersm import testHelperSM


class testHelperSMSearch:

    def __init__(self, app):
        self.app = app


    def find_region(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='mCSB_2_container']/ul/li[2]/label")
        wd.find_element_by_xpath("//form[@id='frmSearch']//button[.='Поиск']")

    def find_region2(self, reg_name):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        wd.find_element_by_xpath("//div[@id='aggregatesPlaceholder']/table/tbody/tr/td[2]/div/div/div[1]/span[2]").click()
        wd.find_element_by_xpath("//div[@id='mCSB_6_container']/div/ul/li[20]/label").click()
        wd.find_element_by_id("aggSearchText").click()
        wd.find_element_by_id("aggSearchText").clear()
        wd.find_element_by_id("aggSearchText").send_keys("%s" % reg_name)
        wd.find_element_by_id("aggSearch").click()
        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[6]/label").click()
        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[6]/span[3]").click()
        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[6]/label").click()
        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[7]/label").click()
        wd.find_element_by_xpath("//div[@id='mainAggDlgContent']//button[.='Применить фильтр']").click()
        self.app.wait_smBlock(600)
        self.press_search_button()


    def find_region3(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        i = randrange(24)
        wd.find_element_by_xpath("//div[@id='aggregatesPlaceholder']/table/tbody/tr[2]/td[1]/div/div/div[1]/span[2]").click()
        self.app.wait_sm_artefact_Block(10)
        if i > 0:
            #element = wd.find_element_by_xpath("//div[@id='mCSB_11_container']/div/ul/li[%s]/label" % i)
            #ActionChains(wd).move_to_element(element).perform()
            wd.find_element_by_xpath("//div[@id='mCSB_11_container']/div/ul/li[%s]/label" % i).click()
        else:
            i = 2
            wd.find_element_by_xpath("//div[@id='mCSB_11_container']/div/ul/li[%s]/label" % i).click()
        wd.find_element_by_xpath("//div[@id='mainAggDlgContent']//button[.='Применить фильтр']").click()
        self.app.wait_smBlock(20)
        self.press_search_button()

    def find_in_container_number(self, range_container_numbers, container_number, i):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        spicok = []
        if i == 0:
            i = randrange(1, 4, 1)
        else:
            i = i
        if container_number == 0:
            ct = randrange(1, range_container_numbers, 1)
        else:
            ct = container_number
        self.expand_show_hide()
        if i > 0 and ct > 0:
            if ct == 1:
                if i < 3:
                    wd.find_element_by_xpath("//div[@id='mCSB_1_container']/ul/li[%s]/label" % str(i)).click()
                if i == 3:
                    i = 2
                    wd.find_element_by_xpath("//div[@id='mCSB_1_container']/ul/li[%s]/label" % str(i)).click()
            elif ct == 2:
                try:
                    wd.find_element_by_xpath("//div[@id='mCSB_2_container']/ul/li[%s]/label" % str(i)).click()
                except:
                    wd.find_element_by_xpath("//div[@id='mCSB_1_container']/ul/li[%s]/label" % str(i)).click()
            elif ct == 3:
                wd.find_element_by_xpath("//div[@id='mCSB_3_container']/ul/li[%s]/label" % str(i)).click()
            elif ct == 4:
                wd.find_element_by_xpath("//div[@id='mCSB_4_container']/ul/li[%s]/label" % str(i)).click()
            elif ct == 5:
                wd.find_element_by_xpath("//div[@id='mCSB_5_container']/ul/li[%s]/label" % str(i)).click()
            elif ct == 6:
                wd.find_element_by_xpath("//div[@id='mCSB_6_container']/ul/li[%s]/label" % str(i)).click()
            elif ct == 7:
                    wd.find_element_by_xpath("//div[@id='mCSB_7_container']/ul/li[%s]/label" % str(i)).click()
            elif ct == 8:
                    wd.find_element_by_xpath("//div[@id='mCSB_8_container']/ul/li[%s]/label" % str(i)).click()
            elif ct == 9:
                    wd.find_element_by_xpath("//div[@id='mCSB_9_container']/ul/li[%s]/label" % str(i)).click()
            elif ct == 10:
                    wd.find_element_by_xpath("//div[@id='mCSB_10_container']/ul/li[%s]/label" % str(i)).click()
        else:
            i = 2
            wd.find_element_by_xpath("//div[@id='mCSB_2_container']/ul/li[%s]/label" % str(i)).click()
        self.press_search_button()
        return i, ct

    def expand_show_hide(self):
        wd = self.app.wd
        if not self.is_sm_advSearch_is_displayed():
            if len(wd.find_elements_by_xpath("//div[@class='block-label']//a[.='Показать/скрыть']")) < 2:
                wd.find_element_by_xpath("//div[@class='block-label']//a[.='Показать/скрыть']").click()
            else:
                wd.find_element_by_xpath("//div[@id='advSearch']/div[2]/a").click()

    def press_search_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form[@id='frmSearch']//button[.='Поиск']").click()

    def is_sm_advSearch_is_displayed(self):
        try:
            text = self.app.wd.find_element_by_id("advSearchContent").value_of_css_property("display")
            if text == 'block':
             return True
        except:
            return False

    def find_zakazchik_for_purchases_list(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        i = randrange(24)
        wd.find_element_by_xpath(
            "//div[@id='aggregatesPlaceholder']/table/tbody/tr[1]/td[3]/div[2]/div/div[1]/span[2]").click()
        self.app.wait_sm_artefact_Block(10)
        wd.find_element_by_id("aggSearchText").click()
        wd.find_element_by_id("aggSearchText").clear()
        wd.find_element_by_id("aggSearchText").send_keys("администрация")
        wd.find_element_by_id("aggSearch").click()
        self.app.wait_sm_artefact_Block(10)
        if i > 0:
            wd.find_element_by_xpath("//div[@id='mCSB_12_container']/div/ul/li[%s]/label" % i).click()
        else:
            i = 2
            wd.find_element_by_xpath("//div[@id='mCSB_12_container']/div/ul/li[%s]/label" % i).click()
        wd.find_element_by_xpath("//div[@id='mainAggDlgContent']//button[.='Применить фильтр']").click()
        self.app.wait_smBlock(600)
        self.press_search_button()


# ! not work
    def search_in_opened_container(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        self.expand_show_hide()
        i = randrange(1, 24, 1)
        c = len(wd.find_elements_by_css_selector("span.agg-widget_btn"))
        ct = randrange(c)
        wd.find_elements_by_css_selector("span.agg-widget_btn")[ct].click()
        self.app.wait_sm_artefact_Block(10)
        #найти как кликнуть на элементе

        wd.find_element_by_xpath("//div[@id='mainAggDlgContent']//button[.='Применить фильтр']").click()
        self.app.wait_smBlock(600)
        self.press_search_button()




    def get_artef_parametrs(self, ct):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        for row in wd.find_elements_by_xpath("//div[@id='mCSB_%s_container']/ul/li[1]" % ct):

            cells = row.find_elements_by_tag_name("span")
            results = cells[0].find_element_by_tag_name("em").text
            try:
                parametr = cells[3].text
            except:
                parametr = cells[2].text
            return parametr


    def get_artef_param(self, ct):
        wd = self.app.wd
        param = self.get_artef_parametrs(ct)
        return param

    def get_table_parametrs(self, i, s):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        for row in wd.find_elements_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[%s]" % i):
            cells = row.find_elements_by_tag_name("td")
            zakazchik_summ, zakazchik, href_zakazchik = self.cell_in_table_res_with_price(cells, s)
            try:
                publication_name = cells[3].find_element_by_tag_name("a").text.rstrip()
            except:
                publication_name = 0
            try:
                href_publication = cells[3].find_element_by_tag_name("a").get_attribute("href")
            except:
                href_publication = 0
            try:
                poctavschik_summ = cells[4].find_element_by_css_selector("p.price").text.rstrip()
            except:
                poctavschik_summ = 0
            try:
                poctavschik = cells[4].find_element_by_tag_name("a").text.rstrip()
            except:
                poctavschik = 0
            try:
                href_poctavschik = cells[4].find_element_by_tag_name("a").get_attribute("href")
            except:
                href_poctavschik = 0
            period = cells[6].text.rstrip()
            return zakazchik_summ, zakazchik, href_zakazchik, publication_name, href_publication, poctavschik_summ, poctavschik, href_poctavschik,  period

    def get_table_parametrs2(self, i):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        for row in wd.find_elements_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[%s]" % i):
            cells = row.find_elements_by_tag_name("td")
            cell1_href, cell1_price, cell1_text = self.cell_in_table_res_with_price(cells, 1)
            cell2_href, cell2_price, cell2_text = self.cell_in_table_res_with_price(cells, 2)
            cell3_href, cell3_price, cell3_text = self.cell_in_table_res_with_price(cells, 3)
            cell4_href, cell4_price, cell4_text = self.cell_in_table_res_with_price(cells, 4)
            cell5_href, cell5_price, cell5_text = self.cell_in_table_res_with_price(cells, 5)
            cell6_href, cell6_price, cell6_text = self.cell_in_table_res_with_price(cells, 6)
            cell7_href, cell7_price, cell7_text = self.cell_in_table_res_with_price(cells, 7)
            return cell1_price, cell1_text, cell1_href, cell2_text, cell2_href, cell3_text, cell3_href, cell4_price, \
                   cell4_text, cell4_href, cell5_text, cell5_href, cell6_text, cell6_href, cell7_text, cell7_href

    def get_one_table_parametr(self, i, s):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        td = 1
        cell1_href = 0
        i2 = 1
        while cell1_href == 0 and td < 40:
            if td <= 20:
                if i == 0:
                 i1 = randrange(51)
                else:
                    i1 = i
                for row in wd.find_elements_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[%s]" % i1):
                    cells = row.find_elements_by_tag_name("td")
                    cell1_href, cell1_price, cell1_text = self.cell_in_table_res_with_price(cells, s)
                    td = td + 1
                    if cell1_href != 0 and td < 20:
                        return cell1_href, cell1_price, cell1_text
            if td > 20 and td < 40:
                for row in wd.find_elements_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[%s]" % i2):
                    cells = row.find_elements_by_tag_name("td")
                    cell1_href, cell1_price, cell1_text = self.cell_in_table_res_with_price(cells, s)
                    td = td + 1
                    i2 = i2 + 1
                    if cell1_href != 0 and td < 20:
                        return cell1_href, cell1_price, cell1_text






    def cell_in_table_res_with_price(self, cells, i):
        try:
            cell1_price = cells[i].find_element_by_css_selector("p.price").text.rstrip()
        except:
            cell1_price = 0
        try:
            cell1_text = cells[i].find_element_by_tag_name("a").text.rstrip()
        except:
            cell1_text = 0
        try:
            cell1_href = cells[i].find_element_by_tag_name("a").get_attribute("href")
        except:
            cell1_href = 0
        return cell1_href, cell1_price, cell1_text

    def get_table_param(self, ct):
        wd = self.app.wd
        param = self.get_table_parametrs(ct)
        return param

    def is_smresult_not_0(self):
        try:
            text = self.get_total_results()
            if text != '0':
             return True
        except:
            return False

    def check_results(self):
        self.app.wait_smBlock(900)
        if self.is_smresult_not_0():
            result = self.get_total_results()
            return result
        else:
            return '0'


    def get_total_results(self):
        wd = self.app.wd
        results = wd.find_element_by_xpath("//div[@class='panel_header']/h2").get_attribute("textContent")
        #clear_result = wd.find_element_by_xpath("//div[@class='panel_header']/h2").get_attribute("textContent")[13:len(results)]
        clear_result = results[13:len(results)]
        return self.clear_result(clear_result)



    def select_all_50(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//label[@for='allItemsCb']").click()
        if not wd.find_element_by_id("allItemsCb").is_selected():
            wd.find_element_by_id("allItemsCb").click()

    def clear_result(self, s):
        x = re.sub(" ", "", str(s))
        return x

    def clear_spase_result(self, s):
        x = re.sub(" ", "", str(s))
        return x


    def ensure_link_work(self):
        wd = self.app.wd
        header = wd.find_element_by_css_selector("h1.clip").text
        return header.rstrip()

    def ensure_link_type2_work(self):
        wd = self.app.wd
        header = wd.find_element_by_css_selector("h2").text
        return header[0:8]


    def compare_company_name(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        current_text_in_header2 = wd.find_element_by_xpath("//div[@class='card-hdr_title']/h1").text.rstrip()
        current_text_in_header = current_text_in_header2[10:len(current_text_in_header2)]
        short_name_text = wd.find_element_by_xpath("//div[@id='main']/div[1]/table/tbody/tr[2]/td[2]").text.rstrip()
        return current_text_in_header, short_name_text

    def compare_lot(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        current_text_in_header2 = wd.find_element_by_xpath("//div[@class='card-hdr_title']/h1").text.rstrip()
        current_text_in_header = current_text_in_header2[10:len(current_text_in_header2)]
        short_name_text = wd.find_element_by_xpath("//div[@id='main']/div[1]/table/tbody/tr[1]/td[2]").text.rstrip()
        period = wd.find_element_by_xpath("//div[@id='main']/div[1]/table/tbody/tr[6]/td[2]").text.rstrip()
        price2 = wd.find_element_by_xpath("//div[@id='main']/div[1]/table/tbody/tr[7]/td[2]").text.rstrip()
        price = price2[4:len(price2)]
        customer = wd.find_element_by_xpath("//div[@id='customersInfo']/div/table/tbody/tr/td[1]/a").text.rstrip()
        customer_price2 = wd.find_element_by_xpath("//div[@id='customersInfo']/div/table/tbody/tr/td[2]/strong").text.rstrip()
        customer_price = customer_price2[4:len(customer_price2)]
        seller = wd.find_element_by_xpath("//div[@id='sellerInfo']/div/table/tbody/tr/td[1]/a").text.rstrip()
        seller_price2 = wd.find_element_by_xpath("//div[@id='sellerInfo']/div/table/tbody/tr/td[2]/strong").text.rstrip()
        seller_price = seller_price2[4:len(seller_price2)]
        return current_text_in_header, short_name_text, period, price, customer, customer_price, seller, seller_price

    def find_company_by_fio(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        wd.find_element_by_id("SearchParams.PersonsSearchParams.FioTextSearch").send_keys("Иванов")



