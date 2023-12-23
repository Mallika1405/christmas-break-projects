import pandas as pd

file_path = 'santas_list.xlsx'
df = pd.read_excel(file_path)
df_dict = df.to_dict('records')

def display_wishes(df_dict):
    print("\nCurrent Wish List:")
    for entry in df_dict:
        # Check if 'Gift' is a list; if not, make it a list
        gifts = entry['Gift'] if isinstance(entry['Gift'], list) else [entry['Gift']]
        print(f"{entry['Name']}: {', '.join(gifts)}")


def add_new_entries(df_dict):
    
    while True:
        name = input("Enter a name (or type exit to finish): ")
        if name.lower() == 'exit':
            break
        gifts = input(f"Enter gifts for {name}(separate with commas if multiple): ")
        gifts = gifts.split(',') # Convert string to list
        if any(entry['Name']==name for entry in df_dict):
            print(f"{name} is already in the list. Choose edit to change their gifts. ")
            continue
        new_row = {'Name': name, 'Gift': gifts}
        df_dict.append(new_row)
    return pd.DataFrame(df_dict)

def edit_wish(df_dict):
    name=input("Enter the name you wish to edit: ")
    for entry in df_dict:
        if entry['Name']==name:
            new_gifts=input(f"Enter new gifts for {name}(separate with commas if multiple): ")
            entry['Gift']=new_gifts.split(',')
            break
        else:
            print(f"No wishes found for {name}.")

def delete_wish(df_dict):
    name=input("Enter the name whose wish you want to delete: ")
    for i, entry in enumerate(df_dict):
        if entry['Name']==name:
            del df_dict[i]
            print(f"Wish for {name} deleted.")
            break
        else:
            print(f"No wishes found for {name}.")

df_dict=df.to_dict('records')

while True:
    print("\nOptions: \n1. Display Wish List \n2. Add New Wish \n3. Edit a Wish \n4. Delete a Wish \n5. Exit")
    choice = input("Enter your choice: ")

    if choice=='1':
        display_wishes(df_dict)
    elif choice=='2':
        add_new_entries(df_dict)
    elif choice=='3':
        edit_wish(df_dict)
    elif choice=='4':
        delete_wish(df_dict)
    elif choice=='5':
        break
    else:
        print("Invalid choice. Please try again")
    
            

df=pd.DataFrame(df_dict)

df.to_excel(file_path, index=False)
    