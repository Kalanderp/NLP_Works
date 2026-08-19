"""OpenAI-compatible text generation example. Requires OPENAI_API_KEY."""
import os
try:
 from openai import OpenAI
 prompt='Write one short sentence about natural language processing.'
 if not os.getenv('OPENAI_API_KEY'): print('Set OPENAI_API_KEY before running this experiment.'); raise SystemExit
 client=OpenAI(); response=client.completions.create(model='gpt-3.5-turbo-instruct', prompt=prompt, max_tokens=40, temperature=0.7)
 print(response.choices[0].text.strip())
except ImportError: print('Install the OpenAI library: pip install openai')
except Exception as e: print('API call not completed:', e)
