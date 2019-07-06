import pytest
from ..src import encoder


def test_valid_encoding():
    """Ensure that the encoder is creating a string with characters matching the input.
    Also make sure that a valid amount of symbols are being used.
    """
    test_string = "NatIon"
    encoded, elements = encoder.encode(test_string)
    assert encoded.lower() == test_string.lower()
    assert len(test_string) / 2 <= len(elements) <= len(test_string)


def test_invalid_encoding():
    """Ensure that the encoder throws the correct error when a string cannot be
    encoded.
    """
    test_string = "nathan"
    with pytest.raises(encoder.SymbolError):
        assert encoder.encode(test_string)


def test_avoid_repetitions():
    """Ensure that the encoder uses different substitutions where possible."""
    short_string = "fer"
    encoded_short, _ = encoder.encode(short_string)
    encoded_long, _ = encoder.encode(short_string * 3)
    assert encoded_long != encoded_short * 3
