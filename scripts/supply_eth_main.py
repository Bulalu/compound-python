import pytest
from brownie import Contract, chain, accounts

one_hour = 3600
one_day = one_hour * 24
one_week = one_day * 7
one_month = one_day * 30

@pytest.fixture
def cETH():
    yield Contract.from_explorer("0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5")

# @pytest.fixture
# def pool():
#     yield Contract.from_explorer("0x1338b4065e25AD681c511644Aa319181FC3d64CC")


@pytest.fixture
def whale(accounts):
    yield accounts.at("0x6E685A45Db4d97BA160FA067cB81b40Dfed47245", force=True)

def supply_eth(cETH, whale):
    print(cETH)
    print(whale)
    print(cETH)




def main():

    supply_eth(cETH, whale)
