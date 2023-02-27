#!/usr/bin/env python
# coding: utf-8

# In[9]:

# In[1]:
import shipment as sp

a = -4
b = -1
print('Welcome to O-R-GROWERS!')
print('----------------------')
print('Our app provides users with information about:\n* Weather\n* Loan\n* Subsidy\n* Price\n* Fertilizer\n* Shipping')
print('----------------------')
while a < 0:
    choice = input('Please type: Weather or Loan or Subsidy or Price or Fertilizer or Shipping to continue or type Quit (First letter is uppercase!) ')
    if choice == 'Weather':
        import Final_weather as w
        while b < 0:
            cont = input('Are you interested in other information about Loan, Subsidy, Price, or Fertilizer? Please type Y or N ' )
            print('---------------------------------------------------------')
            if cont == 'Y':
                a = -1
                print('********----********')
                b = 1
            elif cont == 'N':
                print('Thank you!')
                a = 1
                b = 1
            else:
                print('Please type Y or N')
                a = -1
                b = -1
        b = -2
            
    elif choice == 'Subsidy':
        import Final_subsidy as s
        while b < 0:
            cont = input('Are you interested in other information about Weather, Loan, Price, or Fertilizer? Please type Y or N ' )
            print('---------------------------------------------------------')
            if cont == 'Y':
                a = -1
                print('********----********')
                b = 1
            elif cont == 'N':
                print('Thank you!')
                a = 1
                b = 1
            else:
                print('Please type Y or N')
                a = -1
                b = -1
        b = -2        
    elif choice == 'Loan':
        import Final_loan as l
        while b < 0:
            cont = input('Are you interested in other information about Weather, Subsidy, Price, or Fertilizer? Please type Y or N ' )
            print('---------------------------------------------------------')
            if cont == 'Y':
                a = -1
                print('********----********')
                b = 1
            elif cont == 'N':
                print('Thank you!')
                a = 1
                b = 1
            else:
                print('Please type Y or N')
                a = -1
                b = -1
        b = -2        
    elif choice == 'Fertilizer':
        import Final_fertilizer as f
        while b < 0:
            cont = input('Are you interested in other information about Weather, Loan, Subsidy, or Price? Please type Y or N ' ) 
            print('---------------------------------------------------------')
            if cont == 'Y':
                a = -1
                print('********----********')
                b = 1
            elif cont == 'N':
                print('Thank you!')
                a = 1
                b = 1
            else:
                print('Please type Y or N')
                a = -1
                b = -1
        b = -2    
    elif choice == 'Price':
        import Final_price as p
        while b < 0:
            cont = input('Are you interested in other information abour Weather, Loan, Subsidy, or Fertilizer? Please type Y or N ' )
            print('---------------------------------------------------------')
            if cont == 'Y':
                a = -1
                print('********----********')
                b = 1
            elif cont == 'N':
                print('Thank you!')
                a = 1
                b = 1
            else:
                print('Please type Y or N')
                a = -1
                b = -1
        b = -2
    elif choice == 'Shipping':
        print_sub_menu = True
        shipment = sp.Shipment()
        subMenu = shipment.display_sub_menu()
        table = ''
        while print_sub_menu:
            print(subMenu)
            sub_selection = int(input())
            if sub_selection == 1:
                shipment.set_address(to_address=False)
                continue

            elif sub_selection == 2:
                shipment.set_address(to_address=True)
                continue

            elif sub_selection == 3:
                shipment.set_parcel()
                continue

            elif sub_selection == 4:
                try:
                    shipment.create_shipment()
                except Exception as e:
                    print(e)
                continue

            elif sub_selection == 5:
                shipment.export()
                continue

            elif sub_selection == 6:
                print_sub_menu = False
            else:
                print("Please give a valid selection")
                continue
    else:
        pass
        a = 2
        print('Thank you!')


# In[ ]:




