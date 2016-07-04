A centralized suite for home automation. 

### Libraries
Server is built in Python3 using the Flask web framework and uses an SQLAlchemy database. 

### Installation
##### Server
Clone the repository
```bash
git clone https://github.com/jflowaa/smart_home.git
```
Create a virtual environment. This helps keep the server isolated.
```bash
cd smart_home/server
pyvenv venv
```
Enter the virtual environment and install the packages.
```bash
source venv/bin/activate
pip install -r requriments.txt
```
Configure the database and run the server
```bash
python run.py db init
python run.py db migrate
python run.py db upgrade
python run.py runserver
```
Server is now running at: http://127.0.0.1:5000/

### Todo
- [x] Add/remove devices to server
- [ ] Control devices from server
- [x] Create log database table to store notifications
- [x] Create notifications on server on add/remove device
- [ ] Store temperature data in database
- [ ] Store motion data in database --> notification
- [ ] Create temperature chart on server dashboard
- [ ] The TODOs throughout the code