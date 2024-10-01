from src.crypto import hash160, create_checksum
from src.constants import OpCode

TEST_PUBKEY = bytes.fromhex(
    "036889e5873ed5a78666cde9b0f623d0bde8807ecda551222e2943800b0fb1e47d"
)
TEST_PRIVKEY = bytes.fromhex(
    "ce815918fd4e77328f3c5b696081d9d4ff478a7c07cfb9b443aa34e52284d670"
)
TEST_PREFIX = bytes.fromhex("00")
TEST_PUBKEY_HASH = hash160(TEST_PUBKEY)
TEST_CHECKSUM = create_checksum(TEST_PREFIX + TEST_PUBKEY_HASH)
TEST_PUBKEY_HASH_LEN = bytes([len(TEST_PUBKEY_HASH)])
TEST_P2SH_REDEEMSCRIPT = hash160(
    OpCode.OP_0.value + bytes([len(TEST_PUBKEY_HASH)]) + TEST_PUBKEY_HASH
)
TEST_P2SH_REDEEMSCRIPT_LEN = bytes([len(TEST_P2SH_REDEEMSCRIPT)])
TEST_P2SH_BYTES = bytes.fromhex(
    "21036889e5873ed5a78666cde9b0f623d0bde8807ecda551222e2943800b0fb1e47dac"
)
TEST_FINGERPRINT = b"2aae3e30"
TEST_SEED = "test seed"
TEST_PASSPHRASE = "test passphrase"
TEST_CHAINCODE = b"chaincode" * 4
