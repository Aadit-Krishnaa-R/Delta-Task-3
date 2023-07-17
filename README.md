# FILE ARCHIVAL SERVER


> Starting off, git clone my repo
>
>> git clone https://github.com/Aadit-Krishnaa-R/Delta-Task-3.git

### Run the db script
```
python3 db.py
```
database will be set up

### Run the adduser.sh (if it works)

If it doesn't work run these commands manually from the working directory
```
sudo mkdir -p ~/Desktop/aadit/client_files
sudo mkdir -p ~/Desktop/krishnaa/client_files
sudo mkdir -p ~/Desktop/simp/client_files
sudo mkdir -p ~/Desktop/thalaiva/client_files

sudo cp ./client.py ~/Desktop/aadit
sudo cp ./client.py ~/Desktop/krishnaa
sudo cp ./client.py ~/Desktop/simp
sudo cp ./client.py ~/Desktop/thalaiva

sudo cp ./client_files/simp.txt ~/Desktop/aadit/client_files
sudo cp ./client_files/simp2.txt ~/Desktop/krishnaa/client_files
sudo cp ./client_files/simp3.txt ~/Desktop/simp/client_files
sudo cp ./client_files/simp4.txt ~/Desktop/thalaiva/client_files
```

### Run the server script 

```
python3 server.py
```

### Run the client script

cd to any of the user's directory to run the client script or run the client in the working directory itself

```
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