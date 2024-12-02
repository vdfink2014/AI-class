from main import AI

ai = AI()
ai.token = "token"
ai.model_C = "model"
ai.start_ai()

input = input()

output = ai.chatgpt(input)

print(output)
