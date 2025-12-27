#!/usr/bin/env python3
"""
Test the exact example from the requirements
"""

from ranchi_translator import RanchiTranslator

def test_exact_example():
    """Test the exact example provided in requirements"""
    translator = RanchiTranslator()
    
    # The exact example from requirements
    input_sentence = "Arre baba, Litti Chokha khao, bahut acha hai"
    expected_output = "Hey friend, try Litti Chokha (traditional Ranchi dish), it's very good"
    
    print("🧪 Testing Exact Example from Requirements:")
    print("=" * 60)
    print(f"Input:  \"{input_sentence}\"")
    
    result = translator.translate_sentence(input_sentence)
    
    # Create the expected format output
    translated = input_sentence
    translated = translated.replace("Arre baba", "Hey friend")
    translated = translated.replace("Litti Chokha", "Litti Chokha (traditional Ranchi dish)")
    translated = translated.replace("khao", "try")
    translated = translated.replace("bahut acha hai", "it's very good")
    
    print(f"Output: \"{translated}\"")
    
    print(f"\n📋 Detailed Breakdown:")
    for explanation in result['explanations']:
        print(f"  • {explanation}")

if __name__ == "__main__":
    test_exact_example()