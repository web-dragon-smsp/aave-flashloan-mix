from brownie import FlashloanV2, accounts, config, network

# AAVE_LENDING_POOL_ADDRESS_PROVIDER = "0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5"


def main():
    """
    Deploy a `FlashloanV2` contract from `accounts[0]`.
    """

    acct = accounts.add(
        config["wallets"]["from_key"]
    )  # add your keystore ID as an argument to this call

    flashloan = FlashloanV2.deploy(
        "0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9",
        {"from": acct},
    )
    return flashloan
