from brownie import interface, accounts, network, config, Contract
from brownie.network.gas.strategies import GasNowStrategy
from scripts.helpful_scripts import get_account
from scripts.abi.cETHRinkeby import abi
from web3 import Web3



def supply_eth():
    account = get_account()
    amount_to_deposit = Web3.toWei(1, "ether")
    cEthContractAddress = config["networks"][network.show_active()]["cETH"]
    
    cEthContract = Contract.from_abi(name= "CEther", address=cEthContractAddress, abi=abi)
    decimals = cEthContract.decimals()
    eth_decimals = 18
    
    print("Beep boop, supplying ETH to the compound Protocol")
    
    # tx = cEthContract.mint({"from": account, "value": amount_to_deposit})
    # print(tx)
    # tx = account.transfer(cEthContractAddress, amount_to_deposit)
    print("Account balance: ", account.balance())
    print("decimals: ", decimals)
    print("contract", cEthContract.name())
    
    




    
    # print("cETH Mint operation successful")
    # print(decimals)
    
    # balanceOfUnderlying = (cEthContract.balanceOfUnderlying(account)) / 10**eth_decimals
    # print("Eth supplied to the Compound Protocol", balanceOfUnderlying)

    # cTokenBalance = cEthContract.balanceOf(account) / 10**decimals
    # print("cToken Balance", cTokenBalance)

    # exchangeRateCurrent = cEthContract.exchangeRateCurrent() 
    # exchangeRateCurrent = exchangeRateCurrent / 10**(18 + eth_decimals - 8)
    # print("Current exchange rate from cETH to ETH", exchangeRateCurrent)

    # print("Reedeming the cETH for ETH ..." )
    # print()
    # print("Exchanging all cETH based on cToken amount....")
    # cEthContract.redeem(cTokenBalance * 10**decimals, {"from": account, "gas_price": gas_strategy} )
    # print("cETH Redeem operation successful")
    # print()
    # print("Checking the balance of cETH after redeeming....")
    # cTokenBalance = cEthContract.balanceOf(account) / 10**decimals
    # print("cToken Balance", cTokenBalance)
    # eth_balance = account.balance()
    # print("ETH Balance", eth_balance)


def main():
    supply_eth()
    # print(Web3.toWei(0.5, "ether"))
