from chatbot_functions import generate_chatbot_response


def main():
   """
   Implements the main chatbot conversation loop.
   """
   while True:
       user_input = input("You: ")
       if user_input.lower() == "quit":
           break
       chatbot_response = generate_chatbot_response(user_input)
       print("Gemini:", chatbot_response)


if __name__ == "__main__":
   main()