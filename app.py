#!/usr/bin/env python3
"""
Flask Web Application for Ranchi Local Guide Translator
"""

from flask import Flask, render_template, request, jsonify
import json
import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ranchi_translator import RanchiTranslator

app = Flask(__name__)

# Initialize the translator
try:
    translator = RanchiTranslator()
    print(f"✅ Translator initialized with {len(translator.terms_dict)} terms")
except Exception as e:
    print(f"❌ Error initializing translator: {e}")
    translator = None

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    """API endpoint for translation"""
    try:
        if not translator:
            return jsonify({
                'success': False,
                'error': 'Translator not initialized'
            })
            
        data = request.get_json()
        sentence = data.get('sentence', '').strip()
        
        if not sentence:
            return jsonify({
                'success': False,
                'error': 'Please enter a sentence to translate'
            })
        
        # Translate the sentence
        result = translator.translate_sentence(sentence)
        
        return jsonify({
            'success': True,
            'original': result['original'],
            'translated': result['translated'],
            'has_translations': result['has_translations'],
            'explanations': result['explanations'],
            'terms_found': result['terms_found']
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Translation error: {str(e)}'
        })

@app.route('/terms')
def get_terms():
    """API endpoint to get all available terms"""
    try:
        if not translator:
            return jsonify({
                'success': False,
                'error': 'Translator not initialized'
            })
            
        # Organize terms by category
        categories = {
            "Food & Drinks": [],
            "Greetings & Slang": [],
            "Places & Locations": [],
            "Common Phrases": []
        }
        
        for term, translation in translator.terms_dict.items():
            term_info = {
                'term': term.title(),
                'translation': translation
            }
            
            if any(word in translation.lower() for word in ['dish', 'food', 'drink', 'rice', 'beer', 'snack', 'curry']):
                categories["Food & Drinks"].append(term_info)
            elif any(word in translation.lower() for word in ['greeting', 'friend', 'brother', 'sister', 'how are']):
                categories["Greetings & Slang"].append(term_info)
            elif any(word in translation.lower() for word in ['road', 'area', 'lake', 'ground', 'chowk']):
                categories["Places & Locations"].append(term_info)
            else:
                categories["Common Phrases"].append(term_info)
        
        return jsonify({
            'success': True,
            'categories': categories,
            'total_terms': len(translator.terms_dict)
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error fetching terms: {str(e)}'
        })

if __name__ == '__main__':
    print("🚀 Starting Ranchi Local Guide Translator Web Server...")
    print("🌐 Visit: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)