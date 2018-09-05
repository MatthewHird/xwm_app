# xwm_app

This app is to be used in conjunction with the xwm_database. The script to setup the xwm_database can be found at https://github.com/MatthewHird/xwm_database

A PostgreSQL server and database must be set up before this script can be run. Additionally, a text file must be created called "server_parameters" in the main directory. This file should contain a single line in the form of:

    host=server_id dbname=database_name user=postgres_username password=postgres_password

This app also requires the ImageTk extension for PIL, as well as the psycopg2 library. On linux this can be installed in the terminal using:
  
for python2:
  
    sudo apt-get install python-imaging python-imaging-tk
    sudo pip install psycopg2-binary
  
for python3:
  
    sudo apt-get install python3-pil python3-pil.imagetk
    sudo pip3 install psycopg2-binary
