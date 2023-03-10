from web3 import Web3
from web3.contract import Contract

# Connect to local blockchain
w3 = Web3(Web3.HTTPProvider('ADD Localhost URL'))

# Load contract ABI and address
# Insert ABI here
contract_abi = [
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "device",
          "type": "address"
        }
      ],
      "name": "authorizeDevice",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "device",
          "type": "address"
        }
      ],
      "name": "deauthorizeDevice",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "device",
          "type": "address"
        }
      ],
      "name": "isAuthorized",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": True
    }
  ]
contract_address = 'Add blockchain contract adress from solitdity after deployment' # Insert address here

# Instantiate contract object
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Authorize a device
device_address = 'Device Address in a blockchain contract'
txn_hash = contract.functions.authorizeDevice(device_address).transact()
txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)

# Check if a device is authorized
is_authorized = contract.functions.isAuthorized(device_address).call()
print('Device is authorized:', is_authorized)
