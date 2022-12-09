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
        # test_drop_down_values,
        # test_toatl_query_data,
        # test_row_data,
        # test_repo_details_data,
        # test_next_prev_button,
    ]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
    print(results)
    # ...


if __name__ == '__main__':
    run_some_tests()