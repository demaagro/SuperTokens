# test_supertokens.py
"""
Tests for SuperTokens module.
"""

import unittest
from supertokens import SuperTokens

class TestSuperTokens(unittest.TestCase):
    """Test cases for SuperTokens class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SuperTokens()
        self.assertIsInstance(instance, SuperTokens)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SuperTokens()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
