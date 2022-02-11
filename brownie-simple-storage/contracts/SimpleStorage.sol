// SPDX-License-Identifier: GPL-3.0-or-later
pragma solidity >=0.8.0;

contract SimpleStorage {
    // Variable that will be seen by everyone.
    uint256 public publicFavNum = 2;

    // Functions
    function store(uint256 _favoriteNumber) public {
        publicFavNum = _favoriteNumber;
    }

    // Why do we need this? publicFavNum is already public...
    // view: blockchain status is not altered
    function retrieve() public view returns (uint256) {
        return publicFavNum;
    }

    // Associate a favorite number to an adress.
    // Many users can store their favorite number in this contract.
    struct People {
        uint256 favoriteNumber;
        string name;
    }

    // Create one person
    People public bobSponge = People({favoriteNumber: 2, name: "bobSponge"});

    // Array of people.
    // Its a dynamic array, it can change the size.
    // We can fix the size of the array.
    People[] public people;

    // Mapping: key=name, value=favNum
    mapping(string => uint256) public nameToFavoriteNumber;

    // Adding a person. (string is an array, so we need to specify)
    // memory: stores only in execution.
    // storage: data persists after execution.
    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
