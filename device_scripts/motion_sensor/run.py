import socketserver
import requests
import configparser


class ServerHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data.decode())
        self.handle_data()

    def handle_data(self):
        data = self.data.decode().split(":")
        config[data[0]][data[1]] = data[2]



config = configparser.ConfigParser()
config.read("config.ini")

def send_motion_event():
    id = config["DEVICE"]["ID"]
    if not id:
        return "Error: ID is not set! Configure at device management page."
    server_ip = config["SERVER"]["ServerIP"]
    server_port = config["SERVER"]["ServerPort"]
    r = requests.get("http://{}:{}/api/motion/{}".format(server_ip, server_port, id))
    return "yes"

def run_listener():
    port = int(config["DEVICE"]["Port"])
    sock = socketserver.TCPServer(("0.0.0.0", port), ServerHandler)
    print("Listening on: 0.0.0.0:{}".format(port))
    sock.serve_forever()


def run_detector():
    return 1

if __name__ == "__main__":
    # run_listener()
    # run_detector()
    send_motion_event()