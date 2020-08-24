#### FLASK RESTX APP

“Flask restx app for a PoK (proof of knowledge).”


### Terminal commands
Note: make sure you have `pip` and `virtualenv` installed.

    Initial installation: make install

    To run test: make tests

    To run coverage: make coverage (HTML reports are on /htmlcov)

    To run application: make run

    To run all commands at once : make all
    
    To create wheel for delivery: make production (for production use gunicorn server)

### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/


### TODO's

* Complete the unit test for office-service
* Complete the unit test for department-service
* Complete the unit test for expand-service
* Compile wheel in C for production artifact
* Improve exception logic in services