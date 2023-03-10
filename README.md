# IoT Authentication using Blockchain with Truffle

This project aims to demonstrate how blockchain technology can be used for authentication in the context of IoT devices. We use Truffle, a development framework for Ethereum, to create a smart contract that manages the authentication of IoT devices. 

## Requirements

- Truffle (v5.4.15)
- Node.js (v14.18.0)
- Ganache (v2.5.4)

## Installation

1. Clone the repository: `git clone https://github.com/your-username/iot-authentication.git`
2. Navigate to the project directory: `cd iot-authentication`
3. Install the necessary packages: `npm install`
4. Compile the smart contract: `truffle compile`
5. Start Ganache and get the address.
6. Deploy the smart contract on Ganache: `truffle migrate`
7. Start the application: `npm start`

## Usage

1. Create a virtual environment: `python3 -m venv venv`
2. Activate the virtual environment: `source venv/bin/activate`
3. Install the required packages: `pip install -r requirements.txt`
4. Run the application: `python3 main.py`

## Project Structure

- `contracts/`: Contains the smart contract code (IoTAuthentication.sol).
- `migrations/`: Contains the migration script (2_deploy_contract.js) for deploying the smart contract.
- `src/`: Contains the front-end code for the application.
- `test/`: Contains the test cases for the smart contract.
- `main.py`: Contains the back-end code for the application.

## Contributing

If you would like to contribute to this project, feel free to submit a pull request or open an issue.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
