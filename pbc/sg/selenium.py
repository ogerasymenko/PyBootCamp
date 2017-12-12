import time
from pbc.sg.connections import Ssh

class Grid(Ssh):

    def is_downloaded(self):
        _, stdout, _= self.client.exec_command('test -f "selenium-server-standalone-3.8.0.jar" && echo yes')
        processes = []
        for row in stdout:
            processes.append(row)
        if 'yes' in str(processes):
            return True
        else:
            return False

    def download(self):
        if self.is_downloaded() is False:
            print 'Download selenium'
            self.send_command('wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X')
            time.sleep(10)
            self.send_command('wget -O sg-node.json https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/')


    def start_hub(self):
        print 'Start hub'
        self.send_command('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')


    def add_node(self):
        print 'Add node'
        self.send_command('java -jar selenium-server-standalone-3.8.0.jar -role node -nodeConfig sg-node.json >> log.txt 2>&1 &')
        