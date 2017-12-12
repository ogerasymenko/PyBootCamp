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
            print 'Download'
            self.send_command('wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X')


    def start_hub(self):
        print 'Start hub'
        self.send_command('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')


    def add_node(self):
        print 'Add node'
        self.send_command('java -jar selenium-server-standalone-3.8.0.jar -role node  -hub http://localhost:4444/grid/register >> log.txt 2>&1 &')
        