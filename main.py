import os
from zabbix_api import ZabbixAPIModule
from time import sleep
from excel_reader import ExcelReader


print("Welcome to the Zabbix data import tool.\n")
print("Please log in to the Zabbix server:")
zabbix_api_module = ZabbixAPIModule()
zabbix_api_module.connection_to_server()
excel_reader = ExcelReader()

print("\nPlease choose the option:\n1 - Get list of the ID for the zabbix groups"
      "\n2 - Change the group ID for the further import\n3 - Starting import\n4 - Exit")
script_execution = 1
user_choice = input("\nPlease choose the option: ")
while script_execution:
    if str(user_choice) == "1" or str(user_choice) == "2" or str(user_choice) == "3":

        if str(user_choice) == "1":
            with open("list of groups IDs.txt", "w") as file:
                file.write(str(zabbix_api_module.id_group_collector()))
            sleep(2)
            osCommandString = "notepad.exe list of groups IDs.txt"
            os.system(osCommandString)
            try:
                open("list of groups IDs")
            except FileNotFoundError:
                user_choice = input("\nPlease choose the option: ")

        elif str(user_choice) == "2":
            try:
                zabbix_api_module.group_id = int(input("Enter the group ID: "))
            except ValueError:
                zabbix_api_module.group_id = int(input("Enter the group ID (number): "))
            print(zabbix_api_module.group_id)
            user_choice = input("\nPlease choose the option: ")

        elif str(user_choice) == "3":
            script_execution = 0
            excel_reader.data_reader()
            zabbix_api_module.bulk_adding(excel_reader.hosts, excel_reader.ip, excel_reader.bu, excel_reader.site)
            print("Import was finished. Check the log file for more information.")
    elif str(user_choice) == "4":
        print("Aloha!")
        script_execution = 0
        break
    else:
        print("Please try again!\n")
        user_choice = input("Please choose the option: ")

input("\nPress ENTER to exit...")


