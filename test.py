# import os
# import openai

# openai.api_key = "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"

# while True:
#     a = input('Human..')
#     response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt=a,
#     temperature=0,
#     max_tokens=100,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0,
#     )


#     print(f"\n\n{response['choices'][0]['text']}")

import pyautogui

# Ask user for the message they want to send
message = input("What message would you like to send? ")

# Ask user for the number of times they want to send the message
num_times = int(input("How many times would you like to send the message? "))

# Loop through the number of times the user wants to send the message
for i in range(num_times):
    pyautogui.typewrite(message)
    pyautogui.press('enter')qwert
    qwert
    qwert
    qwert
    qwert
    qwert
    qwert
    qwert
    qwert
    