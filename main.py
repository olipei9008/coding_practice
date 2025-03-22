import pytest
import os

if __name__ == "__main__":
    print("Hello World!")
    curr = os.getcwd()
    pytest.main(["test"])