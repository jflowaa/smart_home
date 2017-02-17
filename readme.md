A centralized suite for home automation. Automate and control devices that are added to an embedded system such as a raspberry pi or beaglebone. Supported devices is very limited. This project is very early in development.

## Features
- Configure device settings remotely
- Add a PIR sensor and be notified when motion is detected

## Planned Features
- More supported devices (tmp36, dht11/22, wifi lightbulbs)
- Bind events. Such as turn on a light when motion is detected
- Record temperatures and graph the data
- Control lighting
- PaaS deploy

### Supported Devices
- PIR sensor

## Libraries
Server is built in Python3 using the Flask web framework.

## Installation
#### Server
Clone the repository

```bash
git clone https://github.com/jflowaa/smart_home.git
```

Create a Python virtual environment. This helps keep the server packages isolated.
The easiest way would be
```bash
cd smart_home/server
python3 -m venv venv
```
Although there are better methods, such as: [pyenv](https://github.com/yyuu/pyenv)

Activate the virtual environment and install the packages

```bash
source venv/bin/activate
pip install -r requriments/dev.txt
```

Using [Bower](https://bower.io/) to download the used CSS/JS packages
```bash
bower install
```

Now flask needs to be configured
```bash
export FLASK_APP=$(pwd)/run.py
export FLASK_DEBUG=1
```
The above sets the location for flask to get an instance of the app and sets debugging mode.

Configure the database and run the server

```bash
flask db init
flask db migrate
flask db upgrade
flask db run
```
Server is now running at: http://127.0.0.1:5000/

#### Devices
Put the correct `run.py` and `config.ini` onto the embedded system. These files can be found in the `device_scripts/<device_type>` folder.

*These scripts are written in Python3*


To run the script:
```bash
python3 run.py
```

To manage the device:
- Add the device on the server by going to http://0.0.0.0:5000/adddevice
- Go to the device management page. This page can be accessed in many ways. Easiest way is going to the http://0.0.0.0:5000/devices page
- From this page you will be able to manage many aspects of the device

## Misc
If you make changes to the CSS/JS and want to recompress them for production then run
```bash
flask assets clean
flask assets build
```

## Todo
- [ ] Auth for PaaS deploy
- [ ] Add a new page in the nav bar that discribes how to add and control a device
- [ ] Make device types more dynamic and less hard coded
- [x] Add/remove devices to server
- [ ] Control devices from server
- [x] Create log database table to store notifications
- [x] Create notifications on server on add/remove device
- [ ] Create API for server so devices can send data to server
- [ ] Store temperature data in database
- [x] Store motion data in database --> notification
- [ ] Create temperature chart on server dashboard with stored temperature data
- [ ] The TODOs throughout the code
- [x] Get current config.ini from device and display in the textbox for editing.
