import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        '''能够正常处理santiago chile这样的值'''
        test_data=city_country('santiago','chile')
        self.assertEqual(test_data,'Santiago,Chile')

    def test_city_country_population(self):
        '''能够正常处理santiago chile 5000000这样的值'''
        test_data=city_country('santiago','chile',5000000)
        self.assertEqual(test_data,'Santiago,Chile - population 5000000')

unittest.main()
    