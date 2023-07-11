import socket
import os
import shutil

IP = socket.gethostbyname(socket.gethostname())
PORT = 4457
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024000

def main():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDR)

    """ Opening and reading the file data. """
    ch=input("What do you want to do ? (upload/download)")
    client.send(ch.encode(FORMAT))
    msg1=client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg1}")
    if ch == "upload":
        print("\n The available files in your directory are")
        print(os.listdir('client_files/'))
        fname=input("Enter the file Name")
        filepath=os.path.join("client_files", fname)
        file = open(filepath, "r")
        data = file.read()

        """ Sending the filename to the server. """
        client.send(fname.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        """ Sending the file data to the server. """
        client.send(data.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        """ Closing the file. """
        file.close()
    elif ch == "download":
        fname1=input("Enter the file that has to be extracted (zip format)")
        """Sending the filename to server"""
        client.send(fname1.encode(FORMAT))
        msg2=client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg2}")
        
        filename1=client.recv(SIZE).decode(FORMAT)
        client.send("Decompressed file name received".encode(FORMAT))

        print(filename1)

        act2_file_path=os.path.join("client_files", filename1)
        file2 = open(act2_file_path, "w")

        data = client.recv(SIZE).decode(FORMAT)
        file2.write(data)
        client.send("FILE DATA RECIVED".encode(FORMAT))
        file2.close()


    """ Closing the connection from the server. """
    client.close()


if __name__ == "__main__":
    main()