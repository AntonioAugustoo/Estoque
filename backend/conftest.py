import pytest


pytest_plugins = ("anyio",)


def pytest_configure(config):
    config.addinivalue_line("markers", "anyio: mark test to run with anyio")


@pytest.fixture(scope="session")
def anyio_backend():
    """Force asyncio backend instead of trio to avoid event loop conflicts"""
    return "asyncio"
