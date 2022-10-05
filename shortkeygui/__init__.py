from uiaction import doubleKey, singleKey

class mainShotcut:

    def file_menu(self=1):
        doubleKey("alt", "f", interval=0.25)
        # File menu options in the current program.

    def edit_option(self=1):
        doubleKey("alt", "e", interval=0.25)
        # Open Edit options in the current program.

    def switch_program(self=1):
        doubleKey("alt", "tab", interval=0.25)
        # Switch between open programs.

    def help(self=1):
        # View help information (F1 is used by almost every Windows program to display help).
        singleKey("f1", interval=0.25)

    def rename(self=1):
        # Rename a selected file.
        singleKey("f2", interval=0.25)

    def refresh(self=1):
        # Refresh the current program window.
        singleKey("f5", interval=0.25)

    def bookmark(self=1):
        # Bookmark the current page in most Internet browsers.
        doubleKey("ctrl", "d", interval=0.25)

    def create_new(self=1):
        # Create a new or blank document in some software, or open a new tab in most Internet browsers.
        doubleKey("ctrl", "n", interval=0.25)

    def open(self=1):
        # Open a file in the current software.
        doubleKey("ctrl", "o", interval=0.25)

    def select_all(self=1):
        # Select all text.
        doubleKey("ctrl", "a", interval=0.25)

    def cut(self=1):
        # Cut selected item.
        doubleKey("ctrl", "x", interval=0.25)

    def copy(self=1):
        # Copy selected item.
        doubleKey("ctrl", "c", interval=0.25)

    def paste(self=1):
        # Paste
        doubleKey("ctrl", "v", interval=0.25)

    def redo(self=1):
        # Redo the last action.
        doubleKey("ctrl", "y", interval=0.25)

    def undo(self=1):
        # Undo the last action.
        doubleKey("ctrl", "z", interval=0.25)

    def insert_hyperlink(self=1):
        # Undo the last action.
        doubleKey("ctrl", "k", interval=0.25)

    def print(self=1):
        # Print the current page or document.
        doubleKey("ctrl", "p", interval=0.25)

    def end(self=1):
        # Go to the end of the current line.
        doubleKey("end", interval=0.25)

    def end_doc(self=1):
        # Go to the end of the document.
        doubleKey("ctrl", "end", interval=0.25)

    def home(self=1):
        # Go to the beginning of the current line.
        doubleKey("home", interval=0.25)

    def home_doc(self=1):
        # Go to the beginning of the document.
        doubleKey("ctrl", "home", interval=0.25)

    def highlight_start(self=1):
        # Highlight from the current position to the beginning of line.
        doubleKey("shift", "home", interval=0.25)

    def highlight_end(self=1):
        # Highlight from the current position to the end of line.
        doubleKey("shift", "end", interval=0.25)

    def word_by_word_left(self=1):
        # Move one word to the left at a time.
        doubleKey('ctrl', 'left', interval=0.25)

    def word_by_word_right(self=1):
        # Move one word to the right at a time.
        doubleKey('ctrl', 'right', interval=0.25)

    def start_menu(self=1):
        # Open the Start menu.
        doubleKey('ctrl', 'esc', interval=0.25)

    def task_manager(self=1):
        # Open Windows Task Manager.
        doubleKey('ctrl', 'shift', 'esc', interval=0.25)

    def close_program(self=1):
        # Open Windows Task Manager.
        doubleKey('alt', 'f4', interval=0.25)

    def properties(self=1):
        # Open the properties for the selected item (file, folder, shortcut, etc.).
        doubleKey('alt', 'enter', interval=0.25)

    def lock(self=1):
        # Lock the computer, requiring password entry to access again.
        doubleKey('win', 'l', interval=0.25)

    def task_menu(self=1):
        # Access the Power User Tasks Menu in Windows 8 and Windows 10.
        doubleKey('win', 'x', interval=0.25)

    def minimize(self=1):
        # Minimize the active program window.
        doubleKey('win', 'pgdn', interval=0.25)

    def maximize(self=1):
        # Minimize the active program window.
        doubleKey('win', 'pgup', interval=0.25)

    def switch_all_program(self=1):
        # Switch between into the current programs.
        doubleKey('alt', 'shift', 'tab', interval=0.25)

    def switch_tab(self=1):
        # Switch between into the current programs.
        doubleKey('ctrl', 'shift', 'tab', interval=0.25)

    def screenshot(self=1):
        # take a screenshot on current display
        doubleKey('alt', 'printscrn', interval=0.25)

    def shutdown_menu(self=1):
        doubleKey('ctrl', 'alt', 'del', interval=0.25)

    def zoom_in(self=1):
        # zoom the current program
        doubleKey('ctrl', '+', interval=0.25)

    def open_settings(self=1):
        # open a settings for current program
        doubleKey('alt', 'enter', interval=0.25)

    def right_click(self=1):
        # click a right mouse button
        doubleKey('shift', 'f10', interval=0.25)

    def delete_permanently(self=1):
        # delete a selected file permanently
        doubleKey('shift', 'del', interval=0.25)

    def delete(self=1):
        # delete a selected file
        singleKey('del', interval=0.25)


    def save(self=1):
        # Saves the open worksheet.
        doubleKey('ctrl', 's', interval=0.25)

    def saveAs(self=1):
        # Save as a open worksheet.
        doubleKey('shift', 'ctrl', 's', interval=0.25)

    def page_Up(self=1):
        # scroll up a current page
        singleKey("pgup", interval=0.25)

    def page_Dn(self=1):
        # scroll down a current page
        singleKey("pgdn", interval=0.25)

    def new_tab(self=1):
        # create a new tab on current program
        doubleKey("ctrl", "t", interval=0.25)
        print("hii")


class msExcel:
    def __init__(self=1):
        PAUSE = 1
        FAILSAFE = True

    def next_cell(self=1):
        # Move to the next cell, to the right of the currently selected cell.
        singleKey("tab", interval=0.25)

    def create_new(self=1):
        # Create a new or blank document in some software, or open a new tab in most Internet browsers.
        doubleKey("ctrl", "n", interval=0.25)

    def open(self=1):
        # Open a file in the current software.
        doubleKey("ctrl", "o", interval=0.25)

    def bold(self=1):
        # Cut selected item.
        doubleKey("ctrl", "b", interval=0.25)

    def select_all(self=1):
        # Select all text.
        doubleKey("ctrl", "a", interval=0.25)

    def search(self=1):
        # Search current sheet.
        doubleKey("ctrl", "f", interval=0.25)

    def go2certain_area(self=1):
        # Go to a certain area.
        doubleKey("ctrl", "g", interval=0.25)

    def italics(self=1):
        # Puts italics on all cells in the highlighted section.
        doubleKey("ctrl", "i", interval=0.25)

    def table_dialogBox(self=1):
        # Puts italics on all cells in the highlighted section.
        doubleKey("ctrl", "l", interval=0.25)

    def find_replace(self=1):
        # Find and replace.
        doubleKey("ctrl", "h", interval=0.25)

    def save(self=1):
        # Saves the open worksheet.
        doubleKey('ctrl', 's', interval=0.25)

    def saveAs(self=1):
        # Save as a open worksheet.
        doubleKey('shift', 'ctrl', 's', interval=0.25)

    def underline(self=1):
        # Underlines all cells in the highlighted section.
        doubleKey('ctrl', 'u', interval=0.25)

    def close(self=1):
        # Closes the current workbook.
        doubleKey('ctrl', 'w', interval=0.25)

    def cut(self=1):
        # Cuts all cells in the highlighted section.
        doubleKey("ctrl", "x", interval=0.25)

    def copy(self=1):
        # Copy selected item.
        doubleKey("ctrl", "c", interval=0.25)

    def paste(self=1):
        # Paste
        doubleKey("ctrl", "v", interval=0.25)

    def redo(self=1):
        # Repeats the last entry (redo).
        doubleKey("ctrl", "y", interval=0.25)

    def undo(self=1):
        # Undo the last action.
        doubleKey("ctrl", "z", interval=0.25)

    def insert_hyperlink(self=1):
        # Undo the last action.
        doubleKey("ctrl", "k", interval=0.25)

    def print(self=1):
        # Print the current page or document.
        doubleKey("ctrl", "p", interval=0.25)

    def end(self=1):
        # Go to the end of the current line.
        singleKey("end", interval=0.25)

    def end_doc(self=1):
        # Go to the end of the document.
        doubleKey("ctrl", "end", interval=0.25)

    def home(self=1):
        # Go to the beginning of the current line.
        singleKey("home", interval=0.25)

    def home_doc(self=1):
        # Go to the beginning of the document.
        doubleKey("ctrl", "home", interval=0.25)

    def highlight_start(self=1):
        # Highlight from the current position to the beginning of line.
        doubleKey("shift", "home", interval=0.25)

    def highlight_end(self=1):
        # Highlight from the current position to the end of line.
        doubleKey("shift", "end", interval=0.25)

    def word_by_word_left(self=1):
        # Move one word to the left at a time.
        doubleKey('ctrl', 'left', interval=0.25)

    def word_by_word_right(self=1):
        # Move one word to the right at a time.
        doubleKey('ctrl', 'right', interval=0.25)

    def changeformate(self=1):
        # Changes the format of the selected cells.
        doubleKey('ctrl', '1', interval=0.25)

    def boldAllcell(self=1):
        # Bolds all cells in the highlighted section.
        doubleKey('ctrl', '2', interval=0.25)

    def italicsAllcell(self=1):
        # Puts italics all cells in the highlighted section.
        doubleKey('ctrl', '3', interval=0.25)

    def underlineAllcell(self=1):
        # Underlines all cells in highlighted section.
        doubleKey('ctrl', '4', interval=0.25)

    def strikethrough(self=1):
        # Puts a strikethrough all cells in the highlighted section.
        doubleKey('ctrl', '5', interval=0.25)

    def showORhide(self=1):
        # Shows or hides objects.
        doubleKey('ctrl', '6', interval=0.25)

    def showORhide_Toolbar(self=1):
        # Shows or hides the toolbar.
        doubleKey('ctrl', '7', interval=0.25)

    def toggle(self=1):
        # Toggles the outline symbols.
        doubleKey('ctrl', '8', interval=0.25)

    def hideRow(self=1):
        # Hides rows.
        doubleKey('ctrl', '9', interval=0.25)

    def hideColumns(self=1):
        # Hides columns.
        doubleKey('ctrl', '0', interval=0.25)

    def currentTime(self=1):
        # Enters the current time.
        doubleKey('ctrl', 'shift', ':', interval=0.25)

    def currentDate(self=1):
        # Enters the current date.
        doubleKey('ctrl', ';', interval=0.25)

    def changeValue_Formula(self=1):
        # Changes between displaying cell values or formulas in the worksheet.
        doubleKey('ctrl', '`', interval=0.25)

    def copyFormula_Cell(self=1):
        # Copies a formula from the cell above.
        doubleKey('ctrl', "'", interval=0.25)

    def copyValue_Cell(self=1):
        # Copies value from cell above.
        doubleKey('ctrl', 'shift', '"', interval=0.25)

    def deleteRowORcolumn(self=1):
        # Deletes the selected column or row.
        doubleKey('ctrl', '-', interval=0.25)

    def insertRowORcolumn(self=1):
        # Inserts a new column or row.
        doubleKey('ctrl', 'shift', '=', interval=0.25)

    def switch_Value(self=1):
        # Switches between showing Excel formulas or their values in cells.
        doubleKey('ctrl', 'shift', '~', interval=0.25)

    def timeFormatting(self=1):
        # Applies time formatting.
        doubleKey('ctrl', 'shift', '@', interval=0.25)

    def commaFormatting(self=1):
        # Applies comma formatting.
        doubleKey('ctrl', 'shift', '!', interval=0.25)

    def currencyFormatting(self=1):
        # Applies currency formatting.
        doubleKey('ctrl', 'shift', '$', interval=0.25)

    def dateFormatting(self=1):
        # Applies date formatting.
        doubleKey('ctrl', 'shift', '#', interval=0.25)

    def percentageFormatting(self=1):
        # Applies percentage formatting.
        doubleKey('ctrl', 'shift', '%', interval=0.25)

    def exponentialFormatting(self=1):
        # Applies exponential formatting.
        doubleKey('ctrl', 'shift', '^', interval=0.25)

    def selectCurrent_region(self=1):
        # Selects the current region around the active cell.
        doubleKey('ctrl', 'shift', '*', interval=0.25)

    def border(self=1):
        # Places border around selected cells.
        doubleKey('ctrl', 'shift', '&', interval=0.25)

    def removeBorder(self=1):
        # Removes a border.
        doubleKey('ctrl', 'shift', '_', interval=0.25)

    def insert(self=1):
        # Insert.
        doubleKey('ctrl', '+', interval=0.25)

    def delete(self=1):
        # Delete contents of the currently-active cell.
        doubleKey('ctrl', '-', interval=0.25)

    def unhideRow(self=1):
        # Unhide rows.
        doubleKey('ctrl', 'shift', '(', interval=0.25)

    def unhideColumn(self=1):
        # Unhide columns.
        doubleKey('ctrl', 'shift', '&', interval=0.25)

    def selectArray(self=1):
        # Selects the array containing the active cell.
        doubleKey('ctrl', '/', interval=0.25)

    def selectCell(self=1):
        # Selects the cells with a static value or don’t match the formula in the active cell.
        doubleKey('ctrl', '\\', interval=0.25)

    def selectColumn(self=1):
        # Selects the entire column.
        doubleKey('ctrl', 'spacebar', interval=0.25)

    def selectWorksheet(self=1):
        # Selects the array containing the active cell.
        doubleKey('ctrl', 'shift', 'spacebar', interval=0.25)

    def moveState(self=1):
        # Move to cell A1.
        doubleKey('ctrl', 'home', interval=0.25)

    def moveLast(self=1):
        # Move to last cell with text on the worksheet.
        doubleKey('ctrl', 'end', interval=0.25)

    def switchExcelFile(self=1):
        # Move between Two or more open Excel files.
        doubleKey('ctrl', 'tab', interval=0.25)

    def switchPervious(self=1):
        # Activates the previous workbook.
        doubleKey('ctrl', 'shift', 'tab', interval=0.25)

    def argumentINTOformula(self=1):
        # Inserts argument names into a formula.
        doubleKey('ctrl', 'shift', '(', interval=0.25)

    def dropDownMenu(self=1):
        # Opens the drop-down menu for fonts.
        doubleKey('ctrl', 'shift', 'f', interval=0.25)

    def dropDownMenu_Pointsize(self=1):
        # Opens the drop-down menu for point size.
        doubleKey('ctrl', 'shift', 'p', interval=0.25)

    def pastesONclipboard(self=1):
        # Pastes what is stored on the clipboard.
        doubleKey('ctrl', 'shift', 'f', interval=0.25)

    def selectLeft(self=1):
        # Highlights all text to the left of the cursor.
        doubleKey('shift', 'home', interval=0.25)

    def selectRight(self=1):
        # Highlights all text to the right of the cursor.
        doubleKey('shift', 'end', interval=0.25)

    def selectTop(self=1):
        # Extends the highlighted area up one cell.
        doubleKey('shift', 'pgup', interval=0.25)

    def selectBottum(self=1):
        # Extends the highlighted area down one cell.
        doubleKey('shift', 'pgdn', interval=0.25)

    def systemMenu(self=1):
        # Opens the system menu.
        doubleKey('alt', 'spacebar', interval=0.25)

    def multipleLine(self=1):
        # While typing text in a cell, singleKeying Alt + Enter moves to the next line, allowing for multiple lines of text in one cell
        doubleKey('alt', 'enter', interval=0.25)

    def sumAllCell(self=1):
        # Creates a formula to sum all of the above cells.
        doubleKey('alt', '=', interval=0.25)

    def help(self=1):
        # Opens the help menu.
        singleKey('f1', interval=0.25)

    def edit(self=1):
        # Edits the selected cell.
        singleKey('f2', interval=0.25)
