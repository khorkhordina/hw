import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://api.openbrewerydb.org/v1",
        help="Base URL for Brewery API"
    )

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="session")
def headers():
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Brewery-Testing/1.0"
    }