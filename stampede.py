import json
import time
from datetime import datetime
from datetime import timedelta
import math
import contract as c

elephant_contract_addr = "0x6839e295a8f13864A2830fA0dCC0F52e71a82DbF"
wallet_public_addr = "0x98C4Ac9C24C2971e5e2C085cA424a061D0A9020D"

# load private key
wallet_private_key = open('key.txt', "r").readline()

# load abi
f = open('stampede_abi.json')
contract_abi = json.load(f)

# create contract
elephant_contract = c.connect_to_contract(elephant_contract_addr, contract_abi)

# def get_user_bonds(addr):
#     return elephant_contract.functions.userInfo(addr).call()

def get_user_rewards(addr):
    return elephant_contract.functions.claimsAvailable(addr).call()

def roll():
    txn = elephant_contract.functions.roll().buildTransaction(c.get_tx_options(wallet_public_addr, 500000))
    return c.send_txn(txn, wallet_private_key)

# Format time
intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60 
    ('minutes', 60),
    ('seconds', 1),
)

def display_time(seconds, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(math.floor(value), name))
    return ', '.join(result[:granularity])    

# General options
minimum_to_roll = 2e18
time_between_check = 60
last_reward = 0
actual_reward = 0

while True:
    while True:
        try:
            # print(f'Checking actual rewards')
            actual_rewards = math.floor(get_user_rewards(wallet_public_addr))

            # Calculating next roll
            if last_reward == 0:
                last_reward = actual_rewards
            else: 
                actual_reward = actual_rewards

            if last_reward > 0 and actual_reward > 0:
                speed = actual_reward - last_reward
                # Calculate the current speed (rewards / sec)
                speed = speed / time_between_check
                remaining = minimum_to_roll - actual_rewards
                next_roll = remaining / speed
                print(f'Current rewards speed is: {round(speed/1e18*60*60,4)} (TRUNK/hour). Next roll will be available in {display_time(next_roll)}')
                last_reward = actual_reward
            
            # TO DO: Calculate Trunk/month, Trunk/week, Trunk/day, trunk/hour
            # TO DO: Improve the estimation using average data

            print(f'Actual rewards: {round(actual_rewards/1e18,4)} TRUNK(s)')
            if actual_rewards >= math.floor(minimum_to_roll):
                print(f'Rolling...')
                roll()
                print(f'Rolled! Waiting 60 seconds to start a new cycle')
                time.sleep(60) # Interval to check a new roll
            else:
                print(f'Min rewards not achieved yet, trying again in {time_between_check} seconds')
                time.sleep(time_between_check) # Interval of each check

        except Exception as e:
            pass
            print("ERROR")
            print(e)
            print("Entered in the except of the main loop. Probably an error ocurred. Pausing the process for 15 seconds.")
            time.sleep(15)
        else:
            break



