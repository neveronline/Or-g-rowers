import shipment as sp

def get_main_menu():
    f = open('./static/menu.txt')
    output = ""
    for line in f:
        output += line
    f.close()
    return output

if __name__ == '__main__':
    loop = True
    menu = get_main_menu()
    while loop:
        print(menu)
        selection = int(input())
        if selection == 1:
            print('weather info')
        elif selection == 2:
            print('Loan Info')
        elif selection == 3:
            print('Fertilizer info')
        elif selection == 4:
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

                if sub_selection == 2:
                    shipment.set_address(to_address=True)
                    continue

                if sub_selection == 3:
                    shipment.set_parcel()
                    continue

                if sub_selection == 4:
                    try:
                        shipment.create_shipment()
                    except Exception as e:
                        print(e)
                    continue

                if sub_selection == 5:
                    shipment.export()
                    continue

                if sub_selection == 6:
                    print_sub_menu = False
                else:
                    print("Please give a valid selection")
                    continue
        elif selection == 5:
            print('Subsidies Info')
        elif selection == 6:
            print('Historical Price Info')
        elif selection == 7:
            print('Bye')
            loop = False
        else:
            print('Not valid selection')



