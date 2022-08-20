import subprocess
import unittest

import fixtup
from click.testing import CliRunner


class TestCli(unittest.TestCase):

    def setUp(self) -> None:
        self._runner = CliRunner()

    def test_fixtup_sqlalchemy_plugin_is_enable(self):
        # Assign
        with fixtup.up("fixtup-project"):
            # Acts
            output = subprocess.check_output(["fixtup", "info"])

            # Assert
            self.assertIn(b"* fixtup_sqlalchemy.plugin", output)

if __name__ == '__main__':
    unittest.main()
