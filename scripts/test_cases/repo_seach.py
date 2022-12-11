from scripts.common_util.constants import *
import functools
def decorate(method):
    @functools.wraps(method)
    def wrapper(self):
        logger.info('\n')
        logger.info("*****************************************************************************")
        logger.info("Starting the test case " + str(method.__qualname__) )
        logger.info("*****************************************************************************")
        result = method(self)
        logger.info("*****************************************************************************")
        logger.info("Finished the test case " + str(method.__qualname__))
        logger.info("*****************************************************************************")
        logger.info("\n")
        return result
    return wrapper

class SimplisticTest(unittest.TestCase):
    @decorate
    def test(self):
        obj = UI_HELPER()
        obj.searchtext = 'flyoverthings'
        obj.verify_total_query_data()


# 1 : check the initial fresh page ( nodata found, search is empty, rowpage is 10 , page cout is 0)
class test_initial_launch_page(unittest.TestCase):
    @decorate
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
    @decorate
    def test(self):
        for value in [10, 25, 50]:
            with self.subTest(i=value,msg="getAll"):
                obj = UI_HELPER()
                obj.drop_down_value = value
                obj.verify_drop_down_repo_search()


# # 3 : check for the total number of data for selected query [0,1, > 2k]
class test_toatl_query_data(unittest.TestCase):
    @decorate
    def test(self):
        for value in ["testNanHere", "flyoverthings", "testingrepo", ]:
            with self.subTest(i=value,msg="getAll"):
                obj = UI_HELPER()
                obj.searchtext = value
                obj.verify_total_query_data()


# 4 : verify the row data i.e ( name, owner, number of stars, link) 
class test_row_data(unittest.TestCase):
    @decorate
    def test(self):
        for value in ["testNanHere", "flyoverthings", "testingrepo", ]:
            with self.subTest(i=value,msg="getAll"):
                obj = UI_HELPER()
                obj.searchtext = value
                obj.drop_down_value = 10
                obj.compute_repo_api_json = True
                obj.verify_row_data()


# 5 : verify the repo details i.e ( last 3 commits, fork, fork bio)
class test_repo_details_data(unittest.TestCase):
    @decorate
    def test(self):
        for value in ['test']:
            with self.subTest(i=value,msg="getAll"):
                obj = UI_HELPER()
                obj.searchtext = value
                obj.drop_down_value = 10
                obj.compute_repo_details_api_json = True
                obj.verify_repo_details_data()


# 6 : verify the next button +  make sure the count matches
class test_next_prev_button(unittest.TestCase):
    @decorate
    def test(self):
        for value in [10, 25, 50]:
            with self.subTest(i=value,msg="getAll"):
                obj = UI_HELPER()
                obj.searchtext = 'testing1234'
                obj.drop_down_value = value
                obj.compute_repo_api_json = True
                obj.verify_next_prev_button()


# 7 : scenario based i.e initial 10 rows refresh there shd be 10 rows
class test_drop_down_after_refresh(unittest.TestCase):
    @decorate
    def test(self):
        obj = UI_HELPER()
        obj.searchtext = 'testing1234'
        obj.drop_down_value = 10
        obj.verify_drop_down_after_refresh()


# 8 : scenario based i.e initial 10 , select 25 > search for test , the number of rows shd be 25
class test_search_after_drop_down(unittest.TestCase):
    @decorate
    def test(self):
        obj = UI_HELPER()
        obj.searchtext = 'testing'
        obj.drop_down_value = 25
        obj.verify_search_after_drop_down()

# 9 : false negative case making sure the framework is working
# 10 : scroll down and select 10th repo details
class test_whole_table_repo_details_data(unittest.TestCase):
    @decorate
    def test(self):
        for value in [10,]:# not including 50 and 25 due to rate limit ( 25 also might fail )
            with self.subTest(i=value,msg="getAll"):
                obj = UI_HELPER()
                obj.searchtext = 'google'
                obj.drop_down_value = value
                obj.compute_repo_details_api_json = True
                obj.verify_whole_table_repo_details_data()

# 11 : verify the tool tip ( checking if we can hover over tooltip )
class test_whole_table_repo_details_tooltip(unittest.TestCase):
    @decorate
    def test(self):
        obj = UI_HELPER()
        obj.searchtext = "flyoverthings"
        obj.verify_whole_table_repo_details_tooltip()