from brownie import Contract, chain, accounts
import pytest
from web3 import Web3



def test_borrow_dai(cDAI, comptroller, priceFeed, dai, whale):
    print(dai.name())
    print(f"Whale DAI balance: {dai.balanceOf(whale)}")
    print(f"Whale ETH balance: {whale.balance()}")
    print(f"Whale cDAI balance: {cDAI.balanceOf(whale)}")

    # supplying eth to compound as collateral
    amount_to_deposit = Web3.toWei(4, "ether")