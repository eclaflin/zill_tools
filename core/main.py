from simple_term_menu import TerminalMenu
from quote import quote_a_property

def closing_cost_estimator():
    print('this is the closing cost estimatory')

def interest_rate_spread():
    print('this is the interest rate spread')

def main():
    main_menu_title = "  Main Menu.\n  Press Q or Esc to quit. \n"
    main_menu_items = [
        '1. Quote a property',
        '2. Closing Cost Estimator',
        '3. Interest Rate Spread'
    ]
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("bg_red", "fg_yellow")
    main_menu_exit = False

    menu = TerminalMenu(
        menu_entries=main_menu_items,
        title=main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )
    menu_index = menu.show()

    while not main_menu_exit:

        if menu_index == 0:
            main_menu_exit = quote_a_property()
        
        elif menu_index == 1:
            return closing_cost_estimator()
        
        elif menu_index == 2:
            return interest_rate_spread()

    #print(f"You have selected {options[menu_index]}")

if __name__ == "__main__":
    main()