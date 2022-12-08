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
        print(button_array)
        button = button_array[table_index]
        button.click()

        time.sleep(5)
        # replace with wait for page to load ..

    """
    Code to fetch values from ui
    """
