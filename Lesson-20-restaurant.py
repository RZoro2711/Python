class Restaurant :
    menu = {
        'pizza' : 5000,
        'cola' : 600,
        'apple juice' : 2000,
        'hamburger' : 1000,
        'fried potato' : 600,
    }

    def __init__(self) :
        self.total = 0
        self.orders = []

    def addOrder(self,order) : 
        self.orders.append(order)
        self.total += self.menu[order]
    
    def printBill(self) : 
        for order in self.orders : 
            print(f'{order} : {self.menu[order]}')
            
        print(f'Total Price : {self.total}')

def start() :
    table = Restaurant()
    while True :
        order = input('Menu : ')
        table.addOrder(order)

        another = input('Order again? Enter y/n : ')
        if another == 'y' or another == 'yes' or another == 'Yes' :
            continue
        if another == 'n' or another == 'no' or another == 'No' :
            table.printBill()
            break

start()
