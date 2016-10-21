import socketserver
import configparser
from flux_light import FluxLightControl
import sys
import threading


config = configparser.ConfigParser()
config.read("config.ini")


class ServerHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data.decode())
        self.handle_data()

    def handle_data(self):
        data = self.data.decode().split(":")
        if data[0] == "CONFIG":
            with open("config.ini", "w") as writer:
                writer.write(data[1])
            config.read("config.ini")
        elif data[0] == "GET":
            with open("config.ini", "rb") as reader:
                self.request.sendall(reader.read())
        elif data[0] == "TURNONOFF":
            with FluxLightControl(config["DEVICE"]["BulbIP"], int(config["DEVICE"]["BulbPort"])) as bulb:
                print(bulb.turn_on_off())
        elif data[0] == "TURNON":
            with FluxLightControl(config["DEVICE"]["BulbIP"], int(config["DEVICE"]["BulbPort"])) as bulb:
                print(bulb.turn_on())
        elif data[0] == "TURNOFF":
            with FluxLightControl(config["DEVICE"]["BulbIP"], int(config["DEVICE"]["BulbPort"])) as bulb:
                print(bulb.turn_off())


def run_listener():
    port = int(config["DEVICE"]["Port"])
    sock = socketserver.TCPServer(("0.0.0.0", port), ServerHandler)
    print("Listening on: 0.0.0.0:{}".format(port))
    sock.serve_forever()

if __name__ == "__main__":
    try:
        t1 = threading.Thread(target=run_listener)
        t1.daemon = True
        t1.start()
        t1.join()
    except KeyboardInterrupt:
        print("\nClosing...")
        sys.exit(0)
