const IotAuthentication = artifacts.require("IotAuthentication");

contract("IotAuthentication", accounts => {
  it("should authorize and deauthorize devices", async () => {
    const iotAuthentication = await IotAuthentication.deployed();

    const device1 = accounts[1];
    const device2 = accounts[2];

    assert.equal(await iotAuthentication.isAuthorized(device1), false);
    assert.equal(await iotAuthentication.isAuthorized(device2), false);

    await iotAuthentication.authorizeDevice(device1);

    assert.equal(await iotAuthentication.isAuthorized(device1), true);
    assert.equal(await iotAuthentication.isAuthorized(device2), false);

    await iotAuthentication.deauthorizeDevice(device1);

    assert.equal(await iotAuthentication.isAuthorized(device1), false);
    assert.equal(await iotAuthentication.isAuthorized(device2), false);
  });
});
