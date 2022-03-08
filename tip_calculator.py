# Asks user for cost of meal.
def get_cost():
    # Setting the while loop to run while True will ensure it keeps looping until condition/s is/are met.
    while True:
        cost = input('How much did your meal/s cost?\n$')
        try:
            # cost_num is made global so it can be used in other functions.
            global cost_num  
            # The user's input is converted from str to float.
            cost_num = float(cost)  
            if cost_num > 0:
                # So long as the input is greater than 0, it will be stored with no issues and the while loop will stop running.
                break  
            else:
                # If the input is less than 0, user will be prompted to re-enter cost.
                print('Please enter value greater than $0.00.')  
        except ValueError:
            # If input is not a number, user will be prompted to enter a valid number.  
            print('You did not enter a valid number, please try again.')  
    return cost_num     
    
get_cost()


# Asks user for number of people splitting the bill.
def get_bill_split():
    while True:
        split = input('How many people are splitting the bill?\n')
        try:
            global split_num
            # The user's input is converted from str to int.
            split_num = int(split)
            if split_num > -1:
                break
            else:
                print('Please enter a value of 0 or greater.')
        except ValueError:
            print('You did not type a valid number, please try again.')
    return split_num

get_bill_split()


# Calculates the tip percentage by multiplying the user's input by 0.01. 
def tip_percentage(num):
    num = num * 0.01
    return num

# Empty array to store tip amounts.
tips = []
# Asks user for tip percentage.
def get_tip():
    while True:
        tip = input('What tip percentage would you like to leave?\n')
        try:
            tip_num = float(tip) 
            if tip_num > -1:
                # tip_amount is declared with the tip_percentage function taking user input as its argument; resulting in a float to use for calculations.
                tip_amount = tip_percentage(tip_num)
                # The tip_amount/s are appended to the empty tips array for storage.
                tips.append(tip_amount)
                tip_again = input('Would you like to add another tip? Please enter "yes" or "no".\n')
                # If the user would like to add another tip, the get_tip function is ran again.
                if tip_again == 'yes':
                    get_tip()
                elif tip_again == 'no':
                    # If user answers "no", while loop will end then total and bill split calculations will be displayed. 
                    break
                else:
                    while True:
                        # If user answers something other than "yes" or "no" to tip_again question, they will be prompted to re-enter a valid answer.
                        try_again = input('That is invalid. Please enter "yes" or "no".\n')
                        if try_again == 'yes':
                            get_tip()
                        elif try_again == 'no':
                            # After user answers "no", program will break the while loop then display total and bill split calculations.
                            break   
                # This break statement will terminate the outer while loop after conditions are met.            
                break                                                         
            else:
                print('Please enter a value of 0 or greater.')
        except ValueError:
            print('You did not enter a valid number, please try again.')  
    return tips 
    
get_tip()
       

# Bill total is calculated and printed in f string.
def bill_total():
    # tip_total is declared with the sum method adding tip amounts in the tips array together; resulting in one tip amount to use for calculations.
    tip_total = sum(tips)
    # cost_post_tax is declared with an operation that multiplies the 10% sales tax to the cost of the meal then adds the result to the cost of the meal
    # to get the cost of the meal post-tax.
    cost_post_tax = (cost_num * .10) + cost_num
    global total
    total = (cost_post_tax * tip_total) + cost_post_tax
    # The ":,.2f" in the f string formats the float to where it'll add comma separaters at the hundreds place/s when necessary and display the decimal to 
    # the second place ... idk the name of the place but it's two places to the right. Example "$00.00"
    print(f'The total of your bill, tip/s and sales tax included, is: ${total:,.2f}')
    return total

bill_total()


# Bill split is calculated and printed in f string.
def bill_split():
    # Split is defined as the total amount from the bill_total function.
    split = total 
    try:
        if split_num > 0:
            # Now, split is defined as the total amount from bill_total divided by the split_num from get_bill_split user input.
            split = total / split_num
            print(f'Each person in the party is responsible for: ${split:,.2f}')
    # If user entered 0 for split_num in get_bill_split function, this exception will resolve the ZeroDivisonError. 
    except ZeroDivisionError:
        print('')
    return split

bill_split()


# Will run program again if user answers "yes".
def run_again():
    run_again = input('Would you like to use this tool again? "Please enter "yes" or "no".\n')
    while True:
        if run_again == 'yes':
            get_cost()
            get_bill_split()
            get_tip()
            bill_total()
            bill_split()
            break
        else:
            break    
           
run_again()


