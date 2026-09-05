import openpyxl
import os
from rich.console import Console
from pyfiglet import figlet_format
console = Console()


 # INITILIZATION
file_name = "bank_records_2.xlsx"        #"bank_records_1.xlsx"
bank_name = figlet_format("J BANK",font="slant")




#========================================================
#  Excel Creation Function 
#========================================================



def Create_excel_file():
    """ This is a function which help us to creat new excel file named bank_records_2 If it does not exist """
    if not os.path.exists(file_name):
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = "Bank RecordS"
        headers = ["Account No","Name","PIN","Transaction ID","Transaction Type","Amount",
                  "Previous Balance","Current Balance","Date-Time"]

        sheet.append(headers)


        # for i in range(1,10):
                #     sheet.cell(row=2, column=i).value = "abc"
                # # sheet["A1"].value = ""
                # sheet["B1"].value = ""


        wb.save(file_name)
        wb.close()
        console.print("[bold blue]Excel Data Base Created Succcessfully [/bold blue]")
     #  console.print("[bold cyan]Excel database Created Successfully [/bold cyan]")



#========================================================
#   MAIN PROGRAM
#========================================================


if __name__ == "__main__":
    Create_excel_file()
    while True:
        console.print( f"[cyan] {bank_name} [/cyan]")
        print()
        console.print("[bold green] Welcome to J banking system [/bold green]")
      # console.print("[bold cyan] Welcome to Python Banking System [/bold cyan]")
        print("""1. Create Account
2. Login
3. Exit""") 
        print()
        choice = console.input("[bold purple]Enter Your Choice :: [/bold purple] ")
        if choice == "3":
            console.print("[yellow]Thankyou for Visting J bank [/yellow]")  
            break      