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
    type_effect("Welcome to PC Part Picker!\n")


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
    type_effect("Choose an option:\n")
    option = display_menu(["Build a PC", "Prebuilt PCs", "Exit"])
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    if option == "1":
        cpu = select_component(cpu_sheet, "CPU")
        print()
        motherboard = select_component(motherboard_sheet, "Motherboard")
        print()
        gpu = select_component(gpu_sheet, "GPU")
        print()
        ram = select_component(ram_sheet, "RAM")
        print()
        storage = select_component(storage_sheet, "Storage")
        print()
        powersupply = select_component(powersupply_sheet, "PowerSupply")
        print()
        case = select_component(case_sheet, "Case")
        print()

        # Calculate total price of the build
        total_price = cpu["Price"] + motherboard["Price"] + gpu["Price"] + ram["Price"] + storage["Price"] + powersupply["Price"] + case["Price"]
        print(f"Total Price: {total_price}\n")

        builds_sheet.append_row([
            cpu["Model"],
            motherboard["Model"],
            gpu["Model"],
            ram["Model"],
            storage["Model"],
            powersupply["Model"],
            case["Model"],
            total_price
        ])
        print("Build configuration saved to 'Builds' worksheet.\n")   

    elif option == "2":
        prebuilt_option = display_menu(["Under $1000", "Under $2000", "Under $4000"])
        prebuilt_records = prebuilts_sheet.get_all_records()
        matching_prebuilts = []

        for prebuilt in prebuilt_records:
            configuration = prebuilt["Configuration"]
            if prebuilt_option in configuration:
                matching_prebuilts.append(prebuilt)

        if matching_prebuilts:
            print(f"Matching {prebuilt_option} prebuilt configurations:")
            for idx, prebuilt in enumerate(matching_prebuilts, start=1):
                print(f"{idx}. Configuration: {prebuilt['Configuration']}")

            selected_idx = int(input("Select a prebuilt configuration (enter number): ")) - 1

            if 0 <= selected_idx < len(matching_prebuilts):
                selected_prebuilt = matching_prebuilts[selected_idx]
                print(f"Selected Prebuilt Configuration: {selected_prebuilt['Configuration']}")
                print(f"CPU: {selected_prebuilt['CPU Model']}")
                print(f"Motherboard: {selected_prebuilt['Motherboard Model']}")
                print(f"RAM: {selected_prebuilt['RAM Model']}")
                print(f"GPU: {selected_prebuilt['GPU Model']}")
                print(f"Storage: {selected_prebuilt['Storage Model']}")
                print(f"PowerSupply: {selected_prebuilt['PowerSupply Model']}")
                print(f"Case: {selected_prebuilt['Case Model']}")
                print(f"Total Price: {selected_prebuilt['Total Price']}")
        else:
            print("Invalid selection.\n")

    elif option == "4":
        type_effect("Thank you for using PC Part Picker!\n")
        break
