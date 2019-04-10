from proj.inventory import  MobileInventory,InsufficientException
import pytest

class TestingInventoryCreation:
    def test_creating_empty_inventory(self):
        mb=MobileInventory()
        if(not isinstance(mb.balance_inventory,dict)):
            pytest.fail('failed test_creating_empty_inventory')
    def test_creating_specified_inventory(self):
        inventory={'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25}
        mb = MobileInventory(inventory)
    def test_creating_inventory_with_list(self):
        inventory =['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z']
        with pytest.raises(TypeError):
            MobileInventory(inventory)
    def test_creating_inventory_with_negative_value(self):
        inventory = {'iPhone Model X':-45, 'Xiaomi Model Y': 200, 'Nokia Model Z':25}
        with pytest.raises(ValueError):
            MobileInventory(inventory)

    def test_creating_inventory_with_numeric_keys(self):
        inventory = {1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'}
        with pytest.raises(ValueError):
            MobileInventory(inventory)
    def test_creating_inventory_with_nonnumeric_values(self):
        inventory = {1: 'iPhone Model X', 2: 'Xiaomi Model Y', 3: 'Nokia Model Z'}
        with pytest.raises(ValueError):
            MobileInventory(inventory)

    def test_add_new_stock_as_dict(self):
        inventory = {1: 'iPhone Model X', 2: 'Xiaomi Model Y', 3: 'Nokia Model Z'}
    def test_add_new_stock_as_list(self):
        inventory = {1: 'iPhone Model X', 2: 'Xiaomi Model Y', 3: 'Nokia Model Z'}
    def test_add_new_stock_with_numeric_keys(self):
        inventory = {1: 'iPhone Model X', 2: 'Xiaomi Model Y', 3: 'Nokia Model Z'}
    def test_add_new_stock_with_nonnumeric_values(self):
        inventory = {1: 'iPhone Model X', 2: 'Xiaomi Model Y', 3: 'Nokia Model Z'}
    def test_add_new_stock_with_float_values(self):
        inventory = {1: 'iPhone Model X', 2: 'Xiaomi Model Y', 3: 'Nokia Model Z'}

    def test_sell_stock_as_dict(self):
        inventory = {1: 'iPhone Model X', 2: 'Xiaomi Model Y', 3: 'Nokia Model Z'}
    def test_sell_stock_as_list(self):
        inventory = {1: 'iPhone Model X', 2: 'Xiaomi Model Y', 3: 'Nokia Model Z'}
    def test_sell_stock_with_numeric_keys(self):
        inventory = {1: 'iPhone Model X', 2: 'Xiaomi Model Y', 3: 'Nokia Model Z'}
    def test_sell_stock_with_nonnumeric_values(self):
        inventory = {1: 'iPhone Model X', 2: 'Xiaomi Model Y', 3: 'Nokia Model Z'}
    def test_sell_stock_with_float_values(self):
        inventory = {1: 'iPhone Model X', 2: 'Xiaomi Model Y', 3: 'Nokia Model Z'}
    def test_sell_stock_of_nonexisting_model(self):
        inventory = {1: 'iPhone Model X', 2: 'Xiaomi Model Y', 3: 'Nokia Model Z'}
    def test_sell_stock_of_insufficient_stock(self):
        inventory = {1: 'iPhone Model X', 2: 'Xiaomi Model Y', 3: 'Nokia Model Z'}




