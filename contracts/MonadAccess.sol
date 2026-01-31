// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title MonadAccess
 * @dev Pay-As-You-Go SaaS platform on Monad Testnet
 * @notice Users pay in MON tokens to access AI services
 */
contract MonadAccess {
    // Owner address
    address public owner;
    
    // Service types
    enum ServiceType { GPT_PRO, GEMINI_AI, BG_REMOVER, IMAGE_GENERATOR }
    
    // Service pricing in wei (1 MON = 10^18 wei)
    mapping(ServiceType => uint256) public servicePrices;
    
    // Events
    event ServicePurchased(
        address indexed user,
        ServiceType indexed service,
        uint256 amount,
        uint256 timestamp
    );
    
    event PriceUpdated(
        ServiceType indexed service,
        uint256 oldPrice,
        uint256 newPrice
    );
    
    event Withdrawal(
        address indexed owner,
        uint256 amount,
        uint256 timestamp
    );
    
    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this");
        _;
    }
    
    /**
     * @dev Constructor - sets initial prices
     */
    constructor() {
        owner = msg.sender;
        
        // Initialize service prices - All 0.003 MON
        servicePrices[ServiceType.GPT_PRO] = 0.003 ether;
        servicePrices[ServiceType.GEMINI_AI] = 0.003 ether;
        servicePrices[ServiceType.BG_REMOVER] = 0.003 ether;
        servicePrices[ServiceType.IMAGE_GENERATOR] = 0.003 ether;
    }
    
    /**
     * @dev Pay for a service
     * @param service The service type to purchase
     */
    function payForService(ServiceType service) external payable {
        uint256 price = servicePrices[service];
        require(msg.value >= price, "Insufficient payment");
        
        // Emit event for backend to listen
        emit ServicePurchased(msg.sender, service, msg.value, block.timestamp);
        
        // Refund excess payment
        if (msg.value > price) {
            uint256 refund = msg.value - price;
            (bool success, ) = payable(msg.sender).call{value: refund}("");
            require(success, "Refund failed");
        }
    }
    
    /**
     * @dev Update service price (admin only)
     * @param service Service type to update
     * @param newPrice New price in wei
     */
    function updatePrice(ServiceType service, uint256 newPrice) external onlyOwner {
        uint256 oldPrice = servicePrices[service];
        servicePrices[service] = newPrice;
        
        emit PriceUpdated(service, oldPrice, newPrice);
    }
    
    /**
     * @dev Withdraw collected funds (admin only)
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        (bool success, ) = payable(owner).call{value: balance}("");
        require(success, "Withdrawal failed");
        
        emit Withdrawal(owner, balance, block.timestamp);
    }
    
    /**
     * @dev Get current price for a service
     * @param service Service type
     * @return Price in wei
     */
    function getPrice(ServiceType service) external view returns (uint256) {
        return servicePrices[service];
    }
    
    /**
     * @dev Get contract balance
     * @return Balance in wei
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
    
    /**
     * @dev Transfer ownership (admin only)
     * @param newOwner New owner address
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address");
        owner = newOwner;
    }
}
