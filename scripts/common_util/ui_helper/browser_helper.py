from scripts.common_util.constants import *


class BROWSER_HELPER:

    def __init__(self):
        self.wait_due_api_rate_limit = 5
        pass

    def invoker_browser(self):
        #  add code to disable cache , history , extentions ...
        try:
            logger.info("Launching the Chrome browser")
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-extensions')
            options.add_argument('--disable-software-rasterizer')
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("–-disable-dev-shm-usage")
            options.add_argument('window-size=1920x1080')
            capabilities = DesiredCapabilities.CHROME
            capabilities['applicationCacheEnabled'] = False
            self.driver = webdriver.Chrome(executable_path=webdriver_path, chrome_options=options,
                                           desired_capabilities=capabilities)
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Launching the Chrome browser failed")
            assert False,("Launching the Chrome browser failed")

    def close_browser(self):
        try:
            logger.info("Closing the Chrome browser")
            self.driver.close()
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Closing the Chrome browser failed")
            assert False, ("Closing the Chrome browser failed")

    def get_url(self, url):
        try:
            logger.info("Requesting for url : " + str(url))
            self.driver.get(url)
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Requesting for url  failed : " + str(url))

    def refresh_browser(self):
        try:
            logger.info("Refreshing the browser")
            self.driver.refresh()
        except Exception as err:
            logger.error("Error : " + str(err))
            assert False,("Error : " + str(err))

    def wait_for_load_complete(self):
        try:
            logger.info("Wait for the load to be completed")
            wait_time = 0 # wait for 3 minutes
            while wait_time < 180 :
                xpath = "//div[contains(@data-testid , 'bars-loading')]"
                try :
                    self.driver.find_element(By.XPATH, xpath)
                except :
                    logger.info("Wait for page to load 5 second waiting ")
                    time.sleep(self.wait_due_api_rate_limit)
                    wait_time += 5
                    pass
                time.sleep(self.wait_due_api_rate_limit)
                return True
            assert False, "Could not the load the page after 3 minutes"
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("The page could be loaded waited for " + str(wait_time)+ " minutes")
            assert False,("The page could be loaded waited for " + str(wait_time)+ " minutes")
    """
    Code to set elements or select elements in ui
    """

    def search_text(self, name):
        try:
            self.wait_for_load_complete()
            button_xpath = "//button[contains (@class , 'MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1dpd72z-MuiButtonBase-root-MuiIconButton-root')]"
            search_icon = self.driver.find_element(By.XPATH, value=button_xpath)
            search_icon.click()

            search_text = self.driver.find_element('xpath', '//input[contains(@placeholder, "Search")]')
            # search_text = search_text[0]
            search_text.send_keys(Keys.CONTROL, "a")
            search_text.send_keys(Keys.BACKSPACE)
            search_text.send_keys(name)
            search_text.send_keys(Keys.ENTER)

            self.wait_for_load_complete()
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Searching of the text in search box failed : " + str(name))
            assert False,("Searching of the text in search box failed : " + str(name))

    def select_drop_down(self, value):
        try:
            logger.info("Selecting the drop down : " + str(value))
            self.wait_for_load_complete()
            if value == 10:
                self.select_drop_down(25)

            drop_down_xpath = "//*[text()='" + str(
                "Rows per page:") + "']" + "/following::*[contains(@class, 'MuiTablePagination-select MuiSelect-select MuiSelect-standard MuiInputBase-input css-194a1fa-MuiSelect-select-MuiInputBase-input')]"
            logger.info(drop_down_xpath)
            drop_down = self.driver.find_element(By.XPATH, value=drop_down_xpath)
            drop_down.click()

            self.wait_for_load_complete()
            drop_down_value_xpath = "//li[contains(@class, 'MuiMenuItem-root MuiMenuItem-gutters MuiButtonBase-root MuiTablePagination-menuItem css-qcv4r-MuiButtonBase-root-MuiMenuItem-root-MuiTablePagination-menuItem')" + " and text()='" + str(
                value) + "']"
            drop_down = self.driver.find_element(By.XPATH, value=drop_down_value_xpath)
            drop_down.click()

            self.wait_for_load_complete()
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Selecting the drop down : failed " + str(value))
            assert False,("Selecting the drop down : failed " + str(value))

    def select_next_prev_button(self, value):
        try:
            logger.info("Selecting the " + str(value) + " button")
            button_xpath = "//button[contains(@class , 'MuiButtonBase-root MuiIconButton-root MuiIconButton-colorInherit MuiIconButton-sizeMedium css-1hgjne-MuiButtonBase-root-MuiIconButton-root')"

            if value == 'next':
                button_xpath = button_xpath + " and contains(@title, 'Go to next page')]"
            else:
                button_xpath = button_xpath + " and contains(@title, 'Go to previous page')]"

            button = self.driver.find_element(By.XPATH, value=button_xpath)
            button.click()

            self.wait_for_load_complete()
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Selecting the " + str(value) + " button failed ")
            assert False,("Selecting the " + str(value) + " button failed ")

    def select_get_details(self, table_index=0, retry_count = 0):
        try:
            self.wait_for_load_complete()
            logger.info("Cliking on the tool tip to get the repo details ")
            #  need to check for scroll like ( rows grtrr than 9 is not visible)

            button_xpath = "//span[contains(@class,'MuiButtonBase-root MuiIconButton-root MuiIconButton-colorPrimary MuiIconButton-sizeMedium css-1ek9g0z-MuiButtonBase-root-MuiIconButton-root')"
            button_xpath = button_xpath + "and contains(@tabindex, '0')]"

            try :
                button_array = self.driver.find_elements(By.XPATH, value=button_xpath)
                print(len(button_array))
                button = button_array[table_index]
                button.click()
                retry_count += 3
            except:
                if retry_count > 2:
                    assert False
                else:
                    time.sleep(self.wait_due_api_rate_limit)
                    self.select_get_details(table_index, retry_count)


            self.wait_for_load_complete()
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Failed tp Clik on the tool tip to get the repo details " + str(table_index) + " th row")
            assert False,("Failed tp Clik on the tool tip to get the repo details " + str(table_index) + " th row")

    def select_close_tab(self):
        try:
            logger.info("Closing the modal window")
            button_xpath = "//button[contains(@class,'MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-8g0vn4-MuiButtonBase-root-MuiIconButton-root')]"

            button = self.driver.find_element(By.XPATH, value=button_xpath)
            button.click()

            self.wait_for_load_complete()
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Failed closing the modal window")
            assert False,("Failed closing the modal window")

    def select_accept_tab(self):
        try:
            logger.info("Clicking on the OK button in window")
            button_xpath = "//button[contains(@class,'MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root  css-1q7oytv-MuiButtonBase-root-MuiButton-root')]"

            button = self.driver.find_element(By.XPATH, value=button_xpath)
            button.click()

            self.wait_for_load_complete()
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Failed to clic on the OK button in window")
            assert False,("Failed to clic on the OK button in window")

    """
    Code to fetch values from ui
    """

    def fetch_table_headers(self):
        try:
            logger.info("Fetch the table headers or the column names of the table")
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
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Failed to fetch the table headers or the column names of the table")
            assert False,("Failed to fetch the table headers or the column names of the table")

    def fetch_initial_text(self):
        try:
            logger.info("Fetch the data of the page , after the launch of the page")
            xpath = "//div[contains(@class, 'MuiGrid-root MuiGrid-container css-1ry2eeo-MuiGrid-root')]"
            element = self.driver.find_element(By.XPATH, xpath)
            # print(element.text)
            return element.text
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Failed to fetch the data of the page , after the launch of the page")
            assert False,("Failed to fetch the data of the page , after the launch of the page")

    def fetch_rows_data_from_table(self, table_index=0):
        try:
            logger.info("Fetch the data of each row in the table")
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
            # print(table_data)
            return table_data
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Failed to fetch the data of each row in the table")
            assert False,("Failed to fetch the data of each row in the table")

    def fetch_number_page_details(self):
        try:
            logger.info("Fetch the page details written in footer")
            xpath = "//p[contains(@class, 'MuiTablePagination-displayedRows css-11ceysh-MuiTablePagination-displayedRows')]"
            element = self.driver.find_element(By.XPATH, xpath)
            # print(element.text)
            return element.text
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Fetch the page details written in footer")
            assert False,("Fetch the page details written in footer")

    def fetch_repo_details(self, identifier):
        try:
            logger.info("Fetch the repo details from the modal window of " + str(identifier))
            details_path = "//div[contains(@class, 'MuiGrid-root css-vj1n65-MuiGrid-root')]"
            identity_path = "/following::*[(text()='" + str(identifier) + "')]/../following-sibling::p"
            xpath = details_path + identity_path
            # print(xpath)
            details = self.driver.find_element(By.XPATH, xpath)
            return details.text
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Failed to fetch the repo details from the modal window of " + str(identifier))
            assert False,("Failed to fetch the repo details from the modal window of " + str(identifier))

    def fetch_commit_fork_details(self, value):
        try:
            logger.info("Fetch the repo details from the modal window of the row " + str(value))
            print(value)
            self.select_get_details(value)

            data = {}
            data["commit_details"] = self.fetch_repo_details(identifier="Last 3 committers: ")
            data["fork_details"] = self.fetch_repo_details(identifier="Recent Forked User: ")
            data["fork_bio_details"] = self.fetch_repo_details(identifier="Recent Forked User Bio: ")

            self.select_accept_tab()

            return data
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Failed to fetch the repo details from the modal window of the row " + str(value))
            assert False,("Failed to fetch the repo details from the modal window of the row " + str(value))

    def fetch_drop_down_details(self):
        try:
            logger.info("Fetching the drop down value")
            drop_down_xpath = "//*[text()='" + str(
                "Rows per page:") + "']" + "/following::*[contains(@class, 'MuiTablePagination-select MuiSelect-select MuiSelect-standard MuiInputBase-input css-194a1fa-MuiSelect-select-MuiInputBase-input')]"
            drop_down = self.driver.find_element(By.XPATH, value=drop_down_xpath)

            # print(drop_down.text)
            return drop_down.text
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Failed to fetch the drop down value")
            assert False,("Failed to fetch the drop down value")

    def fetch_search_text_details(self):
        try:
            logger.info("Fetch the the string in the search box")
            search_text = self.driver.find_element('xpath', '//input[contains(@placeholder, "Search")]')

            # print(drop_down.text)
            return search_text.text
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Failed to fetch the the string in the search box")
            assert False,("Failed to fetch the the string in the search box")

    def fetch_tooltip_detail(self):
        try:
            logger.info("Fetch the tootip detail")
            tool_tip = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'MuiButtonBase-root MuiIconButton-root MuiIconButton-colorPrimary MuiIconButton-sizeMedium css-1ek9g0z-MuiButtonBase-root-MuiIconButton-root')]")))
            hov = ActionChains(self.driver).move_to_element(tool_tip)
            return True
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Failed to fetch the tootip detail")
            assert False,("Failed to fetch the tootip detail")
    """
    does page has certain elements
    """
