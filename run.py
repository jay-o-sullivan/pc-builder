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
    while True:
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")
        try:
            choice = int(input("Select an option: "))
            if 1 <= choice <= len(options):

                return str(choice)
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Function to get valid integer input from the user
def get_valid_integer_input(prompt):
    while True:
        try:
            choice = int(input(prompt))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Function to select a component from a given sheet
def select_component(sheet, component_type):
    # Display available components
    print(f"Available {component_type}s:")
    components = sheet.get_all_records()
    for index, component in enumerate(components, start=1):
        print(f"{index}. {component['Model']} - ${component['Price']}")

    while True:
        try:
            # Get user input
            choice = input(f"Select a {component_type} (enter number): ")

            # Check if user input is not empty
            if choice:
                choice = int(choice) - 1

                # Check if the choice is within valid range
                if 0 <= choice < len(components):
                    selected_component = components[choice]
                    return selected_component
                else:
                    print("Invalid choice. Please select a valid number.")
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Function to display an introduction to the app
def display_introduction():
    type_effect("Welcome to PC Part Picker!")
    type_effect
    ("This application allows you to build your own PC configuration \
      or choose from prebuilt options.")
    type_effect("You can also save your custom "
                "builds and search for them later.")
    type_effect("Let's get started!\n")


def search_build_by_name(sheet, name):
    builds = sheet.get_all_records()
    matching_builds = []

    print(f"Searching for builds with name '{name}'")

    for build in builds:
        if 'Name' in build and 'Configuration' in build and 'Total Price' in build:
            if name.lower() in build['Name'].lower().strip() or name.lower() in build['Configuration'].lower().strip():
                matching_builds.append(build)
                print(f"Match found: {build['Name']} - {build['Configuration']}")

    return matching_builds


def main():
    display_introduction()

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

    user_name = input("Enter your name: ")

    while True:
        type_effect("Choose an option:\n")
        option = display_menu(
            ["Build a PC", "Prebuilt PCs", "Search Builds by Name", "Exit"]
        )
        os.system('clear' if os.name == 'posix' else 'cls')
        print()

        # Build a custom PC configuration
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

            total_price = (
                cpu["Price"] + motherboard["Price"] +
                gpu["Price"] + ram["Price"] + storage["Price"] +
                powersupply["Price"] + case["Price"]
            )

            print(f"Total Price: {total_price}\n")

            publish_build = input(
                "Do you want to publish this build? (yes/no): "
                )
            if publish_build.lower() == "yes":
                # Get the build name from the user
                build_name = input("Enter a name for this build: ")
                # Save as custom build
                builds_sheet.append_row([
                    user_name,
                    build_name,
                    cpu["Model"],
                    motherboard["Model"],
                    gpu["Model"],
                    ram["Model"],
                    storage["Model"],
                    powersupply["Model"],
                    case["Model"],
                    total_price
                ])
                print(f"Build configuration '{build_name}' saved to 'Builds' worksheet.\n")

        elif option == "2":
            while True:
                print("Viewing prebuilt configurations:")
                prebuilt_option = input("Select prebuilt option (1/2): ")
                if prebuilt_option in ["1", "2"]:
                    break
                else:
                    print("Invalid input. Please enter either '1' or '2'.")
            prebuilt_option = int(prebuilt_option)  # Convert to int

            prebuilt_records = prebuilts_sheet.get_all_records()
            matching_prebuilts = []

            for prebuilt in prebuilt_records:
                configuration = prebuilt["Configuration"]
                if prebuilt_option == 1 and "Under $1000" in configuration:
                    matching_prebuilts.append(prebuilt)
                elif prebuilt_option == 2 and "Under $2000" in configuration:
                    matching_prebuilts.append(prebuilt)

            if matching_prebuilts:
                print(f"Matching {'Under $1000' if prebuilt_option == 1 else 'Under $2000'} prebuilt configurations:")
                for idx, prebuilt in enumerate(matching_prebuilts, start=1):
                    print(f"{idx}. Configuration: {prebuilt['Configuration']}")

                selected_idx = get_valid_integer_input("Select a prebuilt configuration (enter number): ") - 1

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
                    print(f"Total Price: {selected_prebuilt['Total Price']}\n")

                    input(
                        "Press Enter to return to the PC configuration selection screen..."
                        )
            else:
                print(f"No matching {'Under $1000' if prebuilt_option == 1 else 'Under $2000'} prebuilt configurations found.\n")

        elif option == "3":
            # Search for builds by name
            search_name = input("Enter the name to search for builds: ")
            matching_builds = search_build_by_name(builds_sheet, search_name)

            if matching_builds:
                # Display only the matching build information
                matching_build = matching_builds[0]
                print("Matching build:")
                print(f"Name: {matching_build['Name']}")
                print(f"Configuration: {matching_build['Configuration']}")
                print(f"Total Price: ${matching_build['Total Price']:.2f}\n")

                # Display the components for the matching build
                components = [
                    "CPU",
                    "Motherboard",
                    "GPU",
                    "RAM",
                    "Storage",
                    "Power Supply",
                    "Case"]
                print("\nComponents:")
                for component in components:
                    if component in matching_build:
                        print(f"{component}: {matching_build[component]}")

                print()  # Print an empty line for spacing
            else:
                print("No matching builds found.\n")

        elif option == "4":
            type_effect("Thank you for using PC Part Picker!\n")
            break

        else:
            print("Invalid selection.\n")


if __name__ == "__main__":
    main()
