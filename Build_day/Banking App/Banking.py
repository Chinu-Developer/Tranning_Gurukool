import openpyxl,os,time, uuid
from rich.console import Console
from rich.progress import track
from pyfiglet import figlet_format
from pwinput import pwinput
from datetime import datetime
console = Console()


 # INITILIZATION
file_name = "bank_records_2.xlsx"        #"bank_records_1.xlsx"
bank_name = figlet_format("J BANK",font="slant")

#========================================================
# Progress bar 3 sec 
#========================================================
def Progress_bar(val=1):
     for _ in track(range(val), description="Processing..."):
            time.sleep(1)


#========================================================
# Current Date & Time 
#========================================================
def Cur_date():
     now = datetime.now()
         # Format: YYYY-MM-DD HH:MM:SS
     formatted_1 = now.strftime("%Y-%m-%d %H:%M:%S")
     return formatted_1
     #print("Format 1:", formatted_1)  # Output: 2026-09-05 22:00:00
     





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



#=======================================================
# ERROR MESSAGE
#=======================================================
def Err_msg(error):
    console.print(f" [bold red]Invalid {error} try again [/bold red]")






#========================================================
# Creat Account
#========================================================
def Creat_account():
     console.print("[bold yellow]  Creat Account [/bold yellow]")
     name =   input("Enter Your Name  : ")
     acc_nr = input("Enter Your Account Number : ")

     if not acc_nr.isdigit():
          Err_msg("Account No ")
          return
     if acc_nr == "exist":
          pass


     pin = pwinput("Creat  A 4 DIGIT PIN : ", mask= "*")


     if len(pin) != 4 or not pin.isdigit():
          Err_msg("PIN")
          return



     try:
          amount = float(input("Enter a Opening Balance"))
          if amount < 0 :
               Err_msg("Opening Balance : ")
               return
     except ValueError:
          Err_msg("Value Entered")
          return

     transction_id = str(uuid.uuid4())[:8]
     status = "Opening..."
     dt = Cur_date()



     wb = openpyxl.load_workbook(file_name)
     sheet = wb.active
     sheet.append([acc_nr,name,pin,transction_id,status,amount,0,dt])
     wb.save(file_name)
     wb.close()


     Progress_bar(5)

     console.print("[bold green] Account Created Successfully [/bold green]")





#========================================================
# Check Balance   
#========================================================
def Check_balance(acc_nr):
     wb = openpyxl.load_workbook(file_name)
     sheet = wb.active

     for row in sheet.iter_rows(min_rows=2,values_only=True):
              if(row[0]  == acc_nr):
                   amount = row[7]

     console.print(f"[bold magenda] Your Bank Balance IS [/bold magent]")




     wb.close()





#========================================================
# SUB MENU 
#========================================================
 
def Sub_Menu(acc_nr):
     while True():
          console.print(""" [bold cyan] BANKING OPTIONS
        1. Check Balance
        2. Deposit Money
        3. Withdraw Money
        4. Transaction History
        5. Logout [/bold cyan] 
        """)
          Choice = input("Enter Choice ::")

          if choice == "1":
              Check_balance(acc_nr)
          elif choice =="2":
               pass
          elif choice == "3":
                 pass
          elif choice == "4":
                pass
          elif choice == "5":
                break
          else:
            Err_msg("CHOICE") 


              
               


          






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
        if choice == "1":
            Creat_account()
        if choice == "2":
            pass
        if choice == "3":
            console.print("[bold yellow] Thankyou For Visiting J Banking System , Visit Again  [/ bold yellow]")
            break
        #else:    
       # Err_msg("CHOICE") 