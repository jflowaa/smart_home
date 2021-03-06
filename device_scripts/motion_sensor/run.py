import socketserver
import urllib.request
import configparser
import time
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
        else:
            config[data[0]][data[1]] = data[2]


def send_motion_event():
    print("Got Motion")
    id = config["DEVICE"]["ID"]
    if not id:
        return "Error: ID is not set! Configure at device management page."
    server_ip = config["SERVER"]["ServerIP"]
    server_port = config["SERVER"]["ServerPort"]
    urllib.request.urlopen("http://{}:{}/api/motion/{}".format(server_ip, server_port, id))
    return None


def run_listener():
    port = int(config["DEVICE"]["Port"])
    sock = socketserver.TCPServer(("0.0.0.0", port), ServerHandler)
    print("Listening on: 0.0.0.0:{}".format(port))
    sock.serve_forever()


def run_detector():
    model = config["DEVICE"]["Model"]
    pin = config["DEVICE"]["GPIOPin"]
    delay = int(config["DEVICE"]["NotifyRate"])
    if model == "pi":
        import RPi.GPIO as io
        io.setmode(io.BCM)
        io.setup(int(pin), io.IN)
        while True:
            if io.input(pin):
                send_motion_event()
                time.sleep(delay * 60)
            time.sleep(1)
    elif model == "bone":
        from Adafruit_BBIO import GPIO
        GPIO.setup(pin, GPIO.IN)
        GPIO.add_event_detect(pin, GPIO.RISING)
        while True:
            if GPIO.event_detected(pin):
                send_motion_event()
                time.sleep(delay * 60)
            time.sleep(1)


if __name__ == "__main__":
    try:
        t1 = threading.Thread(target=run_listener)
        t2 = threading.Thread(target=run_detector)
        t1.daemon = True
        t2.daemon = True
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    except KeyboardInterrupt:
        print("\nClosing...")
        sys.exit(0)
