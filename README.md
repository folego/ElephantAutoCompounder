# Autocompound Tool for Elephant TRUNK Stampede
This tool can run locally and your private key will be stored in a regular txt file. This key is needed to interact with the contract and execute the command to roll your rewards.
Please, contribute adding me as a parter: 0x98C4Ac9C24C2971e5e2C085cA424a061D0A9020D

# How to configure
Check the 2 variable in the stampede.py file called minimum_to_roll and time_between_check.
Minimun to roll [minimum_to_roll] variable represents the minimum amount to have before roll your rewards.
Time between checks [time_between_check] variable represents the time the process is paused between each reward TRUNK check.

## Setup Roller
You NEED TO use the encryption outlined in the code to best protect yourself in the event your computer is ever compomised. 

1. Download [Python](https://www.python.org/downloads/) if you do not already have it. There are a number of resources that will walk 
you through installing Python depending on your operating system.

2. Once Python is installed, the following packages need to be installed. Open a terminal/command window and run Python. Then, run the commands shown below. 

```bash
$ python -m pip install web3
$ python -m pip install cryptography
$ python -m pip install python-dotenv
```

3. Using a python terminal (type python in your terminal or command line), import `cryptography` and encrypt your private key

```py
from cryptography.fernet import Fernet
key = Fernet.generate_key()
key.decode()
```

4. Open `.env.example` and replace the key with the key you generated in step 3. SAVE THE FILE WITHOUT .example at the end. This key 
SHOULD contain the quotes before and after the key.

5. Encrypt your private key. 

```py
>>>fernet = Fernet(key)
>>>encMessage = fernet.encrypt('YOUR_PRIVATE_KEY_HERE'.encode())
>>>encMessage.decode()
```

If you are using MetaMask, your private key can be found under account details -> Export Private Key. If you are using TrustWallet, you need to take your seed
phrase and import your wallet into MetaMask. Then you can export the private key. Using your seed phrase for TrustWallet will not work. 

6. Take the value in `encMessage.decode()`, create (or update) a file called `key.txt` and save the text in the file. This file SHOULD NOT contain quotes. 

7. Open the `stampede.py` file and replace the string stored in `wallet_public_addr` with your own public wallet.

8. Change the `minimum_to_roll` value to the minimum number of TRUNKS you want to compound after reaching

## Using the Roller

In a terminal window, navigate to the location where you saved all the files. Run the `stampede.py` file.

```bash
$ python stampede.py
```

This terminal window will always need to remain open for the autoplanter to function. If the terminal window closes, just execute
`stampede.py` again.

If this autoplanter helps you, consider supporting me by sending me an airdrop. 

**wallet:** *0x98C4Ac9C24C2971e5e2C085cA424a061D0A9020D*

If you haven't already invested in the [Elephant](https://elephant.mone), then I highly recommend you doing so!