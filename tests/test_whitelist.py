import logging

import dotenv

dotenv.load_dotenv()


class Test:
    @classmethod
    def test_pull(cls):
        print("hi")
