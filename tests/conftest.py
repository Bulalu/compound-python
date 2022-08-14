from brownie import *
import pytest


@pytest.fixture
def cETH():
    yield Contract.from_explorer("0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5")

@pytest.fixture
def cDAI():
    yield Contract.from_explorer("0x5d3a536e4d6dbd6114cc1ead35777bab948e3643")

@pytest.fixture
def comptroller():
    yield Contract.from_explorer("0x3d9819210a31b4961b30ef54be2aed79b9c9cd3b")

@pytest.fixture
def priceFeed():
    yield Contract.from_explorer("0x922018674c12a7f0d394ebeef9b58f186cde13c1")

@pytest.fixture
def dai():
    yield Contract.from_explorer("0x6B175474E89094C44Da98b954EedeAC495271d0F")
    
@pytest.fixture
def whale(accounts):
    yield accounts.at("0x28C6c06298d514Db089934071355E5743bf21d60", force=True)
