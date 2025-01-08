import os
import pytest
import sqlite3


@pytest.fixture(scope="session")
def change_to_root_directory():
    original_dir = os.getcwd()
    os.chdir(os.path.dirname(os.getcwd()))
    yield
    os.chdir(original_dir)
