import logging

import dotenv

dotenv.load_dotenv()

from pythonseer import Fediseer


class Test:

    @classmethod
    def test_whitelist(cls):
        whitelist = Fediseer().whitelist
        data = whitelist.get(guarantors=3, endorsements=4)
        logging.debug(data)
        assert data is not None

    @classmethod
    def test_whitelist_args(cls):
        whitelist = Fediseer().whitelist
        data = whitelist.get(guarantors=3, endorsements=4, software='lemmy', domains=False, limit=50)
        logging.debug(data)
        assert data is not None
