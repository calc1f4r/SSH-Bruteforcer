### ⚔ Description

#### 🔥 Async SSH Bruteforce

This tool is an asynchronous SSH brute-force script written in Python, designed to aid in testing the security of SSH authentication. It utilizes the power of asynchronous programming using the asyncio library and the asyncssh and paramiko libraries for SSH connections.

By providing a target host, port, username, and a wordlist of passwords, the script attempts to establish SSH connections using different password combinations. It runs multiple SSH brute-force attempts concurrently, maximizing the efficiency of the process.

The tool provides real-time feedback on successful login attempts, displaying the host, login, and password combination in green. Failed attempts are also logged, allowing users to track the progress and identify potential weak credentials.

With its asynchronous approach, this script offers faster and more efficient SSH brute-forcing, making it a valuable addition to security testing and vulnerability assessment workflows.

This is the modern apporach of doing this type of things as it uses the minimal resources.



https://github.com/calc1f4r/SSH-Bruteforcer/assets/74751675/ffee3c42-31bc-4559-8cdf-36b468127900






### 🔥 Multi-threaded SSH bruteforcer

This is another variant of the same tool.
Multithreaded Execution: The script utilizes multithreading to enable concurrent execution of multiple brute-force attempts. This approach maximizes efficiency and reduces the time required to test many passwords.

Paramiko Library: The script leverages the paramiko library, an SSH-2 implementation, to handle SSH communication and authentication. It provides a robust and reliable solution for establishing SSH connections.

Command-Line Arguments: The tool supports customization of the target host, port, username, and wordlist file through command-line arguments. This allows users to easily configure the script to target specific SSH servers and customize the authentication parameters.

Real-Time Feedback: The script provides real-time feedback on successful login attempts. When a successful login is found, the script displays the host, login, and password combination in green, indicating a breach. This feature allows users to identify compromised credentials quickly.

Logging of Failed Attempts: The tool logs failed attempts, providing users with the ability to track progress and identify potential weak credentials. Each failed attempt is logged, including the target host, login, and password combination that was attempted.

![SSH bruetforce using threading](https://github.com/calc1f4r/SSH-Bruteforcer/assets/74751675/85fa67cb-4ee0-4382-a3a0-706f2c63f32d)


### ⚔ Learnings

- ⚡ How to use Paramiko for connecting to clients and sending commands
- ⚡ How to use various features of async programming
- ⚡ How to use argparse to parse outputs

### ⚔ Resources Used

- 📚Documentation of Paramiko | [Link](https://www.paramiko.org/)
- 📚Article on How to Execute Shell Commands in a Remote Machine using Python | [Link](https://www.geeksforgeeks.org/how-to-execute-shell-commands-in-a-remote-machine-using-python-paramiko/)
- 📚Documentation of Asyncio | [Link](https://docs.python.org/3/library/asyncio.html)
- 📚Documentation of Asyncssh | [Link](https://asyncssh.readthedocs.io/en/latest/)
