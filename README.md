# ai-class-python
This class for python lets you do anything with AI. It uses Hugging Face to explore AI
# Documentation
To use this Class, you need to install huggingface_hub and deep_translator by typing "pip install huggingface_hub deep_translator" in the powershell.
Insert the class by typing "from main import AI". If you want, you can change the file's name. But not, you need to type "from {your_file_name} import AI"
After that, you will need to set AI.token, AI.model_C, AI.model_SD.

AI.token -  the token for hugging face. You need to register an account in hugging face and create a token.

AI.model_C - the model for text generation. You can use only models from this page: https://huggingface.co/models?inference=warm&pipeline_tag=text-generation&sort=trending. First, choose the model and click on it. In the right of the page you have "Inference API". After that, find the "View Code" button. If up is "huggingface_hub" then everything is correct. in the "client = InferenceClient("black-forest-labs/FLUX.1-dev", token="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")" or something like this the "black-forest-labs/FLUX.1-dev" is your model.

AI.model_SD - the model for image generation. You can use only models from this page: https://huggingface.co/models?inference=warm&pipeline_tag=text-to-image&sort=trending. First, choose the model and click on it. In the right of the page you have "Inference API". After that, find the "View Code" button. If up is "huggingface_hub" and "requests" then everything is correct. In the "client = InferenceClient("black-forest-labs/FLUX.1-dev", token="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")" or something like this the "black-forest-labs/FLUX.1-dev" is your model.

Before you start, you need to start the AI's by typing AI.start_ai(). Every time you want another model instead of what you typed, you can change the model and type the same command. It works like restart ai.

AI.chatgpt() - for text generation. We are sorry, but it knows only one message that you typed. To use it, you need to type the text in parentheses

AI.SD() - for image generation. To use it, again, type the text in parentheses and it saves into your system ("C:\yourimage.png") as the text without whitespaces.

Example:
''' 
python

from main.py import AI

AI.token = "token"
AI.model_C = "HuggingFaceH4/starchat2-15b-v0.1"
AI.start_ai()

output = AI.chatgpt("What is the capital of France?")

print(output)
'''
Huge thanks to hugging face in this project. Please, visit their sites: https://huggingface.co
That's all for this project!
