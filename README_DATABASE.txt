In our initial implementation, we planned on using a mySQL relational database on AWS.
However, due to costs we had to shut down the server last minute. We provided a mySQL database dump so you
are able to recreate the database on your local machine.

Local mySQL steps:
- in your mySQL application, go to the server tab, then press Data Import
- Choose the "Import from self-contained File" option
- Locate the mySQL dump named "FinalDB_Backup", the dump will be placed in the github of the project
	and submitted along with the report
- Click the Start Import button at the bottom. NOTE: the button could be hidden under the OUTPUT section
- After the import is done, follow the steps regarding the python code


Python Side:
- navigate to the database_abstract.py class in the Controller.database folder of the project
- Inside the connect_to_database function, change "host="reversigroup4.cm0trrj52t1s.us-east-1.rds.amazonaws.com""
	to "host= <WHATEVER YOUR LOCAL INSTANCE SERVER IS NAME ON YOUR COMPUTER>"
	for me, host is "localhost" or "MYSQL80"
- change user and passwd to the proper values on your local machine for the instance named above
- keep database = "reversi" as it is

Sorry for any inconvencience this might have caused. The billing charges from AWS were unexpectedly large