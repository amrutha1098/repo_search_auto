import os
import sys

scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)
os.chdir('../../')
sys.path.insert(0, os.path.abspath(os.curdir))

from scripts.test_cases.repo_seach import *

def run_some_tests():
    # Run only the tests in the specified classes

    test_classes_to_run = [
        # SimplisticTest,
        test_initial_launch_page,
        test_drop_down_values,
        test_toatl_query_data,
        test_row_data,
        test_repo_details_data,
        test_next_prev_button,
        test_drop_down_after_refresh,
        test_search_after_drop_down,
        test_whole_table_repo_details_data,
        test_whole_table_repo_details_tooltip,
    ]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)
    return big_suite

    # ...


if __name__ == '__main__':
    import HtmlTestRunner

    runner = HtmlTestRunner.HTMLTestRunner(
        # resultclass=NumbersTestResult,
        combine_reports=True,
        report_name="MyReport",
        add_timestamp=False
    )
    big_suite = run_some_tests()
    results = runner.run(big_suite)
    print(results)