from termcolor import cprint
from config import *
from main import *

if __name__ == "__main__":


    if RM_WALLETS == True:
        random.shuffle(KEYS_LIST)

    for privatekey in KEYS_LIST:

        cprint(f'\n=============== start : {privatekey} ===============', 'white')

        swaps(privatekey, CHAIN)


