import hre from "hardhat";
import fs from "fs";

async function main() {
    console.log("🚀 Deploying MonadAccess contract to Monad Testnet...\n");

    // Get deployer account
    const [deployer] = await hre.ethers.getSigners();
    console.log("📝 Deploying with account:", deployer.address);

    const balance = await hre.ethers.provider.getBalance(deployer.address);
    console.log("💰 Account balance:", hre.ethers.formatEther(balance), "MON\n");

    // Deploy contract
    const MonadAccess = await hre.ethers.getContractFactory("MonadAccess");
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
    console.log("   GPT-Pro:", hre.ethers.formatEther(gptPrice), "MON");
    console.log("   Gemini AI:", hre.ethers.formatEther(geminiPrice), "MON");
    console.log("   BG Remover:", hre.ethers.formatEther(bgPrice), "MON");
    console.log("   Image Gen:", hre.ethers.formatEther(imgPrice), "MON");

    console.log("\n👤 Contract Owner:", await contract.owner());

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

    // Copy ABI to frontend-friendly location
    const artifact = await hre.artifacts.readArtifact("MonadAccess");
    fs.writeFileSync(
        "contract-abi.json",
        JSON.stringify(artifact.abi, null, 2)
    );

    console.log("\n📁 Saved contract address to: contract-address.json");
    console.log("📁 Saved contract ABI to: contract-abi.json");

    console.log("\n🎉 Deployment complete!");
    console.log("\n🔗 View on Monad Explorer:");
    console.log(`   https://testnet.monadexplorer.com/address/${contractAddress}`);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error("❌ Deployment failed:");
        console.error(error);
        process.exitCode = 1;
    });
