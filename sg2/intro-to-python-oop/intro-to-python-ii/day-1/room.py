class ItemPrinter:
    def __init__(self):
        pass

    def print_contents(self):
        for i in self.storage:
            print(i)
            i.print_contents()


class Room(ItemPrinter):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.storage = []

    def add_item(self, item):
        self.storage.append(item)


class Item(ItemPrinter):
    def __init__(self, name):
        self.name = name
        self.storage = []

    def pick_up(self, item):
        self.storage.append(item)

    def __str__(self):
        return f'My name is {self.name}'


player = Item("Player")
torch = Item("Torch")
player.pick_up(torch)
# player.print_contents()

entryway = Room("Entryway", "The entryway.")
entryway.add_item(player)
entryway.print_contents()

gold = Item("Gold")
bucket = Item("Bucket")
bucket.pick_up(gold)
# Room -> Player -> Bucket -> Gold
player.pick_up(bucket)

player.print_contents()
