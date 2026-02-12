import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720}, # Ekranni kattalashtirish
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "slow_mo": 1500, # Har bir amalni 1.5 soniyaga sekinlashtiradi
        "headless": False # Har doim brauzerni ko'rsatadi
    }