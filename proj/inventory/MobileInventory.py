
class MobileInventory:
    def __init__(self,inventory=None):
        if(not isinstance(inventory,dict)):
            raise TypeError ('Input inventory must be a dictionary')
        if inventory==None:
            self.balance_inventory={}
        else:
            for the_key, the_value in inventory.items():
                if(not isinstance(the_key,str)):
                    raise ValueError('Mobile model name must be a string')
                if(the_value<0):
                    raise ValueError('No. of mobiles must be a positive integer')
            self.balance_inventory = inventory

    def add_stock(self,new_stock):
        if (not isinstance(new_stock, dict)):
            raise TypeError('Input stock must be a dictionary')

        for the_key, the_value in new_stock.items():
            if (not isinstance(the_key, str)):
                raise ValueError('Mobile model name must be a string')
            if (the_value < 0):
                raise ValueError('No. of mobiles must be a positive integer')
            self.balance_inventory[the_key]=the_value

    def sell_stock(self,requested_stock):
        if (not isinstance(requested_stock, dict)):
            raise TypeError('Input stock must be a dictionary')

        for the_key, the_value in requested_stock.items():
            if (not isinstance(the_key, str)):
                raise ValueError('Mobile model name must be a string')
            if (the_value < 0):
                raise ValueError('No. of mobiles must be a positive integer')
            if the_key in self.balance_inventory:
                if self.balance_inventory[the_key]>=the_value:
                    self.balance_inventory[the_key]=self.balance_inventory[the_key]-the_value
                else:
                    raise InsufficientException('Insufficient Stock')
            else:
                raise InsufficientException('No Stock. New Model Request')


