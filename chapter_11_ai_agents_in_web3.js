// Step 3: Enable Web3 Transactions (Buying NFTs in the Metaverse)

const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

// Function to complete a transaction
async function buyNFT(buyer, seller, price) {
    const transaction = await web3.eth.sendTransaction({
        from: buyer,
        to: seller,
        value: web3.utils.toWei(price, 'ether')
    });
    console.log("Transaction successful:", transaction);
}

// Example: Buy an NFT for 0.1 ETH
buyNFT('0xBuyerAddress', '0xSellerAddress', '0.1');
