from custom_provider import BaseProvider, MarketProvider
from faker import Faker

fake = Faker()
fake.add_provider(MarketProvider)


def test_MarketProvider_is_a_faker_provider():
    assert issubclass(MarketProvider, BaseProvider)


def test_faker_return_a_value_with_the_new_provider():
    result = fake.product

    assert result != None
