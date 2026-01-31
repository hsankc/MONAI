// MonadAccess Smart Contract Configuration
// Contract deployed to Monad Testnet on Jan 31, 2026
// Deployment successful!

const CONTRACT_ADDRESS = "0xD1c273e4D5DEC949E4AD83Fd98DA3205122b281e"; // Monad Testnet
const CONTRACT_ABI = [{ "inputs": [], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [{ "indexed": true, "internalType": "enum MonadAccess.ServiceType", "name": "service", "type": "uint8" }, { "indexed": false, "internalType": "uint256", "name": "oldPrice", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "newPrice", "type": "uint256" }], "name": "PriceUpdated", "type": "event" }, { "anonymous": false, "inputs": [{ "indexed": true, "internalType": "address", "name": "user", "type": "address" }, { "indexed": true, "internalType": "enum MonadAccess.ServiceType", "name": "service", "type": "uint8" }, { "indexed": false, "internalType": "uint256", "name": "amount", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "timestamp", "type": "uint256" }], "name": "ServicePurchased", "type": "event" }, { "anonymous": false, "inputs": [{ "indexed": true, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "amount", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "timestamp", "type": "uint256" }], "name": "Withdrawal", "type": "event" }, { "inputs": [], "name": "getBalance", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "enum MonadAccess.ServiceType", "name": "service", "type": "uint8" }], "name": "getPrice", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "owner", "outputs": [{ "internalType": "address", "name": "", "type": "address" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "enum MonadAccess.ServiceType", "name": "service", "type": "uint8" }], "name": "payForService", "outputs": [], "stateMutability": "payable", "type": "function" }, { "inputs": [{ "internalType": "enum MonadAccess.ServiceType", "name": "", "type": "uint8" }], "name": "servicePrices", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "newOwner", "type": "address" }], "name": "transferOwnership", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "enum MonadAccess.ServiceType", "name": "service", "type": "uint8" }, { "internalType": "uint256", "name": "newPrice", "type": "uint256" }], "name": "updatePrice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "withdraw", "outputs": [], "stateMutability": "nonpayable", "type": "function" }];

// Service type enum (matches Solidity contract)
const ServiceType = {
    GPT_PRO: 0,
    GEMINI_AI: 1
};

// Export for use in HTML
if (typeof window !== 'undefined') {
    window.CONTRACT_ADDRESS = CONTRACT_ADDRESS;
    window.CONTRACT_ABI = CONTRACT_ABI;
    window.ServiceType = ServiceType;
}
