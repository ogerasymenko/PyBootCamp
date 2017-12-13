import paramiko
from paramiko import client


class Ssh:
    client = None
    def __init__(self):
        print("Connecting to server.")
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy)
        self.client.connect('192.168.33.10', username='vagrant', password='vagrant')

    def send_command(self, command):
        if self.client:
            result = []
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                for row in stdout:
                    result.append(str(row))
                return result
        else:
            raise ConnectionError('Cannot connect to host!')

    def close(self):
        self.client.close()