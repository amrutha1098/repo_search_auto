from scripts.common_util.constants import *


class BROWSER_HELPER:

    def __init__(self):
        pass

    def invoker_browser(self):
        #  add code to disable cache , history , extentions ...
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument('window-size=2560,1440')
        self.driver = webdriver.Chrome(executable_path=webdriver_path, chrome_options=options)

    def get_url(self, url):
        self.driver.get(url)

    """
    Code to set elements or select elements in ui
    """

    def search_text(self, name):
        time.sleep(5)
        button_xpath = "//button[contains (@class , 'MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1dpd72z-MuiButtonBase-root-MuiIconButton-root')]"
        search_icon = self.driver.find_element(By.XPATH, value=button_xpath)
        search_icon.click()

        search_text = self.driver.find_element('xpath', '//input[contains(@placeholder, "Search")]')
        # search_text = search_text[0]
        search_text.send_keys(Keys.CONTROL, "a")
        search_text.send_keys(Keys.BACKSPACE)
        search_text.send_keys(name)
        search_text.send_keys(Keys.ENTER)

        time.sleep(5)
        # replace with wait for page to load ..

    def select_drop_down(self, value):
        drop_down_xpath = "//*[text()='" + str(
            "Rows per page:") + "']" + "/following::*[contains(@class, 'MuiTablePagination-select MuiSelect-select MuiSelect-standard MuiInputBase-input css-194a1fa-MuiSelect-select-MuiInputBase-input')]"
        drop_down = self.driver.find_element(By.XPATH, value=drop_down_xpath)
        drop_down.click()

        time.sleep(5)
        # replace with wait for page to load ..

        drop_down_value_xpath = "//li[contains(@class, 'MuiMenuItem-root MuiMenuItem-gutters MuiButtonBase-root MuiTablePagination-menuItem css-qcv4r-MuiButtonBase-root-MuiMenuItem-root-MuiTablePagination-menuItem')" + " and text()='" + str(
            value) + "']"
        drop_down = self.driver.find_element(By.XPATH, value=drop_down_value_xpath)
        drop_down.click()

        time.sleep(5)
        # replace with wait for page to load ..

    def select_next_prev_button(self, value):
        button_xpath = "//button[contains(@class , 'MuiButtonBase-root MuiIconButton-root MuiIconButton-colorInherit MuiIconButton-sizeMedium css-1hgjne-MuiButtonBase-root-MuiIconButton-root')"

        if value == 'next':
            button_xpath = button_xpath + " and contains(@title, 'Go to next page')]"
        else:
            button_xpath = button_xpath + " and contains(@title, 'Go to previous page')]"

        button = self.driver.find_element(By.XPATH, value=button_xpath)
        button.click()

        time.sleep(5)
        # replace with wait for page to load ..

    def select_get_details(self, table_index=0):
        #  need to check for scroll like ( rows grtrr than 9 is not visible)

        button_xpath = "//span[contains(@class,'MuiButtonBase-root MuiIconButton-root MuiIconButton-colorPrimary MuiIconButton-sizeMedium css-1ek9g0z-MuiButtonBase-root-MuiIconButton-root')"
        button_xpath = button_xpath + "and contains(@tabindex, '0')]"

        button_array = self.driver.find_elements(By.XPATH, value=button_xpath)
        button = button_array[table_index]
        button.click()

        time.sleep(5)
        # replace with wait for page to load ..

    def select_close_tab(self):
        button_xpath = "//button[contains(@class,'MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-8g0vn4-MuiButtonBase-root-MuiIconButton-root')]"

        button = self.driver.find_element(By.XPATH, value=button_xpath)
        button.click()

        time.sleep(5)
        # replace with wait for page to load .. 
    
    def select_accept_tab(self):
        button_xpath = "//button[contains(@class,'MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root  css-1q7oytv-MuiButtonBase-root-MuiButton-root')]"

        button = self.driver.find_element(By.XPATH, value=button_xpath)
        button.click()

        time.sleep(5)
        # replace with wait for page to load ..  


    """
    Code to fetch values from ui
    """

    def fetch_table_headers(self):
        table_data = []
        table_path = "//th[contains(@class, 'MuiTableCell-root MuiTableCell-head MuiTableCell-alignLeft MuiTableCell-sizeMedium css-gm1hpc-MuiTableCell-root')]"
        table = self.driver.find_elements(By.XPATH, table_path)

        cell = 0
        while cell < len(table):
            data = {}
            for i in range(4):
                data['name'] = table[cell].text
                data['owner'] = table[cell + 1].text
                data['stars'] = table[cell + 2].text
                data['link'] = table[cell + 3].text
                data['details'] = table[cell + 4].text
            table_data.append(data)
            cell += 5
        print(table_data)
        return table_data

    def get_initial_text(self):
        xpath = "//div[contains(@class, 'MuiGrid-root MuiGrid-container css-1ry2eeo-MuiGrid-root')]"
        element = self.driver.find_element(By.XPATH, xpath)
        # print(element.text)
        return element.text

    def fetch_name_from_table(self, table_index=0):
        table_data = []

        table_path = "//td[contains(@class, 'MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft MuiTableCell-sizeMedium css-xrc9mx-MuiTableCell-root')]"
        table = self.driver.find_elements(By.XPATH, table_path)
        # print(len(table))
        cell = 0
        while cell < len(table):
            data = {}
            for i in range(4):
                data['name'] = table[cell].text
                data['owner'] = table[cell + 1].text
                data['stars'] = table[cell + 2].text
                data['link'] = table[cell + 3].text
                # data['extra'] = table[cell+4].text
            cell += 5
            table_data.append(data)
        print(table_data)
        return table_data

    def fetch_number_page_details(self):
        xpath = "//p[contains(@class, 'MuiTablePagination-displayedRows css-11ceysh-MuiTablePagination-displayedRows')]"
        element = self.driver.find_element(By.XPATH, xpath)
        # print(element.text)
        return element.text

    def fetch_repo_details(self, identifier):
        details_path = "//div[contains(@class, 'MuiGrid-root css-vj1n65-MuiGrid-root')]"
        identity_path = "/following::*[(text()='" + str(identifier) +"')]/../following-sibling::p"
        xpath = details_path + identity_path
        # print(xpath)
        details = self.driver.find_element(By.XPATH, xpath)
        return details.text

    def fetch_commit_fork_details(self, value):
        
        self.select_get_details(value)
        
        data = {}
        data["commit_details"] = self.fetch_repo_details(identifier = "Last 3 committers: ")
        data["fork_details"] = self.fetch_repo_details(identifier="Recent Forked User: ")
        data["fork_bio_details"] = self.fetch_repo_details(identifier="Recent Forked User Bio: ")
        # print(data)

        self.select_accept_tab()

        return data

    def fetch_drop_down_details(self):
        drop_down_xpath = "//*[text()='" + str(
            "Rows per page:") + "']" + "/following::*[contains(@class, 'MuiTablePagination-select MuiSelect-select MuiSelect-standard MuiInputBase-input css-194a1fa-MuiSelect-select-MuiInputBase-input')]"
        drop_down = self.driver.find_element(By.XPATH, value=drop_down_xpath)

        # print(drop_down.text)
        return drop_down.text
        
    """
    does page has certain elements
    """
