# compound-python
using Brownie to interact with Compound Protocol

1. Install Brownie

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
# restart your terminal
pipx install eth-brownie
```
Or, if that doesn't work, via pip
```bash
pip install eth-brownie
```

2. Testing
```bash
add a WEB3_INFURA_PROJECT_ID variable in your .env file, checkout the .env.sample for ref

run tests on mainnet fork by running 
brownie test --network mainnet-fork
```
