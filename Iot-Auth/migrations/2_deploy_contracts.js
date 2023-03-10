const IotAuthentication = artifacts.require("IotAuthentication");

module.exports = function(deployer) {
  deployer.deploy(IotAuthentication);
};
