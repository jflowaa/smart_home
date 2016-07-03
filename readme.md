A centralized suite for home automation. 

### Libraries
Server is built in Flask and uses an SQLAlchemy database using Python3. 

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
source venv/bin/active
pip install -r requriments.txt
```
Configure the database and run the server
```bash
python run.py db init
python run.py db migrate
python run.py shell
>>> db.create_all()
>>> exit()
python run.py runserver
```
Server is now running at: http://127.0.0.1:5000/

### Todo
- [x] Add/remove devices to server
- [ ] Control devices from server
- [ ] Create log database table to store notifications
- [ ] Create notifications on server on add/remove device
- [ ] Store temperature data in database
- [ ] Store motion data in database --> notification
- [ ] Create temperature chart on server dashboard
