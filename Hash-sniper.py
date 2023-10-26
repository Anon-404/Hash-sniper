# A simple hash cracker python script by Anon404 

import os
import hashlib
from tqdm import tqdm

RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[1;34m"
os.system("clear")
#_________________banner___________________

banner1 ="""
    dMP dMP .aMMMb  .dMMMb  dMP dMP                   
   dMP dMP dMP"dMP dMP" VP dMP dMP                    
  dMMMMMP dMMMMMP  VMMMb  dMMMMMP                     
 dMP dMP dMP dMP dP .dMP dMP dMP                      
dMP dMP dMP dMP  VMMMP" dMP dMP         """
banner2="""                                                
       .dMMMb  dMMMMb  dMP dMMMMb  dMMMMMP dMMMMb     
      dMP" VP dMP dMP amr dMP.dMP dMP     dMP.dMP     
      VMMMb  dMP dMP dMP dMMMMP" dMMMP   dMMMMK"      
    dP .dMP dMP dMP dMP dMP     dMP     dMP"AMF       
    VMMMP" dMP dMP dMP dMP     dMMMMMP dMP dMP                                                                                                                                                           """
def banner():
	print(GREEN,"_"*63)
	print(RED,banner1)
	print(GREEN,banner2)
	print("Created by Anon404")
	print(GREEN,"_"*63)
	
banner()

print(GREEN,"\b[+] Enter your hash ")
hashvalue1 = input("--> ")

if len(hashvalue1) <= 31:
	print(RED,"\b[-] input a valid hash")
	exit()

hashtypes = """
[1] md5
[2] sha1
[3] sha224
[4] sha256
[5] sha384
[6] sha512
"""

print(GREEN,hashtypes)

print("[+] Enter your hash type ")
hashtype = input("--> ")

#_________wordlist menegement____________
print("[+] Enter your file name")
wordlist1 = input("--> ")	
try:
	wordlist = open(wordlist1,"r" ,errors="replace")
except FileNotFoundError:
	print("file not found")
	exit()

def md5(target_hash, wordlist_file):
    with open(wordlist_file, 'r', encoding='utf-8', errors='replace') as wordlist:
        total_lines = sum(1 for line in wordlist)
        wordlist.seek(0)  # Reset file pointer

        with tqdm(total=total_lines, desc="[+] Cracking MD5 Hash") as pbar:
            for line in wordlist:
                password = line.strip()
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                if hashed_password == target_hash:
                    pbar.close()
                    return password
                pbar.update(1)

    return None

def sha1(target_hash, wordlist_file):
    with open(wordlist_file, 'r', encoding='utf-8', errors='replace') as wordlist:
        total_lines = sum(1 for line in wordlist)
        wordlist.seek(0)  # Reset file pointer

        with tqdm(total=total_lines, desc="[+] Cracking SHA1") as pbar:
            for line in wordlist:
                password = line.strip()
                hashed_password = hashlib.sha1(password.encode()).hexdigest()
                if hashed_password == target_hash:
                    pbar.close()
                    return password
                pbar.update(1)

    return None

def sha224(target_hash, wordlist_file):
    with open(wordlist_file, 'r', encoding='utf-8', errors='replace') as wordlist:
        total_lines = sum(1 for line in wordlist)
        wordlist.seek(0)  # Reset file pointer

        with tqdm(total=total_lines, desc="[+] Cracking SHA224") as pbar:
            for line in wordlist:
                password = line.strip()
                hashed_password = hashlib.sha224(password.encode()).hexdigest()
                if hashed_password == target_hash:
                    pbar.close()
                    return password
                pbar.update(1)

    return None	

def sha256(target_hash, wordlist_file):
    with open(wordlist_file, 'r', encoding='utf-8', errors='replace') as wordlist:
        total_lines = sum(1 for line in wordlist)
        wordlist.seek(0)  # Reset file pointer

        with tqdm(total=total_lines, desc="[+] Cracking SHA256") as pbar:
            for line in wordlist:
                password = line.strip()
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                if hashed_password == target_hash:
                    pbar.close()
                    return password
                pbar.update(1)

    return None	

def sha384(target_hash, wordlist_file):
    with open(wordlist_file, 'r', encoding='utf-8', errors='replace') as wordlist:
        total_lines = sum(1 for line in wordlist)
        wordlist.seek(0)  # Reset file pointer

        with tqdm(total=total_lines, desc="[+] Cracking SHA384") as pbar:
            for line in wordlist:
                password = line.strip()
                hashed_password = hashlib.sha384(password.encode()).hexdigest()
                if hashed_password == target_hash:
                    pbar.close()
                    return password
                pbar.update(1)

    return None			

def sha512(target_hash, wordlist_file):
    with open(wordlist_file, 'r', encoding='utf-8', errors='replace') as wordlist:
        total_lines = sum(1 for line in wordlist)
        wordlist.seek(0)  # Reset file pointer

        with tqdm(total=total_lines, desc="[+] Cracking SHA512") as pbar:
            for line in wordlist:
                password = line.strip()
                hashed_password = hashlib.sha512(password.encode()).hexdigest()
                if hashed_password == target_hash:
                    pbar.close()
                    return password
                pbar.update(1)

    return None								
					
if hashtype == "1":
	if __name__ == '__main__':
	   	print(BLUE,"\b[!] Let me crack your hash")
	   	target_hash = hashvalue1
	   	wordlist_file = wordlist1
	   	result = md5(target_hash, wordlist_file)

	if result:
		print(GREEN,f"\b[+] Password found: {result}")
	else:
		print(RED,"\b[-] Password not found in the wordlist.")
	
elif hashtype == "2":
	if __name__ == '__main__':
		print(BLUE,"\b[!] Let me crack your hash")
		target_hash = hashvalue1
		wordlist_file = wordlist1
		result = sha1(target_hash, wordlist_file)

	if result:
		print(GREEN,f"[+] Password found: {result}")
	else:
		print(RED,"\b[-] Password not found in the wordlist.")
	
elif hashtype == "3":
	if __name__ == '__main__':
		print(BLUE,"\b[!] Let me crack your hash")
		target_hash = hashvalue1
		wordlist_file = wordlist1
		result = sha224(target_hash, wordlist_file)

	if result:
		print(GREEN,f"[+] Password found: {result}")
	else:
		print(RED,"\b[-] Password not found in the wordlist.")
	
elif hashtype == "4":
	if __name__ == '__main__':
		print(BLUE,"\b[!] Let me crack your hash")
		target_hash = hashvalue1
		wordlist_file = wordlist1
		result = sha256(target_hash, wordlist_file)

	if result:
		print(GREEN,f"[+] Password found: {result}")
	else:
		print(RED,"\b[-] Password not found in the wordlist.")
	
elif hashtype == "5":
	if __name__ == '__main__':
		print(BLUE,"\b[!] Let me crack your hash")
		target_hash = hashvalue1
		wordlist_file = wordlist1
		result = sha384(target_hash, wordlist_file)

	if result:
		print(GREEN,f"[+] Password found: {result}")
	else:
		print(RED,"\b[-] Password not found in the wordlist.")
	
elif hashtype == "6":
	if __name__ == '__main__':
		print(BLUE,"\b[!] Let me crack your hash")
		target_hash = hashvalue1
		wordlist_file = wordlist1
		result = sha512(target_hash, wordlist_file)

	if result:
		print(GREEN,f"[+] Password found: {result}")
	else:
		print(RED,"\b[-] Password not found in the wordlist.")	
	
else:
	print(RED,"\b[-]wrong option")
	exit()
