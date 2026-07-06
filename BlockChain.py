from web3 import Web3
from solcx import compile_standard
from solcx import install_solc

install_solc("0.8.0")
import json

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"  # Update with your Ganache URL
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Account information
account_1 = "0x4d7C54086a691D162730965Fd23aa86741701C27"  # Update with your Ganache account address
private_key = "0x3e24b5fb4f31c43a46a3e168aa6f4fd573c779378d205b65789909d061ade053"     # Update with your Ganache account private key

# Compile the solidity contract
def compile_contract():
    with open("./contracts/DataStorage.sol", "r") as file:
        data_storage_file = file.read()

    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {"DataStorage.sol": {"content": data_storage_file}},
            "settings": {
                "outputSelection": {
                    "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                }
            },
        },
        solc_version="0.8.0",
    )
    return compiled_sol

# Deploy the contract
def deploy_contract(compiled_sol):
    bytecode = compiled_sol["contracts"]["DataStorage.sol"]["DataStorage"]["evm"]["bytecode"]["object"]
    abi = compiled_sol["contracts"]["DataStorage.sol"]["DataStorage"]["abi"]

    # Get nonce
    nonce = web3.eth.getTransactionCount(account_1)

    # Build transaction
    transaction = {
        "from": account_1,
        "gas": 2000000,
        "gasPrice": web3.toWei("50", "gwei"),
        "nonce": nonce,
        "data": bytecode,
    }

    # Sign transaction
    signed_transaction = web3.eth.account.sign_transaction(transaction, private_key)

    # Send transaction
    tx_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)

    # Get transaction receipt
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    return web3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# Main function
def main():
    compiled_sol = compile_contract()
    contract = deploy_contract(compiled_sol)

    # Store data
    contract.functions.addData("bob@gmail.com", "1").transact({"from": account_1})
    contract.functions.addData("bob@gmail.com", "2").transact({"from": account_1})
    contract.functions.addData("bob@gmail.com", "3").transact({"from": account_1})
    #contract.functions.addData("name1", "Jane").transact({"from": account_1})

    # Retrieve data
    data = contract.functions.getData("bob@gmail.com").call()
    print("Retrieved Data:", data)



if __name__ == "__main__":
    main()
