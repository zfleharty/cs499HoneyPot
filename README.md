# cs499HoneyPot

##HoneyPy
To start HoneyPY on it's own chang cwd to HoneyPy directory
`docker-ce`
##Database
To run database change cwd to database directory
`docker-compose up -d`


##Connection to database
Enter the following command and type the root password found in the docker-compose.yaml file under environments.
`docker exec -it db_container bash -c "mysql -u root -p"'
