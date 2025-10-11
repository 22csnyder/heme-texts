#!/usr/bin/env python3
"""
Unit tests for AI polishing script
"""

import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the scripts directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# Import after path modification
from ai_script import get_polish_prompt, polish_text


class TestAIPolish(unittest.TestCase):
    """Test cases for AI polishing functionality"""
    
    def test_get_polish_prompt_path_style(self):
        """Test path style prompt generation"""
        text = "sections show atypical cells"
        prompt = get_polish_prompt(text, "path")
        
        self.assertIn("hematopathologist assistant", prompt)
        self.assertIn("pathology report format", prompt)
        self.assertIn("sections show atypical cells", prompt)
        self.assertIn("Do NOT include any explanatory text", prompt)
    
    def test_get_polish_prompt_flow_style(self):
        """Test flow style prompt generation"""
        text = "CD19, CD20, CD5"
        prompt = get_polish_prompt(text, "flow")
        
        self.assertIn("flow cytometry reports", prompt)
        self.assertIn("immunophenotype description", prompt)
        self.assertIn("CD19, CD20, CD5", prompt)
        self.assertIn("Do NOT include any explanatory text", prompt)
    
    def test_get_polish_prompt_email_style(self):
        """Test email style prompt generation"""
        text = "need to tell team case is ready"
        prompt = get_polish_prompt(text, "email")
        
        self.assertIn("professional email assistant", prompt)
        self.assertIn("concise, professional, and courteous", prompt)
        self.assertIn("need to tell team case is ready", prompt)
        self.assertIn("Do NOT include any explanatory text", prompt)
    
    def test_get_polish_prompt_default_style(self):
        """Test default style (path) when no style specified"""
        text = "test text"
        prompt = get_polish_prompt(text)
        
        self.assertIn("hematopathologist assistant", prompt)
        self.assertIn("pathology report format", prompt)
    
    def test_get_polish_prompt_unknown_style(self):
        """Test fallback to path style for unknown style"""
        text = "test text"
        prompt = get_polish_prompt(text, "unknown_style")
        
        self.assertIn("hematopathologist assistant", prompt)
        self.assertIn("pathology report format", prompt)
    
    @patch('ai_script.client')
    def test_polish_text_success(self, mock_client):
        """Test successful text polishing"""
        # Mock the OpenAI response
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Polished text"
        mock_client.chat.completions.create.return_value = mock_response
        
        result = polish_text("test input", "path")
        
        self.assertEqual(result, "Polished text")
        mock_client.chat.completions.create.assert_called_once()
    
    @patch('ai_script.client')
    def test_polish_text_api_error(self, mock_client):
        """Test handling of API errors"""
        # Mock an API error
        mock_client.chat.completions.create.side_effect = Exception("API Error")
        
        result = polish_text("test input", "path")
        
        self.assertEqual(result, "Error: API Error")
    
    def test_polish_prompt_includes_text(self):
        """Test that the prompt includes the input text"""
        test_text = "This is a test case with specific content"
        prompt = get_polish_prompt(test_text, "path")
        
        self.assertIn(test_text, prompt)
        self.assertTrue(prompt.endswith(f"\n\n{test_text}"))


if __name__ == '__main__':
    unittest.main()
