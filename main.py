import os
from zabbix_api import ZabbixAPIModule
from time import sleep
from excel_reader import ExcelReader


#
# # group_id = zapi.hostgroup.get({
# #         "output": "extend",
# #         "filter": {
# #             "name": [
# #                 "pcg_idrac"
# #             ]
# #         }
# #     }
# # )
# #
# # print(group_id)
#
#
#
# excel_data_df = pd.read_excel('data_collection.xlsx')
# # clear_data = excel_data_df.fillna("", inplace=True)
# """orient='records'"""
#
# # print(clear_data['host'].values.tolist())
# # print(excel_data_df['host'].values.tolist())
#
# hosts = excel_data_df['host'].values.tolist()
# ip = excel_data_df['ip'].values.tolist()
# site = excel_data_df['Site'].values.tolist()
# country = excel_data_df['Country'].values.tolist()
# bu = excel_data_df['BU'].values.tolist()
#
# "------------------------------------------------------------------------------"
# zapi = ZabbixAPI("http://fdmech900up.pcg.cargill.com/zabbix")
# zapi.login(user="Nikita", password="Winter2022$$")
#
#
# for host in range(len(hosts)):
#     try:
#         host_creation = zapi.host.create(
#             host=hosts[host],
#             interfaces=[{
#                 "type": 2,
#                 "main": 1,
#                 "useip": 1,
#                 "ip": ip[host],
#                 "dns": "",
#                 "port": 161,
#                 "details": {
#                     "version": 2,
#                     "bulk": 1,
#                     "community": "{$SNMP_COMMUNITY}"
#                 }
#             }],
#             groups=[{
#                 "groupid": 70
#             }],
#             tags=[
#                 {
#                     "tag": "BU",
#                     "value": bu[host]
#                 },
#                 {
#                     "tag": "Site",
#                     "value": site[host]
#                 }
#             ]
#         )
#     except:
#         continue

# zabbix_api_module = ZabbixAPIModule()
# excel_reader = ExcelReader()
#
# excel_reader.data_reader()
# zabbix_api_module.bulk_adding(excel_reader.hosts, excel_reader.ip, excel_reader.bu, excel_reader.site)

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


