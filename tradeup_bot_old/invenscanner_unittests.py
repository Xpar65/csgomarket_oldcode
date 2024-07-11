#set PYTHONPATH=%PYTHONPATH%;C:\Users\liamc\Desktop\Folders\Projects\CSGO\csgomarket\csgomarket\tradeup_bot\src
import unittest
import json
from unittest.mock import patch
from src.Inventoryscanner import item_viability
from src.Inventoryscanner import setupdesc
from src.Inventoryscanner import deletenonweaponskins
from src.Inventoryscanner import addfloatinfo
from src.Inventoryscanner import API_retrieval
from src.Inventoryscanner import loc_of_skins
from src.Inventoryscanner import minimumfloatskins
from src.Inventoryscanner import tradeup_groupings

def load_json(folder_name, file_name):
    #file_path = f'Unittestfiles/mock_data/{folder_name}/{file_name}'
    file_path = f'C:/Users/liamc/Desktop/Folders/Projects/CSGO/csgomarket/csgomarket/tradeup_bot/Unittestfiles/mock_data/{folder_name}/{file_name}'
    with open(file_path, 'r') as file:
        return json.load(file)

# class TestItemViability(unittest.TestCase):
#     def test_viable_item(self):
#         item = {'type': 'Covert'}
#         self.assertTrue(item_viability(item))

#     def test_non_viable_item(self):
#         item = {'type': 'NonViableType'}
#         self.assertFalse(item_viability(item))


# class Testsetupdesc(unittest.TestCase):
            
#     def test_empty_inv(self):
#         testinventory = load_json('setupdesc_files', 'emptyinv.json')
#         expected_testinventory = load_json('setupdesc_files', 'emptyinv_expected.json')
#         (testinventory)
#         self.assertEqual(testinventory, expected_testinventory)

#     def test_my_inventory(self):
#         testinventory = load_json('setupdesc_files', 'myinventory.json')
#         expected_testinventory = load_json('setupdesc_files', 'myinventory_expected.json')
#         setupdesc(testinventory)
#         self.assertEqual(testinventory, expected_testinventory)

#         #other tests I might oneday do. 
#     def test_full_inventory(self):
#         None

#     def one_type_inventory(self):
#         None

# #maybe there is a better way to set up these unit tests. Less code writing.
# class Testdeletenonweaponskins(unittest.TestCase):
#     def test_my_inventory(self):
#         testinventory = load_json('deletenonweaponskins_files', 'myinventory.json')
#         testinventory_expected = load_json('deletenonweaponskins_files', 'myinventory_expected.json')
#         deletenonweaponskins(testinventory)
#         self.assertEqual(testinventory, testinventory_expected)


# class Testaddfloatinfo(unittest.TestCase):
#     @patch('src.Inventoryscanner.API_retrieval') # this line mocks the retrieval function. 
#     def test_addfloatinfo(self, mock_API_retrieval):
#         # Setup - prepare the data and the mock
#         test_inventory = load_json('addfloatinfo_files','myinventory.json')
#         test_steamID = '123456789'
#         mock_API_retrieval.return_value = ({'floatvalue': 0.123}, None)  # Mock return value

#         # Exercise - call the function
#         error_occurred =  addfloatinfo(test_inventory, test_steamID)

#         # Verify - make assertions
#         self.assertFalse(error_occurred)
#         self.assertIn('floatvalue', test_inventory['descriptions'][0])  # example assertion
#         mock_API_retrieval.assert_called()  # Check if API_retrieval was called


class Testloc_of_skins(unittest.TestCase):
    #here we will test all of the different possible combinations of tradeup possibilities which we can think of in my_inv.
    #tradeup1
    # 
    def setUp(self):
        self.myinventory = load_json('loc_of_skins_files', 'myinventory.json')
        #doublemyinventory = load_json('loc_of_skins_files', 'doublemyinventory.json') #dolater
    
    def testtradeup0(self):
        tradeup = load_json('loc_of_skins_files', 'tradeup0.json')
        tradeup_expected = load_json('loc_of_skins_files', 'tradeup0_expected.json')
        loc_of_skins(self.myinventory, tradeup)
        #print(tradeup)
        self.assertEqual(tradeup, tradeup_expected)
    
    def testtradeup1 (self):
        tradeup = load_json('loc_of_skins_files', 'tradeup1.json')
        tradeup_expected = load_json('loc_of_skins_files', 'tradeup1_expected.json')
        loc_of_skins(self.myinventory, tradeup)
        print(tradeup)
        self.assertEqual(tradeup, tradeup_expected)

class Testminimumfloatskins(unittest.TestCase):
    def non_ST_trade(self):
        None

    def fail_av_float_nonST_trade(self):
        None

    def ST_trade(self):
        None  
    None
    
class Testtradeup_groupings(unittest.TestCase):
    None





if __name__ == '__main__':
    unittest.main()
