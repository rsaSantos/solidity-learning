// SPDX-License-Identifier: GPL-3.0-or-later
pragma solidity >=0.8.0;

contract SimpleStorage{
    
    // Types, a small resume. More at https://docs.soliditylang.org/en/v0.8.11/types.html

    // Positive Integer, 256 bits. Can use only uint, or other variations.
    uint256 favNum = 5;
    
    // Integer, 256 bits. Can use only int, or others. int=int256
    // Can also use int8 to represent an 8 bit number, up to int256.
    int256 negNum = -3;

    bool isEmpty = false;
    string myName = "Ruben";
    address myAddress = 0xB55c23174ca295DC5fF9BfbC0eed9003b75e24c4;
    bytes32 byteTypeTest = "someBytes"; // can range from bytes1...bytes32


    // This will get initialized to 0 (zero).
    uint256 nonInitializedInt;

    // This will be empty. Check more default values at https://docs.soliditylang.org/en/v0.8.11/control-structures.html#default-value
    string nonInitializedString;


    // Variable that will be seen by everyone.
    uint public publicFavNum = 2;

    // Functions
    function store(uint256 _favoriteNumber) public {
        publicFavNum = _favoriteNumber;
    }

    // Why do we need this? publicFavNum is already public...
    // view: blockchain status is not altered
    function retrieve() public view returns(uint256) {
        return publicFavNum;
    }


    // Associate a favorite number to an adress.
    // Many users can store their favorite number in this contract.
    struct People{
        uint256 favoriteNumber;
        string name;
    }

    // Create one person
    People public bobSponge = People({
        favoriteNumber:2,
        name:"bobSponge"
    });

    // Array of people.
    // Its a dynamic array, it can change the size.
    // We can fix the size of the array.
    People[] public people;

    // Mapping: key=name, value=favNum
    mapping(string => uint256) public nameToFavoriteNumber;

    // Adding a person. (string is an array, so we need to specify)
    // memory: stores only in execution.
    // storage: data persists after execution.
    function addPerson(string memory _name, uint256 _favoriteNumber) public{
        people.push(People(_favoriteNumber,_name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }

} 
