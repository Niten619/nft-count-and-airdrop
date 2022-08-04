from theblockchainapi import SolanaAPIResource, SolanaNetwork
import subprocess
from solana.publickey import PublicKey
from solana.rpc.api import Client

# solana_client = Client("https://api.devnet.solana.com")
# solana_client.get_token_accounts_by_owner(PublicKey("uyZFLgTNT2j6enw7wUKbawBJdB7Hj5tqVMUxN6TgV9x"), opts="")

# Key Id: TJ1ZdOdlxTaFhjP
# Secret Key: TeNteiDOFhF2xma
MY_API_KEY_ID = "TJ1ZdOdlxTaFhjP"
MY_API_SECRET_KEY = "TeNteiDOFhF2xma"
MAD_token_mint_address = "GkXn6PUbcvpwAzVCgJFychVhAhjwZRMJWmtqzar3SnqG"

BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)


def search_nft():
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key id pair!!!")

    # mint_address = "GkXn6PUbcvpwAzVCgJFychVhAhjwZRMJWmtqzar3SnqG"
    # nfts = BLOCKCHAIN_API_RESOURCE.search_nfts(
    #     mint_address=mint_address,
    #     network=SolanaNetwork.MAINNET_BETA
    # )
    # print(f"Found {len(nfts)} NFT with the mint address '{mint_address}'")

    # update_authority = 'Hrig8yUG2GJPtNvMDsDDTbAxFNw3xyRVRWmXM4nqawpd'
    update_authority = "uyZFLgTNT2j6enw7wUKbawBJdB7Hj5tqVMUxN6TgV9x"
    nfts = BLOCKCHAIN_API_RESOURCE.search_nfts(
        update_authority=update_authority,
        network=SolanaNetwork.MAINNET_BETA
    )
    print("-" * 50)
    print(f"Found {len(nfts)} NFT(s) with an `update_authority` of `{update_authority}`.")
    for nft in nfts:
        print(nft)
    print("-" * 50)

    # Conditions:
    # When a wallet holds between 1-4 NFTs, they get airdropped 2 MAD tokens
    # When a wallet holds between 5-9 NFTs, they get airdropped 12 MAD tokens
    # When a wallet holds between 10 or more NFTs, they get airdropped 40 MAD tokens

    if 1 <= len(nfts) <= 4:
        print("Airdropping 2 MAD Tokens")
        transferLogs = subprocess.run(
            ["spl-token", "transfer", "--fund-recipient", MAD_token_mint_address, 2, update_authority],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(transferLogs.stdout + transferLogs.stderr)
    elif 5 <= len(nfts) <= 9:
        print("Airdropping 12 MAD Tokens")
        transferLogs = subprocess.run(
            ["spl-token", "transfer", "--fund-recipient", MAD_token_mint_address, 12, update_authority],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(transferLogs.stdout + transferLogs.stderr)
    elif len(nfts) >= 10:
        print("Airdropping 40 MAD Tokens")
        transferLogs = subprocess.run(
            ["spl-token", "transfer", "--fund-recipient", MAD_token_mint_address, 40, update_authority],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(transferLogs.stdout + transferLogs.stderr)


if __name__ == '__main__':
    search_nft()







