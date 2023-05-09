# StatsViewer

### Short description
Our app will calculate the number of rising, falling, and flat sessions for the last 1 week, 2 weeks, 1 month, 1 quarter, 6 months, and 1 year for a user-selected currency.
Additionally, the app will determine the median, standard deviation, and coefficient of variation for the same time periods and currency.
Once the app has successfully completed its operation, the generated data will be displayed in tabular form on the console.
The user will select the currency by entering the appropriate ISO 4217 currency code as an argument to the executable program.
The app generates data for one statistical operation and one currency relative to the PLN specified by the user, and for all time intervals.
The supported currencies are EUR and USD.


### Project structure
```
.
├── .circleci
│   └── config.yml
├── src
│   └── main.py
├── tests
│    └── test.py
└── requirements.txt
```

where 
* **.circleci** contain config.yml file with configuration to CI system
* **src** is a dir where we store app files
* **tests** dir contains test files
* **requirements.txt** is a file with list of all python modules used by our app


### Technologies
* Python 3.10
* numpy
* prettytable
* requests
* json
* git


### Getting started
##### if not installed
1. sudo apt install python3.10
2. sudo apt install python3-pip
3. sudo apt install python3.10-venv
4. sudo apt install git-all
##### Run app
1. git clone https://github.com/IIS-ZPI/ZPI2022_IO1_Team_R.git
2. cd ZPI2022_IO1_Team_R
3. python3 -m venv venv
4. . venv/bin/activate
5. pip install -r requirements.txt
6. python3 src/main.py


### Documentation
Not specified yet


### Backlog
https://github.com/orgs/IIS-ZPI/projects/14/views/1


### CI Sysyem
https://app.circleci.com/pipelines/github/IIS-ZPI/ZPI2022_IO1_Team_R


### Reports
Not specified yet
