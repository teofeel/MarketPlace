pragma solidity ^0.5.0;

contract NFT {
    bytes32 private name;
    uint256 private id;

    constructor(bytes32 _name, uint256 _id) public{
        name=_name;
        id=_id;
    } 
}