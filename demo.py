#!/usr/bin/env python3
"""
Demo script for Ranchi Local Guide Translator
Shows example translations
"""

from ranchi_translator import RanchiTranslator

def run_demo():
    """Run demonstration of the translator"""
    print("🏛️  RANCHI LOCAL GUIDE TRANSLATOR - DEMO")
    print("=" * 60)
    
    # Initialize translator
    translator = RanchiTranslator()
    
    # Test sentences with expected outputs
    test_cases = [
        {
            "input": "Arre baba, Litti Chokha khao, bahut acha hai",
            "expected": "Hey friend, try Litti Chokha (traditional Ranchi dish), it's very good"
        },
        {
            "input": "Kaise ho re? Dhuska try kiya hai?",
            "expected": "How are you? Have you tried Dhuska (local rice pancakes)?"
        },
        {
            "input": "Theek ba dada, ghar aa jao",
            "expected": "I'm fine brother, come to my home"
        },
        {
            "input": "Rugra curry bahut acha hai",
            "expected": "Mushroom curry is very good"
        },
        {
            "input": "This sentence has no local terms",
            "expected": "No translation needed"
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n📝 Example {i}:")
        print(f"Input:      {test['input']}")
        
        result = translator.translate_sentence(test['input'])
        
        if result['has_translations']:
            print(f"Translated: {result['translated']}")
            print("Explanations:")
            for explanation in result['explanations']:
                print(f"  • {explanation}")
        else:
            print("Result:     No local terms found")
        
        print("-" * 60)
    
    print("\n💡 To use interactively: python ranchi_translator.py")
    print("📚 To see all available terms, run the program and type 'help'")

if __name__ == "__main__":
    run_demo()