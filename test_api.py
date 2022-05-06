from collection import User_Collection
import unittest

print(User_Collection)

class TestUser(unittest.TestCase):

    def setUp(self):
        User_Collection.insert_one({"name":"Thomas"})

    def test_get(self):
        # self.assertTrue(self.collection.name)
        self.assertEqual({"name":"Thomas"}, User_Collection.find_one({"name":"Thomas"},{'_id': 0}))

    # def test_post(self):
    #     self.assertTrue(self.voiture_on.etat)
    
    # def test_put(self):
    #     self.assertTrue(self.voiture_on.etat)
    
    # def test_delete(self):
    #     self.assertTrue(self.voiture_on.etat)