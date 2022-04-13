//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    //simple contract that stores a number and is able to retrieve it
    uint256 storedNumber;
    //emits a stored event after every storage.
    event Stored(uint256 indexed storedNum, address indexed user);

    //storing function
    function store(uint256 _number) public {
        storedNumber = _number;
        emit Stored(_number, msg.sender);
    }

    //retrieving function
    function retrieve() public view returns (uint256) {
        return storedNumber;
    }
}
