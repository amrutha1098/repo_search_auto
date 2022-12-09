import unittest
import os
import sys

scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)
os.chdir('../../')
sys.path.insert(0, os.path.abspath(os.curdir))

from scripts.common_util.constants import *


# class SimplisticTest(unittest.TestCase):

#     def test(self):
#         # obj = API_OPERATIONS()
#         # expected_data = obj.get_repo_details()

#         ui_obj = BROWSER_HELPER()
#         ui_obj.invoker_browser()
#         ui_obj.get_url("http://localhost:3000/")
#         # ui_obj.fetch_initial_text()
#         ui_obj.search_text("test")
#         ui_obj.select_drop_down(25)
#         ui_obj.select_next_prev_button("next")
#         ui_obj.select_next_prev_button("previous")
#         ui_obj.select_get_details(9)
#         ui_obj.select_close_tab()
#         ui_obj.fetch_rows_data_from_table(7)
#         ui_obj.fetch_table_headers()
#         ui_obj.fetch_number_page_details()
#         ui_obj.fetch_commit_fork_details(1)
#         ui_obj.fetch_drop_down_details()

# # simple case to verify the ui operations 
# class repo_search_smokeTest(unittest.TestCase):
#     def repo_search_smokeTest(self):
#         pass

# 1 : check the initial fresh page ( nodata found, search is empty, rowpage is 10 , page cout is 0)
class test_initial_login_page(unittest.TestCase):
    def test(self):
        obj = UI_HELPER()
        obj.search_text = ''
        obj.page_data = 'No Data Found'
        obj.drop_down_value = 10
        obj.page_split = '0–0 of 0'
        obj.verify_initial_page()


# 2 : check if the drop down is getting selected  + as many rows are present in ui
# ( three sub test 10 : 25 : 50 )
class test_drop_down_values(unittest.TestCase):
    def test(self):
        for value in [10, 25, 50]:
            with self.subTest(i=value):
                obj = UI_HELPER()
                obj.drop_down_value = value
                obj.verify_drop_down_repo_search()


# # 3 : check for the total number of data for selected query [0,1, > 2k]
class test_toatl_query_data(unittest.TestCase):
    def test(self):
        for value in ["testNanHere", "flyoverthings", "testingrepo", ]:
            with self.subTest(i=value):
                obj = UI_HELPER()
                obj.searchtext = value
                obj.verify_total_query_data()


# 4 : verify the row data i.e ( name, owner, number of stars, link) 
class test_row_data(unittest.TestCase):
    def test(self):
        for value in ["testNanHere", "flyoverthings", "testingrepo", ]:
            with self.subTest(i=value):
                obj = UI_HELPER()
                obj.searchtext = value
                obj.drop_down_value = 10
                obj.compute_repo_api_json = True
                obj.verify_row_data()


# 5 : verify the repo details i.e ( last 3 commits, fork, fork bio)
class test_repo_details_data(unittest.TestCase):
    def test(self):
        for value in ["flyoverthings", 'test']:
            with self.subTest(i=value):
                obj = UI_HELPER()
                obj.searchtext = value
                obj.drop_down_value = 10
                obj.compute_repo_details_api_json = True
                obj.verify_repo_details_data()


# 6 : verify the next button +  make sure the count matches
class test_next_prev_button(unittest.TestCase):
    def test(self):
        for value in [10, 25, 50]:
            with self.subTest(i=value):
                obj = UI_HELPER()
                obj.searchtext = 'testing1234'
                obj.drop_down_value = value
                obj.compute_repo_api_json = True
                obj.verify_next_prev_button()


# 7 : senario based i.e initial 10 rows refresh there shd be 10 rows
# 8 : senario based i.e initial 10 , select 25 , search for test , the number of rows shd be 25 
# 9 : false negative case making sure the framework is working 
# 10 : scroll down and select 10th repo details 
# 11 : verify the tool tip

if __name__ == '__main__':
    unittest.main()
