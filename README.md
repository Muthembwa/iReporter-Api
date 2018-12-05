# iReporter Api

Flask Restful Api endpoints for iReporter app that helps fight corruption and help citizens report interventions for efficient functioning of authorities. see more on iReporter from the UI repo https://github.com/Muthembwa/iReporter

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
This project uses Python 3 and Flask restfull which comes with several other dependencies. To install this dependencies at the root folder iReporter-Api, run 'pip install -r requirements.txt' from the terminal. All the dependencies are contained in the requirements.txt


### Installing

A step by step series of examples that tell you how to get a development env running

-clone this repository,
-install a virtualenv "pip install virtualenv"
-create a virtual environment venv at the root of iReporter directory, "virtualenv venv"
-activate it, "source venv/bin/activate"
-install dependencies at the root folder iReporter-Api, run "pip install -r requirements.txt"
-make your flask application run run.py, FLASK_APP=run.py
- to run the app use the command "flask run"
- to test the endpoints install and run postman
- set a Post request to test the endpoint at http://127.0.0.1:5000/api/v1/red-flags 




