import pytest
from hexorcist import (
    to_decimal,
    from_decimal,
    validate_number_string,
    validate_base,
    validate_different_bases
)


def test_to_decimal_base_2():
    """Ensure conversion from base 2 works correctly."""
    result = to_decimal("1010", 2)
    assert result == 10 


def test_to_decimal_base_16():
    """Ensure hexadecimal to decimal conversion works correctly."""
    result = to_decimal("1A", 16)
    assert result == 26 


def test_from_decimal_base_2():
    """Ensure conversion to base 2 works correctly."""
    result = from_decimal(10, 2)
    assert result == "1010"


def test_from_decimal_base_16():
    """Ensure conversion to base 16 works correctly."""
    result = from_decimal(26, 16)
    assert result == "1A"


def test_from_decimal_zero():
    """Ensure converting zero returns '0'."""
    result = from_decimal(0, 10)
    assert result == "0"


def test_from_decimal_invalid_base_low():
    """Ensure ValueError is raised for base less than 2."""
    with pytest.raises(ValueError):
        from_decimal(10, 1) 


def test_from_decimal_invalid_base_high():
    """Ensure ValueError is raised for base greater than 36."""
    with pytest.raises(ValueError):
        from_decimal(10, 37)


def test_validate_number_string_valid():
    """Ensure valid characters pass the validation."""
    result = validate_number_string("123ABC")
    assert result == []


def test_validate_number_string_invalid():
    """Ensure invalid characters are detected."""
    result = validate_number_string("123G$")
    assert result == ["$"]  


def test_round_trip_conversion():
    """Ensure converting to decimal and back returns the original string."""
    original = "101011"
    dec = to_decimal(original, 2)
    back = from_decimal(dec, 2)
    assert back == original


def test_case_insensitivity_in_to_decimal():
    """Ensure lowercase letters work same as uppercase."""
    result_upper = to_decimal("1A", 16)
    result_lower = to_decimal("1a", 16)
    assert result_upper == result_lower


def test_validate_base_valid():
    """Ensure valid bases pass validation."""
    assert validate_base(2) is True
    assert validate_base(10) is True
    assert validate_base(36) is True


def test_validate_base_invalid_low():
    """Ensure ValueError is raised for base less than 2."""
    with pytest.raises(ValueError):
        validate_base(1)


def test_validate_base_invalid_high():
    """Ensure ValueError is raised for base greater than 36."""
    with pytest.raises(ValueError):
        validate_base(37)


def test_validate_base_invalid_type():
    """Ensure ValueError is raised for non-integer bases."""
    with pytest.raises(ValueError):
        validate_base("ten")


def test_validate_different_bases_same():
    """Ensure ValueError is raised if original and new bases are the same."""
    with pytest.raises(ValueError, match="New base must be different from original base"):
        validate_different_bases(10, 10)


def test_validate_different_bases_different():
    """Ensure no error is raised if original and new bases are different."""
    assert validate_different_bases(10, 16) is True
