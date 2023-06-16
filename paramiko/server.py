import paramiko
import socket
import threading

host_key = paramiko.RSAKey(filename='host_key.pem')  # replace with your host key

class Server (paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if (username == 'test') and (password == 'password'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED


def listen_for_connections():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', 2222))
    sock.listen(0)

    while True:
        client, addr = sock.accept()

        print(f'Incoming connection from {addr}.')


        t = paramiko.Transport(client)
        t.set_gss_host(socket.getfqdn(""))
        t.load_server_moduli()
        t.add_server_key(host_key)
        server = Server()
        try:
            t.start_server(server=server)
        except paramiko.SSHException:
            print("[!] SSH negotiation failed.")

        # * handle client requests
        # wait for auth
        chan = t.accept(20)
        if chan is None:
            print("[!] No channel.")
            continue

        print("[+] Authenticated!")        
        chan.send('Welcome to the SSH server.')
        while True:
            try:
                command = chan.recv(1024)
                # command = input("Enter command: ")
                if command == 'exit':
                    chan.send('exit')
                    print('Exiting')
                    t.stop_thread()
                    return
                chan.send(command)
            except KeyboardInterrupt:
                t.stop_thread()


if __name__ == "__main__":    
    print("[+] Listening for connection ...")
    listen_for_connections()
