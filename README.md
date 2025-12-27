# Ranchi Local Guide Translator

A Python program that translates local Ranchi slang, food terms, and cultural phrases to help visitors understand the local language of Ranchi, Jharkhand.

## Features

- 🗣️ **Local Slang Translation**: Understands Nagpuri/Khortha terms like "Arre baba", "Kaise ho re"
- 🍽️ **Food Terms**: Translates local dishes like Litti Chokha, Dhuska, Rugra
- 🏛️ **Cultural Context**: Explains local places and cultural references
- 💬 **Interactive Mode**: User-friendly chat interface
- ⚠️ **Error Handling**: Gracefully handles unknown terms
- 🔍 **Smart Detection**: Finds multiple terms in a single sentence

## Files

- `ranchi_translator.py` - Main interactive translator program
- `demo.py` - Demo script showing example translations
- `test_example.py` - Tests the exact example from requirements
- `product.md/namaste world htlm.txt` - Source file with Ranchi terms
- `README.md` - This documentation

## Quick Start

### Interactive Mode
```bash
python ranchi_translator.py
```

### See Examples
```bash
python demo.py
```

### Test Specific Example
```bash
python test_example.py
```

## Example Usage

**Input:** "Arre baba, Litti Chokha khao, bahut acha hai"

**Output:** "Hey friend, Litti Chokha (traditional Ranchi dish) try, it's very good"

**Explanations:**
- 'Arre baba' → Hey friend (casual greeting)
- 'Litti Chokha' → Traditional dish with roasted wheat balls and mashed vegetables
- 'acha hai' → It's good/Nice

## Available Terms

The translator includes 27+ terms covering:

### 🍽️ Food & Drinks
- Litti Chokha, Dhuska, Rugra, Pittha, Handia, Thekua, Chilka Roti

### 👋 Greetings & Slang  
- Arre baba, Kaise ho re, Theek ba, Dada/Didi, Aaja bhai

### 🏛️ Places & Locations
- Main Road, Tharpakhna, Firayalal, Dhurwa, Morhabadi

### 💬 Common Phrases
- Khana khaao, Paani piyoo, Ghar aa jao, Kahaan jaat ho

## Interactive Commands

- Type any sentence with Ranchi terms to get translation
- Type `help` to see all available terms
- Type `quit`, `exit`, or `q` to stop

## Error Handling

- ✅ Handles missing source files gracefully
- ✅ Ignores unknown terms without errors
- ✅ Prevents overlapping term matches
- ✅ Provides helpful feedback for empty inputs

## Requirements

- Python 3.6 or higher
- No external dependencies required

Perfect for tourists, students, or anyone wanting to understand Ranchi's rich local culture and language!