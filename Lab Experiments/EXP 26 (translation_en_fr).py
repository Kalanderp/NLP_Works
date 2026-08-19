"""English-to-French translation with Hugging Face Transformers."""
text='The cat is sitting on the mat.'
try:
 from transformers import pipeline
 translator=pipeline('translation_en_to_fr', model='Helsinki-NLP/opus-mt-en-fr')
 print(translator(text)[0]['translation_text'])
except ImportError: print('Install Transformers and PyTorch: pip install transformers torch sentencepiece')
except Exception as e: print('Model download/inference unavailable:', e)
