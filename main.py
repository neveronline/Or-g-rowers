
def get_main_menu():
    f = open("./static/menu.txt")
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
            print('Shipping Cost')
        elif selection == 5:
            print('Subsidies Info')
        elif selection == 6:
            print('Historical Price Info')
        elif selection == 7:
            print('Bye')
            loop = False
        else:
            print('Not valid selection')



