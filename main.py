try:
    from huggingface_hub import InferenceClient
    from deep_translator import GoogleTranslator
except:
    print("Error 1")
class AI():
        token = ""    
        model_C = ""    
        model_SD = ""    
        def start_ai(self):
            global client
            client = InferenceClient(api_key=self.token)
            global client2
            client2 = InferenceClient(self.model_SD, token=self.token)
        def chatgpt(self, promt):
            messages = [
                {
                   "role": "user",
                   "content": f"{promt}"}
            ]
            try:
                completion = client.chat.completions.create(model=self.model_C, messages=messages, max_tokens=5000)
            except:
                return "Error #01"     
            a = GoogleTranslator("auto", "ru").translate(text=completion.choices[0].message.content)
            return a

        def SD(self, promt):
            try:
                image = client2.text_to_image(promt)
            except:
                print("Error #02")
            image.save("promt.replace(" ", "") + ".png")
