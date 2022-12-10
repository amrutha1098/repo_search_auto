from scripts.common_util.constants import *


class UI_HELPER(API_OPERATIONS, BROWSER_HELPER):

    def __init__(self):
        API_OPERATIONS.__init__(self)
        pass

    def form_json(self):
        try:
            json_data = {

            }

            if hasattr(self, 'search_text'):
                json_data["search_text"] = self.search_text

            if hasattr(self, 'page_data'):
                json_data["page_data"] = self.page_data

            if hasattr(self, 'drop_down_value'):
                json_data["drop_down_value"] = str(self.drop_down_value)

            if hasattr(self, 'page_split'):
                json_data["page_split"] = self.page_split

            if hasattr(self, 'compute_repo_api_json'):
                json_data = self.get_configured_api_details(self.searchtext, self.drop_down_value)

            if hasattr(self, 'compute_repo_details_api_json'):
                json_data = self.get_configured_repo_api_details(self.searchtext, self.drop_down_value, 1)

            return json_data
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Formatting the api json failed")

    def login(self):
        try :
            logger.info("hello checking the logger here ")
            self.invoker_browser()
            self.get_url("http://localhost:3000/")
        except Exception as err:
            logger.error("Error : " + str(err))
            logger.error("Launching the browser failed")

    def fetch_initial_value(self):
        json_data = {}

        json_data['search_text'] = self.fetch_search_text_details()
        json_data['page_data'] = self.fetch_initial_text()
        json_data['drop_down_value'] = self.fetch_drop_down_details()
        json_data['page_split'] = self.fetch_number_page_details()

        return json_data

    def verify_initial_page(self):

        self.login()

        expected_data = self.form_json()
        actual_data = self.fetch_initial_value()

        logger.info("Expected data : " + str(expected_data))
        logger.info("Actual data : " + str(actual_data))
        assert expected_data == actual_data, "Initial page value is not same as expected"

    def verify_drop_down_repo_search(self):

        self.login()

        self.search_text("test")

        expected_data = self.form_json()["drop_down_value"]
        self.select_drop_down(self.drop_down_value)
        
        actual_data = self.fetch_drop_down_details()
        logger.info("Expected data : " + str(expected_data))
        logger.info("Actual data : " + str(actual_data))
        assert expected_data == actual_data, "Drop down value is not configured as expected"

        #  also check if 10 rows are there in ui
        actual_row_data = len(self.fetch_rows_data_from_table())
        logger.info("Expected data : " + str(expected_data))
        logger.info("Actual data : " + str(actual_row_data))
        assert expected_data == str(actual_row_data), "Number of rows are not present as expected in repo search"

    def verify_total_query_data(self):

        self.login()

        self.search_text(self.searchtext)

        expected_data = self.get_repo_details(self.searchtext)["total_count"]
        actual_data = int(self.fetch_number_page_details().split(" ")[2])
        logger.info("Expected data : " + str(expected_data))
        logger.info("Actual data : " + str(actual_data))
        assert expected_data == actual_data, "the total number of enteries is not as expected count"

    def verify_row_data(self):
        self.login()

        self.search_text(self.searchtext)

        expected_data = self.form_json()
        actual_data = self.fetch_rows_data_from_table()

        logger.info("Expected data : " + str(expected_data))
        logger.info("Actual data : " + str(actual_data))
        assert expected_data == actual_data, "the row data is not as expected"

    def verify_repo_details_data(self):
        self.login()

        self.search_text(self.searchtext)

        index = 0  # checking for only first row
        expected_data = self.form_json()[index]
        actual_data = self.fetch_commit_fork_details(index)

        logger.info("Expected data : " + str(expected_data))
        logger.info("Actual data : " + str(actual_data))
        assert expected_data == actual_data, "the row repo details is not as expected"

    def verify_next_prev_button(self):
        self.login()

        self.select_drop_down(self.drop_down_value)
        self.search_text(self.searchtext)

        toatl_row_data = self.get_repo_details(self.searchtext)["total_count"]

        i = 0
        while i < toatl_row_data:
            page_num_detail = self.fetch_number_page_details().split(" ")[0]
            if i + 50 > toatl_row_data:
                expected_data = str(i + 1) + '–' + str(toatl_row_data)
            else:
                expected_data = str(i + 1) + '–' + str(i + self.drop_down_value)
                self.select_next_prev_button('next')
            logger.info("Expected data : " + str(expected_data))
            logger.info("Actual data : " + str(page_num_detail))
            assert expected_data == page_num_detail, "the page num does not match with actual value"

            i += self.drop_down_value

    def verify_drop_down_after_refresh(self, initial_drop_down=None):
        if initial_drop_down == None:
            initial_drop_down = self.drop_down_value
        self.login()
        expected_data = str(initial_drop_down)
        time.sleep(5)
        # replace with wait for page to load ..
        self.refresh_browser()

        actual_data = self.fetch_drop_down_details()
        logger.info("Expected data : " + str(expected_data))
        logger.info("Actual data : " + str(actual_data))
        assert expected_data == actual_data, "Drop down value is not configured as expected"

    def verify_search_after_drop_down(self):
        self.verify_drop_down_after_refresh(10)

        self.select_drop_down(self.drop_down_value)
        self.search_text(self.searchtext)

        expected_data = str(self.drop_down_value)
        actual_data = self.fetch_drop_down_details()
        logger.info("Expected data : " + str(expected_data))
        logger.info("Actual data : " + str(actual_data))
        assert expected_data == actual_data, "Drop down value is not configured as expected"

        #  also check if 10 rows are there in ui
        actual_row_data = len(self.fetch_rows_data_from_table())
        assert expected_data == str(actual_row_data), "Number of rows are not present as expected in repo search"
    def verify_whole_table_repo_details_data(self):
        self.login()

        self.search_text(self.searchtext)
        expected_json = self.form_json()

        actual_json = []
        for index in range(self.drop_down_value):
            actual_data = self.fetch_commit_fork_details(index)
            actual_json.append(actual_data)

        logger.info("Expected data : " + str(expected_json))
        logger.info("Actual data : " + str(actual_json))
        assert expected_json == actual_json, "the row repo details is not as expected"








