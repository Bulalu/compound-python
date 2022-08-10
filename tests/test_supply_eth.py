import pytest
from brownie import Contract, chain, accounts
from web3 import Web3


one_hour = 3600
one_day = one_hour * 24
one_week = one_day * 7
one_month = one_day * 30


def test_supply_eth(cETH, whale):

    bob = accounts[0]
    amount_to_deposit = Web3.toWei(4, "ether")

    assert cETH.name() == "Compound Ether"
    
    print("Depositing ETH to the Compound Protocol...")
    cETH.mint({"value": amount_to_deposit, "from": bob})
    cTokenBalance = cETH.balanceOf(bob)
    print(f"Bob's cETH balance: {cTokenBalance}")
    print(cETH.totalSupply())
    assert cTokenBalance > 0
    
    exchangeRateCurrent = cETH.exchangeRateCurrent({"from": bob})
    print(f"Current exchange rate from cETH to ETH: {exchangeRateCurrent}")

    print("Redeeming cETH for ETH...")
    print(cETH.balanceOf(accounts[4]))
    # doesn't fail for users with 0 cETH
    tx = cETH.redeem(cTokenBalance, {"from": bob})
    accrued_interest = tx.events["AccrueInterest"]["interestAccumulated"]
    redeem_tokens = tx.events["Redeem"]["redeemTokens"]
    redeem_amount = tx.events["Redeem"]["redeemAmount"]
    print(f"Accrued interest: {accrued_interest}")
    assert redeem_tokens == cTokenBalance
    assert redeem_amount > amount_to_deposit

    



