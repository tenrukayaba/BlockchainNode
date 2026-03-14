# test_blockchainnodeapi.py
"""
Tests for BlockchainNodeApi module.
"""

import unittest
from blockchainnodeapi import BlockchainNodeApi

class TestBlockchainNodeApi(unittest.TestCase):
    """Test cases for BlockchainNodeApi class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainNodeApi()
        self.assertIsInstance(instance, BlockchainNodeApi)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainNodeApi()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
