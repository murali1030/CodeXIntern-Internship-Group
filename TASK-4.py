#!/usr/bin/env python
# coding: utf-8

# 6. Command-Line Chat bot:
# Compose a Python program that interacts with users via text input in the
# terminal. It can handle simple conversations, answer predefined
# questions, or perform specific tasks like setting reminders or providing
# information. The chatbot can be implemented using basic conditional
# statements for rule-based responses or enhanced with natural language
# processing (NLP) techniques for more sophisticated interactions. This
# project is ideal for practicing text processing, user input handling, and
# building basic conversational AI in a lightweight environment.

# In[5]:


import time


# In[6]:


def welcome():
    print("Hello! I'm your friendly chatbot.")
    print("You can ask me about the weather, tell me a joke,set a reminder,football,or puppy")
    print("Type 'exit' to end the chat.\n")


# In[7]:


def respond_to_input(user_input):
    user_input = user_input.lower() 
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    
    elif "weather" in user_input:
        return "I can't predict the weather yet, but it seems sunny in here!"
    
    elif "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    
    elif "footbal" in user_input:
        return "football is very famous game aof all time!"
    elif "puppy" in user_input:
        return "My pet name is  puppy and i love him!"
    
    elif "reminder" in user_input:
        set_reminder()
        return "Reminder is set!"
    
    elif "time" in user_input:
        current_time = time.strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    
    elif "exit" in user_input:
        return "Goodbye! Have a great day!"
    
    else:
        return "Sorry, I didn't understand that. Can you ask something else?"


# In[8]:


def set_reminder():
    reminder = input("What would you like to be reminded about? ")
    time_delay = input("In how many seconds should I remind you? ")
    print(f"Okay, I will remind you to '{reminder}' in {time_delay} seconds.")
    time.sleep(int(time_delay))
    print(f"Reminder: {reminder}")


# In[9]:


def chat():
    welcome()
    while True:
        user_input = input("You: ")  
        if "exit" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = respond_to_input(user_input)   
        print(f"Chatbot: {response}")   


# In[10]:


# Run the chatbot
if __name__ == "__main__":
    chat()


# In[ ]:




