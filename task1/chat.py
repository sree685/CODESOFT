from datetime import date time
print("ChatBot: hello! I'm your simple chatbot.")
print("ChatBot: Type 'Bye' to end the chat.")
while True:
      User = input ("you:").lower()
      if user == "Bye":
      print("ChatBot:GoodBye! Have a nice day.")
      break
  elif "Hello" in user or "Hi" in user:
    print(ChatBot:Hithere! How can i help you ?")
  elif "How are you" in user:
    print ("ChatBot:I'm just a bot ,but I'm doing well!")
  elif "your name" in user:
    print("ChatBot:I'm chatsimple,your friendly chatbot")
  elif "Time" in user:
    current_time = datetime.now().strftime("%H:%M:%S")
      print("ChatBot: Current time is",current_time)
elif "date" in user or "day" in user:
  current_date = datetime.now().strftime("%Y-%M-%D")
  print ("ChatBot:Today's date is",current_date)
else:
  print("ChatBot:I'm not sure that how to respond.")
