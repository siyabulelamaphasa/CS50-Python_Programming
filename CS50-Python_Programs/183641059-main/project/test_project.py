import pytest
from project import get_crypto_price, buy_crypto, sell_crypto

# Test for cryptocurrency price retrieval
def test_get_crypto_price():
    btc_price = get_crypto_price('BTC')
    assert 30000 <= btc_price <= 60000

    eth_price = get_crypto_price('ETH')
    assert 1500 <= eth_price <= 4000

    ltc_price = get_crypto_price('LTC')
    assert 100 <= ltc_price <= 300

    unknown_price = get_crypto_price('XYZ')
    assert unknown_price is None

# Test for buying cryptocurrency
def test_buy_crypto(monkeypatch):
    # Mock input for buying cryptocurrency
    inputs = iter(['BTC', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    portfolio = {}
    history = []

    buy_crypto(portfolio, history)

    assert 'BTC' in portfolio
    assert portfolio['BTC'] == 1.0
    assert len(history) == 1
    assert history[0]['action'] == 'buy'
    assert history[0]['crypto'] == 'BTC'
    assert history[0]['amount'] == 1.0

# Test for selling cryptocurrency
def test_sell_crypto(monkeypatch):
    # Mock input for selling cryptocurrency
    inputs = iter(['BTC', '0.5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    portfolio = {'BTC': 1.0}
    history = []

    sell_crypto(portfolio, history)

    assert portfolio['BTC'] == 0.5
    assert len(history) == 1
    assert history[0]['action'] == 'sell'
    assert history[0]['crypto'] == 'BTC'
    assert history[0]['amount'] == 0.5
