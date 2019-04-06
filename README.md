

the 4th project of full stack web develoepr nanodegree in udacity 


Features
 the endpoint of the application that show information about the content at http://localhost:5000/catalog/JSON

CRUD
In this application we apply the CRUB operation add , update and delete 

Authentication & Authorization
This apps uses facebook and google  as authentication .
authorization


How to run

requirements
vagrant['http://www.vagrant.com'] 
vmware['http://www.vmware.com']
flask['http://www.flask.com']
python ['http://www.python.com']

Run

cd vagrant      
vagrant up      
vagrant ssh      


cd /vagrant/catalog
Setup database
python database_setup.py
python insertitems.py



Now you can run the application:
python project.py
 browser an type localhost:5000
