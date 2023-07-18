# FILE ARCHIVAL SERVER


> Starting off, git clone my repo
>
>> git clone https://github.com/Aadit-Krishnaa-R/Delta-Task-3.git

### Run the db script
```
python3 db.py
```
database will be set up

### Run the adduser.sh 

Modify the permissions 
```
sudo chmod +x adduser.sh
```
Run the script
```
./adduser.sh
```


### Run the server script 

```
python3 server.py
```

### Run the client script

cd to any of the user's directory to run the client script or run the client in the working directory itself

```
cd ~/<username>
python3 client.py
```
### Enter the username and password to get started (can be found in db.py)


## Dockerizing the server

From the working directory, give the command

```
docker compose up
```

Open up another terminal and give 

```
docker ps
```
Get the ID of the container and give the command

```
docker exec -it <ID> /bin/sh
```
Inside the container , Run the client script

```
client.py
```

Or create users by the same commands replacinng 'Desktop' with 'app' and run the client scripts inside the user's directory