import pyzabbix
import requests
from pyzabbix import ZabbixAPI
from actions_logger import Logger
import getpass

logger = Logger()


class ZabbixAPIModule:
    def __init__(self):
        self.login = input("Enter username: ")
        self.password = getpass.getpass('Enter password: ', stream=None)
        # login = "Nikita"
        # password = "Winter2022$$"
        self.group_id = 70


    def connection_to_server(self):
        try:
            self.server = ZabbixAPI("http://fdmech900up.pcg.cargill.com/zabbix")
            self.server.login(user=self.login, password=self.password)
            print("Access granted.")
        except pyzabbix.api.ZabbixAPIException as e:
            logger.access_error(e)
            print("Access denied.")
        except requests.exceptions.ConnectionError as e:
            logger.server_reachability_error(e)
            print("Zabbix server is unreachable.")

    def bulk_adding(self, hosts, ip, bu, site):
        for host in range(len(hosts)):
            try:
                host_creation = self.server.host.create(
                    host=hosts[host],
                    interfaces=[{
                        "type": 2,
                        "main": 1,
                        "useip": 1,
                        "ip": ip[host],
                        "dns": "",
                        "port": 161,
                        "details": {
                            "version": 2,
                            "bulk": 1,
                            "community": "{$SNMP_COMMUNITY}"
                        }
                    }],
                    groups=[{
                        "groupid": self.group_id
                    }],
                    tags=[
                        {
                            "tag": "BU",
                            "value": bu[host]
                        },
                        {
                            "tag": "Site",
                            "value": site[host]
                        }
                    ]
                )
                logger.device_was_added(hosts[host])
            except:
                logger.device_was_not_added(hosts[host])
                continue

    def id_group_collector(self):
        group_id = self.server.hostgroup.get({
            "output": "extend",
            "filter": {
                "name": [
                    "pcg_idrac"
                ]
            }
        }
        )

        return group_id
