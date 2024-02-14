from generic.base_file import BaseTest
from generic.utility import Excel
class Test_Script(BaseTest):

    def test_script1(self):
        print(self.driver.title)
        d=Excel.get_data('../data/input.xlsx','Sheet1',1,1)
        print('xl data in test:',d)