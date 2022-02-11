# Test file always starts with "test" keyword.
# Use "brownie test" to run all tests.
# Use "brownie test -k tests_updating_storage" to run only the selected test.
# See more at https://docs.pytest.org/en/7.0.x/contents.html

# Import brownie accounts, config file and the smart contract from /contracts
from brownie import accounts, config, SimpleStorage  # type: ignore


def test_deploy():
    # Arrange: get an account
    account = accounts[0]

    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 2

    # Assert
    assert starting_value == expected


def test_updating_storage():
    # Arrange: get an account
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # Act
    expected = 15
    transaction = simple_storage.store(15, {"from": account})

    # Assert
    assert expected == simple_storage.retrieve()
