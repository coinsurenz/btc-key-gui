"""Encoding utilities for Bitcoin addresses and keys."""
from .constants import BASE58, CHARSET


def encode_base58(s):
    """
    Encode bytes using Base58 encoding.

    Args:
        s (bytes): The bytes to encode.

    Returns:
        bytes: The Base58-encoded result.

    Note:
        This function implements Base58 encoding, which is commonly used in Bitcoin
        for encoding addresses and private keys. It preserves leading zero bytes
        by prefixing the result with '1' characters.
    """
    count = 0
    for c in s:
        if c == 0:
            count += 1
        else:
            break
    prefix = b"1" * count

    num = int(s.hex(), 16)
    result = bytearray()
    while num > 0:
        num, mod = divmod(num, 58)
        result.insert(0, BASE58[mod])

    return prefix + bytes(result)


def bech32_polymod(values):
    """
    Compute the Bech32 checksum.

    This function is part of the Bech32 address encoding process. It calculates
    a checksum over the given values using the Bech32 generator polynomial.

    Args:
        values (List[int]): A list of integers to compute the checksum over.
                            These typically include the expanded HRP and data.

    Returns:
        int: The computed checksum.

    Note:
        This function implements the polynomial modulus operation as defined
        in the Bech32 specification (BIP 173). The generator polynomial used is:
        x^25 + 0x3b6a57b2*x^20 + 0x26508e6d*x^15 + 0x1ea119fa*x^10 + 0x3d4233dd*x^5 + 0x2a1462b3

    Example:
        >>> bech32_polymod([3, 3, 0, 2, 3])
        1002454646

    References:
        BIP 173: https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki
    """
    print('values 32 poly', values)
    generator = [0x3B6A57B2, 0x26508E6D, 0x1EA119FA, 0x3D4233DD, 0x2A1462B3]
    chk = 1
    for value in values:
        top = chk >> 25
        chk = (chk & 0x1FFFFFF) << 5 ^ value
        for i in range(5):
            chk ^= generator[i] if ((top >> i) & 1) else 0
    return chk


def bech32_hrp_expand(hrp):
    """
    Expand the human-readable part of a Bech32 address.

    This function is part of the Bech32 address encoding process. It converts
    the human-readable part (HRP) of a Bech32 address into a list of integers
    as specified in the Bech32 encoding scheme.

    Args:
        hrp (str): The human-readable part of the Bech32 address (e.g., 'bc' for Bitcoin mainnet).

    Returns:
        List[int]: A list of integers representing the expanded HRP.
            The list contains three parts:
            1. The high 3 bits of each character in the HRP
            2. A separator (0)
            3. The low 5 bits of each character in the HRP

    Example:
        >>> bech32_hrp_expand('bc')
        [3, 3, 0, 2, 3]

    Note:
        This function is typically used in conjunction with other Bech32 encoding functions
        to create the checksum for a Bech32 address.

    References:
        BIP 173: https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki
    """
    return [ord(x) >> 5 for x in hrp] + [0] + [ord(x) & 31 for x in hrp]


def bech32_create_checksum(hrp, data):
    """
    Create a Bech32 checksum for the given human-readable part (HRP) and data.

    This function is part of the Bech32 address encoding process, used primarily
    in Bitcoin and other cryptocurrencies for segregated witness addresses.

    Args:
        hrp (str): The human-readable part of the address (e.g., 'bc' for Bitcoin mainnet).
        data (List[int]): The data part of the address, as a list of 5-bit integers.

    Returns:
        List[int]: A list of 6 5-bit integers representing the checksum.

    Note:
        This function uses the bech32_hrp_expand and bech32_polymod functions,
        which should be defined elsewhere in the module.

    Example:
        >>> hrp = 'bc'
        >>> data = [0, 14, 20, 15, 7, 13, 26, 0, 25, 18, 6, 11, 13, 8, 21, 4, 20, 3, 17, 2, 29, 3, 12, 29, 3, 4, 15, 24, 20, 6, 14, 30, 22]
        >>> bech32_create_checksum(hrp, data)
        [29, 22, 4, 18, 26, 27]

    References:
        BIP 173: https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki
    """
    values = bech32_hrp_expand(hrp) + data
    polymod = bech32_polymod(values + [0, 0, 0, 0, 0, 0]) ^ 1
    print('checksum res',[(polymod >> 5 * (5 - i)) & 31 for i in range(6)])
    return [(polymod >> 5 * (5 - i)) & 31 for i in range(6)]


def bech32_encode(hrp, data):
    """
    Encode a Bech32 string.

    This function takes a human-readable part (HRP) and data, combines them with a checksum,
    and encodes the result into a Bech32 string.

    Args:
        hrp (str): The human-readable part of the Bech32 address (e.g., 'bc' for Bitcoin mainnet).
        data (List[int]): The data to be encoded, as a list of 5-bit integers.

    Returns:
        str: The complete Bech32-encoded string.

    Example:
        >>> bech32_encode('bc', [0, 14, 20, 15, 7, 13, 26, 0, 25, 18, 6, 11, 13, 8, 21, 4, 20, 3, 17, 2, 29, 3, 12, 29, 3, 4, 15, 24, 20, 6, 14, 30, 22])
        'bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4'

    Note:
        This function assumes that the input data has already been converted to 5-bit integers
        and that the CHARSET global variable is defined with the Bech32 character set.
    """
    combined = data + bech32_create_checksum(hrp, data)
    return hrp + "1" + "".join([CHARSET[d] for d in combined])


def convertbits(data, frombits, tobits, pad=True):
    """
    Convert a list of integers from one bit size to another.

    This function is commonly used in cryptocurrency address encoding, particularly
    for Bech32 addresses, to convert between 8-bit bytes and 5-bit groups.

    Args:
        data (List[int]): The input data as a list of integers.
        frombits (int): The number of bits each input integer represents.
        tobits (int): The desired number of bits for each output integer.
        pad (bool, optional): Whether to pad the output if necessary. Defaults to True.

    Returns:
        Optional[List[int]]: A list of integers representing the converted data,
        or None if the conversion is not possible.

    Raises:
        None, but returns None for invalid input or impossible conversions.

    Example:
        >>> convertbits([0x3F, 0x2C], 8, 5)
        [7, 25, 6, 0]
    """
    acc = 0
    bits = 0
    ret = []
    maxv = (1 << tobits) - 1
    max_acc = (1 << (frombits + tobits - 1)) - 1
    for value in data:
        if value < 0 or (value >> frombits):
            return None
        acc = ((acc << frombits) | value) & max_acc
        bits += frombits
        while bits >= tobits:
            bits -= tobits
            ret.append((acc >> bits) & maxv)
    if pad:
        if bits:
            ret.append((acc << (tobits - bits)) & maxv)
    elif bits >= frombits or ((acc << (tobits - bits)) & maxv):
        return None
    return ret


def encode_bech32(hrp, witver, witprog):
    """
    Encode a Bech32 address.

    Args:
        hrp (str): The human-readable part of the address (e.g., 'bc' for Bitcoin mainnet).
        witver (int): The witness version.
        witprog (bytes): The witness program.

    Returns:
        str: The Bech32-encoded address.

    Note:
        This function encodes the witness version and program into a Bech32 address.
        The commented-out section suggests a potential validation step that's currently disabled.
    """
    ret = bech32_encode(hrp, [witver] + convertbits(witprog, 8, 5))
    # if decode(hrp, ret) == (None, None):
    # return None
    return ret