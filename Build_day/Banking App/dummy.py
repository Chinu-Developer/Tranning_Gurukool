# import os

# var = os.path.exists(r"C:\Users\Sanky\Desktop\training_Python_batch1\Build_day\Banking App\bank_record.xlsx")

# print(var)




# if not (1 == 1): #if not (True) #if False
#     print("ok")
# else:
#     print("NOk")


from rich.console import Console 


console = Console()

console.print(" [bold yellow]Login Successful [/bold yellow]" )

console.print("[bold  blue ]Login Successful[/bold blue]")
console.print("[cyan]Current Balance: ₹10000[/cyan]")



from pyfiglet import figlet_format
bank_name = figlet_format("Joshi BANK", font="slant") 
console.print( f"[blue] {bank_name} [/blue]")

import emoji

print(emoji.emojize(":bank:"))
print(emoji.emojize(":credit_card:"))
print(emoji.emojize(":money_bag:"))
print(emoji.emojize(":dollar:"))