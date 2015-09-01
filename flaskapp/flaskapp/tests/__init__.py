import unittest

from .. import app, db


@app.cli.command()
def test():
    """Initialize the database."""
    from . import BasicTestCase
    unittest.main()