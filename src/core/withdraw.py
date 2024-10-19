from core.eip712_structs import Address, Bytes, EIP712Struct, Uint


class Withdraw(EIP712Struct):
    collateral = Address()
    to = Address()
    amount = Uint(256)
    salt = Uint(256)
    data = Bytes(32)
