import unittest
import os
import sys

scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)
os.chdir('../../')
sys.path.insert(0, os.path.abspath(os.curdir))

from scripts.common_util.constants import *


class SimplisticTest(unittest.TestCase):

    def test(self):
        # obj = API_OPERATIONS()
        # expected_data = obj.get_repo_details()

        ui_obj = BROWSER_HELPER()
        ui_obj.invoker_browser()
        ui_obj.get_url("http://localhost:3000/")
        # ui_obj.search_text("test")
        # ui_obj.select_drop_down(25)
        # ui_obj.select_next_prev_button("next")
        # ui_obj.select_next_prev_button("previous")
        # ui_obj.select_get_details(9)
        # ui_obj.fetch_name_from_table(7)
        # ui_obj.fetch_table_headers()
        # ui_obj.does_initial_text()
        ui_obj.fetch_page_details()


if __name__ == '__main__':
    unittest.main()
