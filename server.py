import socket
import threading
import shutil
import os
import hashlib
import sqlite3
from zipfile import ZipFile
from Crypto.Cipher import AES
SIZE = 1024000
FORMAT = "utf-8"
key=b"ThisIsAaditForU."
nonce=b"ThatWasAaditForU"

cipher=AES.new(key, AES.MODE_EAX, nonce)



def file_compress(filepath):
    filename=os.path.basename(filepath)
    base_name, _=os.path.splitext(filename)
    zip_name=base_name + '.zip'
    f=ZipFile(zip_name,"w")
    f.write(filepath)
    f.close()
    shutil.move(zip_name, 'server_files/')
    return zip_name


def file_decompress(filepath):
    filename=os.path.basename(filepath)
    base_name, _=os.path.splitext(filename)
    txt_name=base_name + '.txt'
    txt_name_path=os.path.join("./", txt_name)
    f1=ZipFile(filepath,"r")
    f1.extractall(path="./")
    print(txt_name)
    return txt_name


def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected")
    while True:
        conn.send("Username:".encode(FORMAT))
        username=conn.recv(SIZE).decode(FORMAT)
        conn.send("Password:".encode(FORMAT))
        password=conn.recv(SIZE)
        password=hashlib.sha256(password).hexdigest()

        c=sqlite3.connect("userdata1.db")
        cur=c.cursor()
        cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?",(username, password))

        if cur.fetchall():
            conn.send("LOGIN SUCCESSFULL".encode(FORMAT))
            ch=conn.recv(SIZE).decode(FORMAT)
            conn.send("Choice Recieved".encode(FORMAT))
            if ch == "upload":
                filename = conn.recv(SIZE).decode(FORMAT)
                # print(f"[RECV] Receiving the filename.")
                file = open(filename, "wb")
                conn.send("Filename received.".encode(FORMAT))

                """ Receiving the file data from the client. """
                data = conn.recv(SIZE)
                # print(f"[RECV] Receiving the file data.")
                file.write(cipher.decrypt(data))
                conn.send("File data received".encode(FORMAT))

                file.close()

                act1_file_path=os.path.join("./", filename)
                zipname=file_compress(act1_file_path)
                os.remove(act1_file_path)
                conn.send(zipname.encode(FORMAT))
                break
            
            elif ch == "download":
                filename1=conn.recv(SIZE).decode(FORMAT)
                act_file_path=os.path.join("server_files/", filename1)
                conn.send("Filename recieved".encode(FORMAT))
                decomp_file=file_decompress(act_file_path)
                os.remove(act_file_path)
                """Sending the name """
                conn.send(decomp_file.encode(FORMAT))
                msg1=conn.recv(SIZE).decode(FORMAT)
                print(f"[CLIENT]: {msg1}")

                file1=open(decomp_file, "rb")
                data1=file1.read()

                encrypted1=cipher.encrypt(data1)

                conn.send(encrypted1)
                msg = conn.recv(SIZE).decode(FORMAT)
                # print(f"[CLIENT]: {msg}")
                file1.close()
                dup1_file_path=os.path.join("./", decomp_file)
                os.remove(dup1_file_path)
                break
            else:
                break
        else:
            conn.send("LOGIN FAILED".encode(FORMAT))
            break
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")

def main():
    print("[STARTING] server is starting ...")
    host = socket.gethostbyname(socket.gethostname())
    port = 9991
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen()
    print(f"[LISTENING] server is listening on {host}")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client,args=((conn, addr)))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")



if __name__ == "__main__":
    main()

