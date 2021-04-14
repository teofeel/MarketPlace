pragma solidity ^0.8.3;

//string = bytes32 u solidity

contract NFT{
    enum tip{Photo, Video, Gif}
    uint256 public id;
    address public owner;
    bytes32 public name;
    uint256 public price;
    tip public choice;

    constructor(tip izbor, uint256 __id, address __owner, bytes32 __name, uint256 __price){
        choice = izbor;
        id = __id;
        owner = __owner;
        name = __name;
        price = __price;
    }
    
}

