import { ethers } from "hardhat";
import fs from "fs";

async function main() {
    console.log("🚀 Deploying MonadAccess contract to Monad Testnet (V2)...\n");

    try {
        // Get deployer account
        const [deployer] = await ethers.getSigners();
        console.log("📝 Deploying with account:", deployer.address);

        // Deploy contract
        const MonadAccess = await ethers.getContractFactory("MonadAccess");
        console.log("⏳ Deploying contract...");

        const contract = await MonadAccess.deploy();
        await contract.waitForDeployment();

        const contractAddress = await contract.getAddress();
        console.log("✅ MonadAccess deployed to:", contractAddress);

        // Get initial prices
        const gptPrice = await contract.getPrice(0); // GPT_PRO
        const geminiPrice = await contract.getPrice(1); // GEMINI_AI
        const bgPrice = await contract.getPrice(2); // BG_REMOVER
        const imgPrice = await contract.getPrice(3); // IMAGE_GENERATOR

        console.log("\n📊 Service Prices:");
        console.log("   GPT-Pro:", ethers.formatEther(gptPrice), "MON");
        console.log("   Gemini AI:", ethers.formatEther(geminiPrice), "MON");
        console.log("   BG Remover:", ethers.formatEther(bgPrice), "MON");
        console.log("   Image Gen:", ethers.formatEther(imgPrice), "MON");

        // Save contract address and ABI
        const deploymentInfo = {
            address: contractAddress,
            deployer: deployer.address,
            network: "monad-testnet",
            chainId: 10143,
            deployedAt: new Date().toISOString()
        };

        fs.writeFileSync(
            "contract-address.json",
            JSON.stringify(deploymentInfo, null, 2)
        );

        console.log("\n📁 Saved contract address to: contract-address.json");

    } catch (error) {
        console.error("❌ Deployment failed:", error);
    }
}

main();
