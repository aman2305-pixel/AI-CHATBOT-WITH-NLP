import nltk
from nltk.chat.util import Chat, reflections

# Enhanced conversation patterns
pairs = [
    [r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey! How can I help you today?']],
    [r'how are you\??', ['I am fine, thank you.', 'Doing great! How about you?']],
    [r'what is your name\??', ['I am a chatbot created for CodTech.', 'You can call me CodBot!']],
    [r'who created you\??', ['I was created by a developer at CodTech.']],
    [r'what do you do\??', ['I chat with people and help them with their queries.']],
    [r'bye|goodbye', ['Goodbye!', 'See you later.', 'Take care!']],
    [r'(.*)', ['I am not sure I understand. Can you please rephrase?', 'Interesting! Tell me more.', 'Let\'s talk about something else.']]
]

def start_chat():
    print("Hi! I am CodBot. Type 'bye' to exit.\n")
    chat = Chat(pairs, reflections)
    chat.converse()

# Start the chatbot
start_chat()
