import ansible_runner
import requests

def run_playbook(playbook_path):
    #command to run the playbook and output results
    command = f"ansible-playbook {playbook_path}"
    response, error_str, return_code = ansible_runner.interface.run_command(executable_cmd=command)
    print(f"--- Output of running the playbook ---\n {response}")
    
if __name__ == "__main__":
    run_playbook("hello.yml")

    #verify the response of the NodeJS servers
    for index in range(1, 4):
        expected_response = f"Hello World from managedhost-app-{index} !"
        response = requests.get('http://0.0.0.0')
        if response.text == expected_response:
            print("Response matches the expected:", response.text)
        else:
            print("Response doesn't match the expected. Expected:", expected_response, "\nActual:", response.text)
