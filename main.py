from simple_term_menu import TerminalMenu
from quote import quote_a_property

def closing_cost_estimator():
    print('this is the closing cost estimatory')

def interest_rate_spread():
    print('this is the interest rate spread')

def main():
    options = [
        '1. Quote a property',
        '2. Closing Cost Estimator',
        '3. Interest Rate Spread'
    ]

    menu = TerminalMenu(options)
    menu_index = menu.show()

    if menu_index == 0:
        return quote_a_property()
    
    elif menu_index == 1:
        return closing_cost_estimator()
    
    elif menu_index == 2:
        return interest_rate_spread()

    #print(f"You have selected {options[menu_index]}")

if __name__ == "__main__":
    main()