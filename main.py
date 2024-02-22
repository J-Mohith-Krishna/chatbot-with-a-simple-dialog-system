import random

class SimpleChatbot:
    def __init__(self):
        self.greetings = ['hello', 'hi', 'hey', 'greetings', 'howdy']
        self.goodbyes = ['bye', 'goodbye', 'see you', 'farewell']
        self.responses = {
            'tell me a joke': 'Why did the chicken cross the road? To get to the other side!',
            'how are you': 'I am just a computer program, but thanks for asking!',
'default': 'I\'m sorry, I don\'t understand that. Can you ask me something else?'

        }

    def get_response(self, user_input):
        user_input = user_input.lower()

        if any(greeting in user_input for greeting in self.greetings):
            return 'Hello! How can I help you today?'

        elif any(goodbye in user_input for goodbye in self.goodbyes):
            return 'Goodbye! Have a great day.'

        else:
            for key in self.responses:
                if key in user_input:
                    return self.responses[key]

            return self.responses['default']

def main():
    chatbot = SimpleChatbot()

    print("Simple Chatbot: Hello! Ask me anything or say goodbye to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye', 'exit']:
            print("Simple Chatbot: Goodbye! Have a great day.")
            break

        response = chatbot.get_response(user_input)
        print("Simple Chatbot:", response)

if __name__ == "__main__":
    main()
