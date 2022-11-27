import random
import Items

def random_item():
    return random.choice(random.choice(Items.items_list))

class LootChest():
    def __init__(self):
        self.items = [random_item(), random_item(), random_item()]





