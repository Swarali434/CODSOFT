def chatbot(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I assist you?"
    elif "how are you" in user_input.lower():
        return "I'm just a bot, but thanks for asking!"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    elif "hi" in user_input.lower():
        return "hi !! how can i help you ?"
    elif "what is your name?" in user_input.lower():
        return " My name is chatbot."
    elif "how old are you?" in user_input.lower():
        return "i am just 1 month old."
    else:
        return "I'm sorry, I didn't understand that."


while True:
    user_query = input("You: ")
    response = chatbot(user_query)
    print("Chatbot:", response)
    if "bye" in user_query.lower():
        break
