import ansible_runner
import json

def load_inventory(inventory_path):
    # extract information from hosts.yml and puts it into a string
    response = ansible_runner.interface.get_inventory(action="list", inventories=[inventory_path])
    inventory_str, error_str = response
    inventory_dict = json.loads(inventory_str)  # convert str to dict
    return inventory_dict

def print_hosts_ip_groups(inventory_data):
    #display hosts information such as names, ip and group names

    #first, host names and ip addresses
    hosts = inventory_data["_meta"]["hostvars"]
    print("--- Host names and their IP addresses ---\n")
    for host in hosts:
        ip_address = hosts[host]["ansible_host"]
        print(f"The IP adress of {host} is {ip_address}")

    #group names
    groups = inventory_data["all"]["children"]
    print("\n--- Hosts and the groups they belong to ---\n")
    for group in groups:
        hosts_in_group = inventory_data[group]["hosts"]
        print(f"Hosts belonging to {group}:")

        for host in hosts_in_group:
            print(f"{host}")

def ping_hosts():
    #ping the hosts and output the results 

    ansible_command = "ansible all:localhost -m ping"
    response, error_str, return_code = ansible_runner.interface.run_command(executable_cmd=ansible_command) 
    print(f"--- Response of pinging all hosts ---\n {response}")

def main():
    inventory_data = load_inventory("./hosts.yml") 
    print_hosts_ip_groups(inventory_data)
    ping_hosts()

if __name__ == "__main__":
    main()
