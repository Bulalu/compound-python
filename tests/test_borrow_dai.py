from brownie import Contract, chain, accounts
import pytest
from web3 import Web3

def print_balances(cDAI, dai, whale, cETH):
    print(f"Whale DAI balance: {dai.balanceOf(whale)}")
    print(f"Whale ETH balance: {whale.balance()}")
    print(f"Whale cDAI balance: {cDAI.balanceOf(whale)}")
    print(f"Whale cETH balance: {cETH.balanceOf(whale)}")


def test_borrow_dai(cDAI, comptroller, priceFeed, dai, cETH):
    bob = accounts[0]
    assetName = "DAI"
    underlyingDecimals = 18
    print(dai.name())
    print_balances(cDAI, dai, bob, cETH)

    # supplying eth to compound as collateral
    amount_to_deposit = Web3.toWei(4, "ether")
    print("\n Supplying ETH to the protocol as collateral \n")
    cETH.mint({"from": bob, "value":amount_to_deposit})
    print_balances(cDAI, dai, bob, cETH)

    print('\nEntering market (via Comptroller contract) for ETH (as collateral)...\n')
    comptroller.enterMarkets([cETH.address], {"from": bob})

    print("Calculating your liquid assets in the protocol...")
    liquidity = comptroller.getAccountLiquidity(bob)
    print(liquidity)
    liquidity = liquidity[1] / 10 ** 18
    print(liquidity)

    print("Fetching cETH collateral factor...")
    collateralFactor =  (comptroller.markets(cETH)[0] / 10 ** 18 ) * 100 #convert to percent
    print(collateralFactor)
    
    print(f" Fetching {assetName} price from the price feed....")
    underlyingPriceInUsd = priceFeed.price(assetName)
    underlyingPriceInUsd = underlyingPriceInUsd / 10 ** 6
    print(underlyingPriceInUsd)

    print(f"Fetching borrow rate per block for {assetName} borrowing...")
    borrowRate = cDAI.borrowRatePerBlock()
    borrowRate = borrowRate / 10 ** underlyingDecimals


    print(f"You have {liquidity} of LIQUID assets (worth of usd) pooled in the protocol.")
    print(f"You can borrow up to {collateralFactor}% of your TOTAL collateral supplied to the protocol as {assetName}")
    print(f"1 {assetName} == {underlyingPriceInUsd} USD")
    print(f"You can borrow up to {liquidity/underlyingPriceInUsd} {assetName} from the protocol ..")
    print(f"NEVER borrow near the maximum amount because your account will be instantly liquidated.")
    print(f"Your borrowed amount INCREASES ({borrowRate} * borrowed amount) {assetName} per block. \n This is based on the current borrow rate.\n")

    underlyingToBorrow = 50
    print(f"Now attempting to borrow {underlyingToBorrow} {assetName}")
    scaledUpBorrowAmount = (underlyingToBorrow * 10 ** underlyingDecimals)

    cDAI.borrow(scaledUpBorrowAmount, {"from": bob})
    print()
    print_balances(cDAI, dai, bob, cETH)

    print(f"Fetching {assetName} borrow balance from {assetName} contract ...")
    # balance = cDAI.borrowBalanceCurrent(bob, {"from": bob})
    # print(balance.events)
    # balance = balance / 10 ** underlyingDecimals
    # print(f"Borrow balance is {balance} {assetName}")

    #do something with the borrowed assets

    # print()
    print("Now repaying the borrow")
    print(f"Approving {assetName} to be transferred from your wallet to the c{assetName} contract ...")
    underlyingToRepay = underlyingToBorrow * 10 ** 18
    dai.approve(cDAI, underlyingToRepay, {"from": bob})

    cDAI.repayBorrow(underlyingToRepay, {"from": bob})
    print("Borrow Repaid!")
    print_balances(cDAI, dai, bob, cETH)

