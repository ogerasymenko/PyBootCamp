import paramiko
import pytest
import time

@pytest.fixture(scope='module')
def setup():
    """Setup environment for launching tests"""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect('192.168.33.10', username='vagrant', password='vagrant')
    stdin, stdout, stderr = client.exec_command('pgrep java | head -1')

    is_running = False
    for line in stdout:
        is_running = True
        break
    client.close()

    if not is_running:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        client.connect('192.168.33.10', username='vagrant', password='vagrant')
        client.exec_command('wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X', timeout=5)
        time.sleep(10)
        client.exec_command('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')
        time.sleep(5)
        client.exec_command('java -jar selenium-server-standalone-3.8.0.jar -role node  -hub http://localhost:4444/grid/register >> log.txt 2>&1 &')
        client.close()
        return 'Setup is ok'

    else:
        return 'Java already running'
