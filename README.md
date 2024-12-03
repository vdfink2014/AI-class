# AI-class
This class for python lets you do anything with AI. It uses Hugging Face to explore AI
# Documentation
To use this Class, you need to install huggingface_hub and deep_translator by typing "pip install huggingface_hub deep_translator" in the powershell.
After that, you will need to set AI.token, AI.model_C, AI.model_SD.

AI.token -  the token for hugging face

AI.model_C - the model for text generation

AI.model_SD - the model for image generation

Before you start, you need to start the AI's by typing AI.start_ai()

AI.chatgpt() - for text generation. We are sorry, but it knows only one message that you typed. To use it, you need to type the text in parentheses

AI.SD() - for image generation. To use it, again, type the text in parentheses and it saves into your system as the text without whitespaces.

Example:
''' python

from AI import AI

AI.token = "token"
AI.model_C = "HuggingFaceH4/starchat2-15b-v0.1"
AI.start_ai()

output = AI.chatgpt("What is the capital of France?")

print(output)
'''

That's all for this project!
