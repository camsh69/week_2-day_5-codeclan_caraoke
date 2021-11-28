class BarTab:
    
    def __init__(self, guest, amount):
        self.guest = guest
        self.amount = amount

    def increase_bar_tab(self, amount):
        self.amount += amount