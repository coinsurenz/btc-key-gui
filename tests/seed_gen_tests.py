"""Tests for seed generation functions"""

import binascii
import hashlib
import hmac
import pytest
from unittest.mock import patch, Mock
from src.seed_gen import (
    path_gen_keylist,
    seed_to_master,
    generate_seed,
    derive_master_keys,
    Keylevel,
    generate_master_pubkey,
)
from src.constants import AddressType
from src.ecdsa_functions import G
from tests.test_constants import (
    TEST_SEED,
    TEST_PASSPHRASE,
)

fake_CKCpriv = b"cd548baa8815d329d2c200d7030584739b67082a0466630ec616438ee65d308c"
fake_CKDpriv = b"a34abca0c375fae6bd04e055d37bf83fd04151da895945070233d0c6a34926fd"
fake_pubkey = b"0385cfdcfebf4fe35cc4b53bc7ab8210b4a22443e56a080510269b938f5b059e5d"
fake_fingerprint = b"4e92cd15"
fake_fprint = b"2aae3e30"
fake_xprv = b"xprvA183oqPmH26ACRheyXqypcZat16XmtKrWiiHQSJTQNr5rE8oqhiwM4QYwSUFC3ojCAimngRJ3Tc9yTpQ55cwBLnNUw4pyJz96Vjcsp3bxGp"
fake_xpub = b"xpub6E7QDLvf7PeTQun85ZNzBkWKS2w2BM3hswdtCpi4xiP4j2TxPF3Btrj2njDmnPX61F7EjicV8U6ivgJtFDWxapu4ujp8BS1VuYGKrjWd1Fp"


class MockKeylevel:

    def __init__(self, *args, **kwargs):
        self.CKCpriv = Mock(return_value=fake_CKCpriv)
        self.CKDpriv = Mock(return_value=fake_CKDpriv)
        self.pubkey = Mock(return_value=fake_pubkey)
        self.fprint = Mock(return_value=fake_fprint)
        self.fingerprint = Mock(return_value=fake_fingerprint)
        self.xprv = Mock(return_value=fake_xprv)
        self.xpub = Mock(return_value=fake_xpub)


@pytest.fixture
def mock_dependencies(monkeypatch):
    monkeypatch.setattr("src.seed_gen.Keylevel", MockKeylevel)
    monkeypatch.setattr(
        "src.seed_gen.convert_pubkey_to_pubdata",
        Mock(return_value=("mock_public", "mock_script_pub", "mock_signscript")),
    )
    monkeypatch.setattr(
        "src.seed_gen.indv_priv_key", Mock(return_value=b"mock_priv_key")
    )
    monkeypatch.setattr("src.seed_gen.string_to_int", Mock(return_value=12345))


@pytest.mark.usefixtures("mock_dependencies")
def test_path_gen_keylist_basic():
    result = path_gen_keylist(
        master_cc=b"be09f51322ff1a104a66ae7b661739ee6601682337fbcd43141059edf21c732f",
        master_pk=b"a7353257b7a9a1b89b1c9afaef86a2415c24ee8c5a6bc9238a66ea7e9332c845",
        master_pubkey=b"03de4706b974c52e9a6d6b6292536b9cd3cbd70a8529ff0ea761175745ce94130f",
        derivation_path=["1"],
        hardened_list=[True],
        total_keys=2,
        address_type="p2pkh",
        is_testnet=True,
    )

    assert isinstance(result, list)
    assert len(result) == 2
    for item in result:
        assert isinstance(item, str)
        assert f"XPRV={fake_xprv.decode('utf-8')}" in item
        assert f"XPUB={fake_xpub.decode('utf-8')}" in item
        assert "DERIVATION PATH=m/1h" in item
        assert "privatekey=mock_priv_key" in item
        assert (
            "Private hex=61333461626361306333373566616536626430346530353564333762663833666430343135316461383935393435303730323333643063366133343932366664"
            in item
        )
        assert "Private scalar=12345" in item
        assert "publickey=mock_public" in item
        assert (
            "public point=303338356366646366656266346665333563633462353362633761623832313062346132323434336535366130383035313032363962393338663562303539653564"
            in item
        )
        assert "Script Pubkey=mock_script_pub" in item


@pytest.mark.usefixtures("mock_dependencies")
def test_path_gen_keylist_different_address_types():
    for address_type in ["p2pkh", "p2sh", "p2wpkh-p2sh", "p2wpkh", "p2wsh"]:
        result = path_gen_keylist(
            master_cc=b"mock_cc",
            master_pk=b"mock_pk",
            master_pubkey=b"mock_pubkey",
            derivation_path=[
                "0",
                "0",
                "0",
            ],
            hardened_list=[False, True, True],
            total_keys=2,
            address_type=address_type,
            is_testnet=True,
        )

        assert len(result) == 2
        if address_type in ["p2sh", "p2wpkh-p2sh", "p2wsh", "p2wpkh"]:
            assert "Scriptpub to sign=mock_signscript" in result[0]
        else:
            assert "Scriptpub to sign=" not in result[0]


@pytest.mark.usefixtures("mock_dependencies")
def test_path_gen_keylist_different_depths():
    for depth in range(1, 5):
        result = path_gen_keylist(
            master_cc=b"mock_cc",
            master_pk=b"mock_pk",
            master_pubkey=b"mock_pubkey",
            derivation_path=list(range(depth)),
            hardened_list=[False] * (depth),
            total_keys=1,
            address_type="p2pkh",
            is_testnet=True,
        )

        assert len(result) == 1
        expected_path = "m/" + "/".join(map(str, range(depth)))
        assert f"DERIVATION PATH={expected_path}" in result[0]


@pytest.mark.usefixtures("mock_dependencies")
def test_path_gen_keylist_hardened_paths():
    result = path_gen_keylist(
        master_cc=b"mock_cc",
        master_pk=b"mock_pk",
        master_pubkey=b"mock_pubkey",
        derivation_path=[0, 1, 2],
        hardened_list=[False, True, False],
        total_keys=1,
        address_type="p2pkh",
        is_testnet=True,
    )

    assert len(result) == 1
    assert "DERIVATION PATH=m/0/1h/2" in result[0]


@pytest.mark.usefixtures("mock_dependencies")
def test_path_gen_keylist_multiple_keys():
    result = path_gen_keylist(
        master_cc=b"mock_cc",
        master_pk=b"mock_pk",
        master_pubkey=b"mock_pubkey",
        derivation_path=[0],
        hardened_list=[False, False],
        total_keys=5,
        address_type="p2pkh",
        is_testnet=True,
    )
    assert len(result) == 5
    for i, item in enumerate(result):
        assert f"KEY INDEX={i}" in item

keylevel_chaincode = binascii.unhexlify('cd548baa8815d329d2c200d7030584739b67082a0466630ec616438ee65d308c'.encode("utf8"))
keylevel_priv_key = binascii.unhexlify('a34abca0c375fae6bd04e055d37bf83fd04151da895945070233d0c6a34926fd'.encode("utf8"))
keylevel_pub_key = binascii.unhexlify('0385cfdcfebf4fe35cc4b53bc7ab8210b4a22443e56a080510269b938f5b059e5d'.encode("utf8"))
keylevel_fingerprint = binascii.unhexlify('4e92cd15'.encode("utf8"))
@pytest.fixture
def keylevel_instance():

    return Keylevel(
        input_chaincode=keylevel_chaincode,
        input_priv_key=keylevel_priv_key,
        input_pub_key=keylevel_pub_key,
        index=0,
        hardened=False,
        depth=5,
        input_fingerprint=keylevel_fingerprint,
        address_type=AddressType.P2PKH.value,
        is_testnet=False,
    )


def test_keylevel_initialization(keylevel_instance):
    assert keylevel_instance.input_chaincode == keylevel_chaincode
    assert keylevel_instance.input_priv_key ==keylevel_priv_key
    assert keylevel_instance.input_pub_key == keylevel_pub_key
    assert keylevel_instance.index == 0
    assert keylevel_instance.hardened == False
    assert keylevel_instance.depth == 5
    assert keylevel_instance.input_fingerprint == keylevel_fingerprint
    assert keylevel_instance.address_type == AddressType.P2PKH.value
    assert keylevel_instance.testnet == False
    CKCpriv = "08136199de7dc04ecb603fc510cc2c252ededfdefb97a813100d8b64d8d6d5be"
    CKDpriv = "ce815918fd4e77328f3c5b696081d9d4ff478a7c07cfb9b443aa34e52284d670"
    pubkey = "036889e5873ed5a78666cde9b0f623d0bde8807ecda551222e2943800b0fb1e47d"
    fingerprint = "2aae3e30"
    xprv = b"xprvA2jtBSZAwQNg7j63ijP3AkcbGQKRTfGpNgPUM4KjaMfmB6iWupegMaoYzqpZtAszAcXcT2179sqSaBoAt624zWSgVfdkPPFWYyrvwNkhKWj"
    xpub = b"xpub6FjEax64mmvyLDAWpkv3XtZKpS9us7zfjuK59SjM8hCk3u3fTMxvuP82r82AuEYf1SYXkz8k1ZGJubN3cEQebuQ9skDVVoXTpUzDBaRDZJF"
    assert keylevel_instance.CKDpriv() == binascii.unhexlify(CKDpriv.encode("utf8"))
    assert keylevel_instance.CKCpriv() == binascii.unhexlify(CKCpriv.encode("utf8"))
    assert keylevel_instance.pubkey() == binascii.unhexlify(pubkey.encode("utf8"))
    assert keylevel_instance.fingerprint()== binascii.unhexlify(fingerprint.encode("utf8"))
    assert keylevel_instance.xprv() == xprv
    assert keylevel_instance.xpub() == xpub

@pytest.mark.parametrize(
    "address_type",
    [
        AddressType.P2PKH.value,
        AddressType.P2SH.value,
        AddressType.P2WPKH.value,
        AddressType.P2WSH.value,
        AddressType.P2WPKH_P2SH.value,
    ],
)
def test_different_address_types(keylevel_instance, address_type):
    keylevel_instance.address_type = address_type
    xprv = keylevel_instance.xprv()
    xpub = keylevel_instance.xpub()
    assert isinstance(xprv, bytes)
    assert isinstance(xpub, bytes)


def test_testnet_mainnet_difference(keylevel_instance):
    keylevel_instance.testnet = True
    testnet_xprv = keylevel_instance.xprv()
    testnet_xpub = keylevel_instance.xpub()

    keylevel_instance.testnet = False
    mainnet_xprv = keylevel_instance.xprv()
    mainnet_xpub = keylevel_instance.xpub()

    assert testnet_xprv != mainnet_xprv
    assert testnet_xpub != mainnet_xpub


@patch("src.seed_gen.generate_seed")
@patch("src.seed_gen.derive_master_keys")
@patch("src.seed_gen.generate_master_pubkey")
@patch("src.seed_gen.path_gen_keylist")
def test_seed_to_master(
    mock_path_gen_keylist,
    mock_generate_master_pubkey,
    mock_derive_master_keys,
    mock_generate_seed,
):
    mock_generate_seed.return_value = b"seed_bytes"
    mock_derive_master_keys.return_value = (b"master_pk", b"master_cc")
    mock_generate_master_pubkey.return_value = b"master_pubkey"
    mock_path_gen_keylist.return_value = ["key1", "key2"]

    result = seed_to_master(
        TEST_SEED, TEST_PASSPHRASE, [0, 1], [False, True], 2, "p2pkh", True
    )

    assert result == ["key1", "key2"]
    mock_generate_seed.assert_called_once_with(TEST_SEED, TEST_PASSPHRASE)
    mock_derive_master_keys.assert_called_once_with(b"seed_bytes")
    mock_generate_master_pubkey.assert_called_once_with(b"master_pk")
    mock_path_gen_keylist.assert_called_once_with(
        b"master_cc",
        b"master_pk",
        b"master_pubkey",
        [0, 1],
        [False, True],
        2,
        "p2pkh",
        True,
    )


@patch("src.seed_gen.PBKDF2")
def test_generate_seed(mock_PBKDF2):
    mock_PBKDF2.return_value.read.return_value = b"generated_seed"
    result = generate_seed(TEST_SEED, TEST_PASSPHRASE)
    assert result == b"generated_seed"
    mock_PBKDF2.assert_called_once_with(
        TEST_SEED,
        f"mnemonic{TEST_PASSPHRASE}",
        iterations=2048,
        macmodule=hmac,
        digestmodule=hashlib.sha512,
    )


def test_derive_master_keys():
    seed_bytes = b"test_seed_bytes"
    expected_hmac = hmac.new(
        key=b"Bitcoin seed", msg=seed_bytes, digestmod=hashlib.sha512
    ).digest()
    master_pk, master_cc = derive_master_keys(seed_bytes)
    assert master_pk == expected_hmac[:32]
    assert master_cc == expected_hmac[32:]


@patch("src.seed_gen.S256Point.sec")
@patch("src.seed_gen.string_to_int")
def test_generate_master_pubkey(mock_string_to_int, mock_sec):
    mock_string_to_int.return_value = 123
    mock_sec.return_value = b"master_pubkey"
    result = generate_master_pubkey(b"master_pk")
    assert result == b"master_pubkey"
    mock_string_to_int.assert_called_once_with(b"master_pk")
    mock_sec.assert_called_once_with(123 * G)
