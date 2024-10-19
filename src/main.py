import asyncio

from loguru import logger

from core.aevo import AevoClient


async def main():
    # The following values which are used for authentication on private endpoints, can be retrieved from the Aevo UI
    aevo = AevoClient(
        signing_key="",
        wallet_address="",
        api_key="",
        api_secret="",
        env="testnet",
    )

    markets = aevo.get_markets("ETH")
    logger.info(markets)

    await aevo.open_connection()
    await aevo.subscribe_ticker("ticker:ETH:PERPETUAL")

    async for msg in aevo.read_messages():
        logger.info(msg)


if __name__ == "__main__":
    asyncio.run(main())