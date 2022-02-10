// SPDX-License-Identifier: GPL-3.0-or-later

// Solidity version.
pragma solidity >=0.8.0;

// SimpleStorage.sol needs to be in the same folder.
// We will import simpleStorage contract.
import "./SimpleStorage.sol";


// This contract will deploy simpleStorage contracts.
// StorageFactory inherits all the functionalities of SimpleStorage.
// StorageFactory is also a SimpleStorage contract.
contract StorageFactory is SimpleStorage {

    // Store all contracts created.
    SimpleStorage[] public simpleStorageArray;

    function createSimpleStorageContract() public {
        // Create an object of type SimpleStorage (creating a new contract).
        SimpleStorage simpleStorage = new SimpleStorage();
    
        // Add newly created contract to the array.
        simpleStorageArray.push(simpleStorage);
    }

    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public {
        // Get respective SimpleStorage object.
        SimpleStorage ss = simpleStorageArray[_simpleStorageIndex];
        
        // Store number to the contract.
        ss.store(_simpleStorageNumber);
    }

    function sfGet(uint256 _simpleStorageIndex) public view returns (uint256) {
        // Get respective SimpleStorage object.
        SimpleStorage ss = simpleStorageArray[_simpleStorageIndex];

        // Get favorite number from contract.
        return ss.retrieve();
    }

}
 
