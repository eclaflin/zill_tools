from simple_term_menu import TerminalMenu

class NavMenu(TerminalMenu):
    
    def __init__(self, options):

        self.go_back = False
        self._menu_entries = options
        
        # simple term menu styling
        self.menu_cursor = "> "
        self.menu_cursor_style = ("fg_red", "bold")
        self.menu_highlight_style = ("bg_red", "fg_yellow")
        self.cycle_cursor=True
        self.clear_screen=True