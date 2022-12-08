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
        obj = API_OPERATIONS()
        expected_data = obj.get_repo_details()

        

if __name__ == '__main__':
    unittest.main()