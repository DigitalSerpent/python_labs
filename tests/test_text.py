import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


def test_normalize_basic():
    """нормалайз"""
    result = normalize("ПрИвЕт\nМИр\t")
    assert result == "привет мир"


def test_normalize_yo():
    """ё"""
    result = normalize("ёжик Ёлка")
    assert result == "ежик елка"


def test_tokenize_basic():
    """токенайз"""
    text = normalize("привет мир")
    result = tokenize(text)
    assert result == ["привет", "мир"]


def test_count_freq():
    """частота"""
    tokens = ["я", "люблю", "python", "python"]
    result = count_freq(tokens)
    assert result == {"я": 1, "люблю": 1, "python": 2}


def test_top_n():
    """топ-N"""
    freq = {"я": 1, "люблю": 3, "python": 2}
    result = top_n(freq, 2)
    assert result == [("люблю", 3), ("python", 2)]
