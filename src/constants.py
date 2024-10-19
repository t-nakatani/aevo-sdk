CONFIG = {
    "testnet": {
        "rest_url": "https://api-testnet.aevo.xyz",
        "ws_url": "wss://ws-testnet.aevo.xyz",
        "signing_domain": {
            "name": "Aevo Testnet",
            "version": "1",
            "chainId": "11155111",
        },
    },
    "mainnet": {
        "rest_url": "https://api.aevo.xyz",
        "ws_url": "wss://ws.aevo.xyz",
        "signing_domain": {
            "name": "Aevo Mainnet",
            "version": "1",
            "chainId": "1",
        },
    },
}

ADDRESSES = {
    "testnet": {
        "l1_bridge": "0xb459023ECAf4ee7E55BEC136e592d2B7afF482E2",
        "l1_usdc": "0xcC3e3DBb31a7410e1dc5156593CdBFA0616BB309",
        "l2_withdraw_proxy": "0x870b65A0816B9e9A0dFCE08Fd18EFE20f245011f",
        "l2_usdc": "0x52623B37Ff81c53567D6D16fd94638734cCDCf27",
    },
    "mainnet": {
        "l1_bridge": "0x4082C9647c098a6493fb499EaE63b5ce3259c574",
        "l1_usdc": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        "l2_withdraw_proxy": "0x4d44B9AbB13C80d2E376b7C5c982aa972239d845",
        "l2_usdc": "0x643aaB1618c600229785A5E06E4b2d13946F7a1A",
    },
}
