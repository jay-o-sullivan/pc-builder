import gspread
import time
import os

from google.oauth2.service_account import Credentials


# Function to simulate typing effect
def type_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()


# Function to display a menu and get user input
def display_menu(options):
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
    choice = input("Select an option: ")
    return choice


# Function to select a component from a given sheet
def select_component(sheet, component_type):
    print(f"Available {component_type}s:")
    components = sheet.get_all_records()
    for index, component in enumerate(components, start=1):
        print(f"{index}. {component['Model']} - ${component['Price']}")
    choice = int(input(f"Select a {component_type} (enter number): ")) - 1
    selected_component = components[choice]
    return selected_component


def main():
    type_effect("Welcome to PC Part Picker!")


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)


SHEET = GSPREAD_CLIENT.open('pc_parts')

builds_sheet = SHEET.worksheet("Builds")
prebuilts_sheet = SHEET.worksheet("Prebuilts")
cpu_sheet = SHEET.worksheet("CPU")
motherboard_sheet = SHEET.worksheet("Motherboard")
gpu_sheet = SHEET.worksheet("GPU")
ram_sheet = SHEET.worksheet("RAM")
storage_sheet = SHEET.worksheet("Storage")
powersupply_sheet = SHEET.worksheet("PowerSupply")
case_sheet = SHEET.worksheet("Case")


while True:
    type_effect("Choose an option:")
    option = display_menu(["Build a PC", "Prebuilt PCs", "Exit"])
    os.system('clear' if os.name == 'posix' else 'cls')

    if option == "1":
        cpu = select_component(cpu_sheet, "CPU")
        motherboard = select_component(motherboard_sheet, "Motherboard")
        gpu = select_component(gpu_sheet, "GPU")
        ram = select_component(ram_sheet, "RAM")
        storage = select_component(storage_sheet, "Storage")
        powersupply = select_component(powersupply_sheet, "PowerSupply")
        case = select_component(case_sheet, "Case")

        # Calculate total price of the build
        total_price = cpu["Price"] + motherboard["Price"] + gpu["Price"] + ram["Price"] + storage["Price"] + powersupply["Price"] + case["Price"]
        print(f"Total Price: ${total_price}")

    elif option == "2":
        prebuilt_option = display_menu(["Under $1000", "Under $2000", "Under $4000"])
        prebuilt_records = prebuilts_sheet.get_all_records()
        for prebuilt in prebuilt_records:
            if prebuilt["Configuration"] == prebuilt_option:
                print(f"Prebuilt Configuration: {prebuilt['Configuration']}")
                print(f"CPU: {prebuilt['CPU Model']}")
                print(f"Motherboard: {prebuilt['Motherboard Model']}")
                print(f"RAM: {prebuilt['RAM Model']}")
                print(f"GPU: {prebuilt['GPU Model']}")
                print(f"Storage: {prebuilt['Storage Model']}")
                print(f"PowerSupply: {prebuilt['PowerSupply Model']}")
                print(f"Case: {prebuilt['Case Model']}")
                print(f"Total Price: ${prebuilt['Total Price']}")

    elif option == "3":
        type_effect("Thank you for using PC Part Picker!")
        break


#if __name__ == "__main__":
#    main()
