#!/usr/bin/env python3
"""
Ranchi Local Guide Translator
Translates local Ranchi slang, food terms, and phrases to standard English/Hindi
"""

import re
import os
from typing import Dict, List, Tuple, Optional

class RanchiTranslator:
    def __init__(self, terms_file: str = "product.md/namaste world htlm.txt"):
        """Initialize the translator with terms from the file"""
        self.terms_dict = {}
        self.load_terms(terms_file)
    
    def load_terms(self, filename: str) -> None:
        """Load terms and their translations from the file"""
        try:
            if not os.path.exists(filename):
                print(f"Warning: {filename} not found. Using default terms.")
                self._load_default_terms()
                return
            
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                self._parse_content(content)
            
            print(f"✅ Loaded {len(self.terms_dict)} terms from Ranchi guide")
        
        except Exception as e:
            print(f"❌ Error loading terms file: {e}")
            print("Using default terms instead.")
            self._load_default_terms()
    
    def _parse_content(self, content: str) -> None:
        """Parse content and extract term definitions"""
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            # Look for lines with format "- **term** = definition"
            if '**' in line and '=' in line:
                # Extract term between ** markers
                term_match = re.search(r'\*\*(.*?)\*\*', line)
                if term_match:
                    term = term_match.group(1).strip()
                    # Get definition after =
                    if '=' in line:
                        definition = line.split('=', 1)[1].strip()
                        # Clean up quotes if present
                        term_clean = term.replace('"', '').strip()
                        self.terms_dict[term_clean.lower()] = definition
                        
                        # Also store quoted versions
                        if '"' in term:
                            quoted_term = term.replace('"', '').strip()
                            self.terms_dict[quoted_term.lower()] = definition
    
    def _load_default_terms(self) -> None:
        """Load default terms if file is not available"""
        default_terms = {
            "arre baba": "Hey friend (casual greeting)",
            "litti chokha": "Traditional dish with roasted wheat balls and mashed vegetables",
            "dhuska": "Fried rice pancakes, local breakfast item",
            "bahut acha": "Very good/excellent",
            "kaise ho re": "How are you? (local informal)",
            "theek ba": "All good/I'm fine"
        }
        self.terms_dict = default_terms
    
    def find_terms_in_sentence(self, sentence: str) -> List[Tuple[str, str, str]]:
        """
        Find local terms in the sentence and return matches with their translations
        Returns: List of (original_term, matched_term, translation) tuples
        """
        sentence_lower = sentence.lower()
        found_terms = []
        
        # Sort terms by length (longest first) to match longer phrases first
        sorted_terms = sorted(self.terms_dict.keys(), key=len, reverse=True)
        
        for term in sorted_terms:
            # Use word boundaries for better matching
            pattern = r'\b' + re.escape(term) + r'\b'
            matches = re.finditer(pattern, sentence_lower)
            
            for match in matches:
                original_term = sentence[match.start():match.end()]
                found_terms.append((original_term, term, self.terms_dict[term]))
        
        return found_terms
    
    def translate_sentence(self, sentence: str) -> Dict:
        """
        Translate a sentence containing local Ranchi terms
        Returns a dictionary with translation details
        """
        found_terms = self.find_terms_in_sentence(sentence)
        
        if not found_terms:
            return {
                "original": sentence,
                "translated": sentence,
                "terms_found": [],
                "explanations": [],
                "has_translations": False
            }
        
        translated_sentence = sentence
        explanations = []
        terms_info = []
        
        # Process terms and create translated sentence
        processed_positions = set()
        
        for original_term, matched_term, translation in found_terms:
            # Find the position of this term in the original sentence
            term_pos = sentence.lower().find(matched_term)
            
            # Check if this position overlaps with already processed terms
            term_range = set(range(term_pos, term_pos + len(matched_term)))
            if not term_range.intersection(processed_positions):
                # Mark this range as processed
                processed_positions.update(term_range)
                
                # Create explanation
                explanations.append(f"'{original_term}' → {translation}")
                terms_info.append({
                    "original": original_term,
                    "translation": translation
                })
        
        # Create a more natural translated sentence
        translated_sentence = self._create_natural_translation(sentence, terms_info)
        
        return {
            "original": sentence,
            "translated": translated_sentence,
            "terms_found": [term["original"] for term in terms_info],
            "explanations": explanations,
            "has_translations": len(explanations) > 0
        }
    
    def _create_natural_translation(self, sentence: str, terms_info: List[Dict]) -> str:
        """Create a more natural English translation"""
        translated = sentence
        
        # Simple replacements for common terms
        replacements = {
            "arre baba": "Hey friend",
            "kaise ho re": "How are you",
            "theek ba": "I'm fine",
            "bahut acha": "very good",
            "khana khaao": "have some food",
            "paani piyoo": "drink water",
            "aaja bhai": "come here brother",
            "kahaan jaat ho": "where are you going",
            "ghar aa jao": "come to my home"
        }
        
        for term_info in terms_info:
            original = term_info["original"]
            original_lower = original.lower()
            
            if original_lower in replacements:
                # Replace with natural English
                translated = re.sub(re.escape(original), replacements[original_lower], translated, flags=re.IGNORECASE)
            elif "litti chokha" in original_lower:
                translated = re.sub(re.escape(original), "Litti Chokha (traditional Ranchi dish)", translated, flags=re.IGNORECASE)
            elif "dhuska" in original_lower:
                translated = re.sub(re.escape(original), "Dhuska (local rice pancakes)", translated, flags=re.IGNORECASE)
        
        return translated
    
    def interactive_mode(self):
        """Run the translator in interactive mode"""
        print("=" * 70)
        print("🏛️  RANCHI LOCAL GUIDE TRANSLATOR")
        print("   Translate local Ranchi slang to English/Hindi")
        print("=" * 70)
        print("💡 Enter sentences with Ranchi local terms and get translations!")
        print("📝 Type 'help' to see available terms")
        print("🚪 Type 'quit', 'exit', or 'q' to stop")
        print("-" * 70)
        
        while True:
            try:
                user_input = input("\n🗣️  Enter sentence: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("\n👋 Dhanyawad! Thanks for using Ranchi Local Guide Translator!")
                    break
                
                if user_input.lower() == 'help':
                    self.show_available_terms()
                    continue
                
                if not user_input:
                    print("⚠️  Please enter a sentence to translate.")
                    continue
                
                # Translate the sentence
                result = self.translate_sentence(user_input)
                
                # Display results
                print(f"\n📥 Original:    {result['original']}")
                
                if result['has_translations']:
                    print(f"📤 Translated:  {result['translated']}")
                    print("\n🔍 Term explanations:")
                    for explanation in result['explanations']:
                        print(f"   • {explanation}")
                else:
                    print("ℹ️  No Ranchi local terms found in this sentence.")
                    print("💡 Try using terms like 'Arre baba', 'Litti Chokha', 'Kaise ho re', etc.")
            
            except KeyboardInterrupt:
                print("\n\n👋 Dhanyawad! Thanks for using Ranchi Local Guide Translator!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                print("Please try again with a different sentence.")
    
    def show_available_terms(self):
        """Display all available terms organized by category"""
        print("\n📚 Available Ranchi Local Terms:")
        print("=" * 50)
        
        # Categorize terms
        categories = {
            "🍽️ Food & Drinks": [],
            "👋 Greetings & Slang": [],
            "🏛️ Places & Locations": [],
            "💬 Common Phrases": []
        }
        
        for term, translation in self.terms_dict.items():
            term_title = term.title()
            short_translation = translation[:60] + "..." if len(translation) > 60 else translation
            
            if any(word in translation.lower() for word in ['dish', 'food', 'drink', 'rice', 'beer', 'snack']):
                categories["🍽️ Food & Drinks"].append(f"   • {term_title}: {short_translation}")
            elif any(word in translation.lower() for word in ['greeting', 'friend', 'brother', 'sister', 'how are']):
                categories["👋 Greetings & Slang"].append(f"   • {term_title}: {short_translation}")
            elif any(word in translation.lower() for word in ['road', 'area', 'lake', 'ground', 'chowk']):
                categories["🏛️ Places & Locations"].append(f"   • {term_title}: {short_translation}")
            else:
                categories["💬 Common Phrases"].append(f"   • {term_title}: {short_translation}")
        
        for category, terms in categories.items():
            if terms:
                print(f"\n{category}:")
                for term in sorted(terms)[:8]:  # Show max 8 per category
                    print(term)
                if len(terms) > 8:
                    print(f"   ... and {len(terms) - 8} more terms")

def main():
    """Main function to run the translator"""
    print("🚀 Starting Ranchi Local Guide Translator...")
    
    # Initialize translator
    translator = RanchiTranslator()
    
    # Show example
    print("\n🧪 Example Translation:")
    example = "Arre baba, Litti Chokha khao, bahut acha hai"
    result = translator.translate_sentence(example)
    
    print(f"Input:  {example}")
    print(f"Output: {result['translated']}")
    if result['explanations']:
        print("Terms:")
        for explanation in result['explanations']:
            print(f"  → {explanation}")
    
    print("\n" + "="*70)
    
    # Start interactive mode
    translator.interactive_mode()

if __name__ == "__main__":
    main()