from web3 import Web3
from eth_abi import decode


def get_beacon_proxy_implementation(beaco_proxy_address):

    web3 = Web3(Web3.HTTPProvider("https://1rpc.io/arb"))

    BEACON_SLOT = "0xa3f0ad74e5423aebfd80d3ef4346578335a9a72aeaee59ff6cb3582b35133d50"

    value_slot = web3.eth.get_storage_at(beaco_proxy_address, BEACON_SLOT)

    beacon_address = decode(["address"], value_slot)[0]

    beacon_address = web3.to_checksum_address(beacon_address)

    beacon_abi = [
        {
            "constant": True,
            "inputs": [],
            "name": "implementation",
            "outputs": [{"name": "", "type": "address"}],
            "type": "function",
        }
    ]

    beacon = web3.eth.contract(beacon_address, abi=beacon_abi)

    implementation_address = beacon.functions.implementation().call()

    return web3.to_checksum_address(implementation_address)
