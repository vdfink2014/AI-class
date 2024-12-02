from main import AI as ai

ai.token = "token"
ai.model_C = "model"
ai.start_ai()

input = input()

output = ai.chatgpt(input)

print(output)
