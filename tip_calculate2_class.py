class TipCalculate():
    def __init__(self, cost, split, tip):
        self.cost = cost
        self.split = split
        self.tip = tip
        self.tips = []

    def get_cost(self):
        while True:
            try:
                global cost_num  
                cost_num = float(self.cost)  
                if cost_num > 0:
                    break  
                else:
                    print('Please enter value greater than $0.00.')  
            except ValueError:
                print('You did not enter a valid number, please try again.')  
        return cost_num 


    def get_bill_split(self):
        while True:
            try:
                global split_num
                split_num = int(self.split)
                if split_num > -1:
                    break
                else:
                    print('Please enter a value of 0 or greater.')
            except ValueError:
                print('You did not type a valid number, please try again.')
        return split_num 


    def get_tip(self):
        while True:
            try:
                tip_num = float(self.tip) 
                if tip_num > -1:
                    tip_amount = (tip_num * 0.01)
                    self.tips.append(tip_amount)
                    tip_again = input('Would you like to add another tip? Please enter "yes" or "no".\n')
                    if tip_again == 'yes':
                        self.tip = input('What tip percentage would you like to leave?\n')
                        self.get_tip() 
                    elif tip_again == 'no':
                        break
                    else:
                        while True:
                            try_again = input('That is invalid. Please enter "yes" or "no".\n')
                            if try_again == 'yes':
                                self.get_tip()
                            elif try_again == 'no':
                                break   
                    break                                                         
                else:
                    print('Please enter a value of 0 or greater.')
            except ValueError:
                print('You did not enter a valid number, please try again.')  
        return self.tips


    def bill_total_and_split(self):
        self.get_cost()
        self.get_bill_split()
        self.get_tip()
        tip_total = sum(self.tips)
        cost_post_tax = (cost_num * .10) + cost_num
        global total
        total = (cost_post_tax * tip_total) + cost_post_tax
        print(f'The total of your bill, tip/s and sales tax included, is: ${total:,.2f}')

        split = total 
        try:
            if split_num > 0:
                split = total / split_num 
                print(f'Each person in the party is responsible for: ${split:,.2f}')
        except ZeroDivisionError:
            print('')
      
        return total, split
