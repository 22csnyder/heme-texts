#!/usr/bin/env python3
"""
Unit tests for Hogwarts house classification script
"""

import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the scripts directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from hw_mrvn import ai_hat, main


class TestHWMervn(unittest.TestCase):
    """Test cases for Hogwarts house classification"""
    
    @patch('hw_mrvn.marvin')
    def test_ai_hat_gryffindor(self, mock_marvin):
        """Test Gryffindor classification"""
        mock_marvin.classify.return_value = "Gryffindor"
        
        result = ai_hat("brave and courageous")
        
        self.assertEqual(result, "Gryffindor")
        mock_marvin.classify.assert_called_once_with(
            "brave and courageous",
            labels=["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        )
    
    @patch('hw_mrvn.marvin')
    def test_ai_hat_slytherin(self, mock_marvin):
        """Test Slytherin classification"""
        mock_marvin.classify.return_value = "Slytherin"
        
        result = ai_hat("ambitious and cunning")
        
        self.assertEqual(result, "Slytherin")
        mock_marvin.classify.assert_called_once_with(
            "ambitious and cunning",
            labels=["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        )
    
    @patch('hw_mrvn.marvin')
    def test_ai_hat_ravenclaw(self, mock_marvin):
        """Test Ravenclaw classification"""
        mock_marvin.classify.return_value = "Ravenclaw"
        
        result = ai_hat("intelligent and wise")
        
        self.assertEqual(result, "Ravenclaw")
        mock_marvin.classify.assert_called_once_with(
            "intelligent and wise",
            labels=["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        )
    
    @patch('hw_mrvn.marvin')
    def test_ai_hat_hufflepuff(self, mock_marvin):
        """Test Hufflepuff classification"""
        mock_marvin.classify.return_value = "Hufflepuff"
        
        result = ai_hat("loyal and hardworking")
        
        self.assertEqual(result, "Hufflepuff")
        mock_marvin.classify.assert_called_once_with(
            "loyal and hardworking",
            labels=["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        )
    
    @patch('hw_mrvn.marvin')
    def test_main_function(self, mock_marvin):
        """Test main function wrapper"""
        mock_marvin.classify.return_value = "Gryffindor"
        
        result = main("test description")
        
        self.assertEqual(result, "Gryffindor")
        mock_marvin.classify.assert_called_once_with(
            "test description",
            labels=["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        )
    
    @patch('hw_mrvn.marvin')
    def test_ai_hat_empty_string(self, mock_marvin):
        """Test handling of empty string input"""
        mock_marvin.classify.return_value = "Hufflepuff"
        
        result = ai_hat("")
        
        self.assertEqual(result, "Hufflepuff")
        mock_marvin.classify.assert_called_once_with(
            "",
            labels=["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        )


if __name__ == '__main__':
    unittest.main()
