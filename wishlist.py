def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

print_colored("Welcome to the Christmas Wish List!", "92")

wish_list=[]

def add_to_wish_list():
    item=input("Enter your wish: ")
    wish_list.append(item)
    print_colored("Wish added!", "93")

def view_wish_list():
    if not wish_list:
        print_colored("Your wish list is empty. Add something","91")
    else:
        print_colored("Your wish List: ","98")
        for item in wish_list:
            print_colored(f"-{item}", "94")

while True:
    print_colored("\nChoose an action: ", "95")
    print_colored("1. Add a wish ", "92")
    print_colored("2. View my wish list", "92")
    print_colored("3. Exit", "92")
    choice=input("Enter the number of your choice: ")

    if choice=='1':
        add_to_wish_list()
    elif choice=='2':
        view_wish_list()
    elif choice=='3':
        print_colored("Goodbye!Merry Christmas!", "92")
        break
    else:
        print_colored("Invalid choice, please try again", "91")
    


