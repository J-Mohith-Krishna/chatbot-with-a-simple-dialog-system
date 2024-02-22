# Chatbot-with-a-simple-dialog-system
## Description-
This code defines a simple chatbot that responds to greetings, goodbyes, and specific user inputs with predefined responses. If the input does not match any predefined patterns, the chatbot provides a default response.
## Explanation-
  -Importing Libraries: The code begins by importing the random library, which is not currently used in the code. It might be a remnant from earlier iterations or intended for future expansion.

  -Class Definition: The SimpleChatbot class is defined. This class encapsulates the behavior and attributes of a simple chatbot.

  -Constructor Method (__init__): The constructor method initializes the chatbot object. It defines three lists: greetings, goodbyes, and a dictionary responses containing various user inputs and their corresponding responses.

  -get_response Method: This method takes a user input and returns a response from the chatbot. It first converts the user input to lowercase for case-insensitive comparison. Then, it checks if the input contains any greetings from the greetings list or any goodbyes from the goodbyes list. If it matches, the chatbot responds accordingly.

  -Fallback Response: If the user input does not match any greetings or goodbyes, the method iterates over the keys in the responses dictionary. If the user input matches any key, the corresponding response is returned. If no match is found, the default response is returned.

  -Main Function (main): The main function creates an instance of the SimpleChatbot class. It then enters a loop where it continuously prompts the user for input until the user enters a goodbye command (bye, goodbye, or exit). After each user input, it calls the get_response method of the chatbot instance to generate a response and prints it.

  -Execution: Finally, the main function is executed if the script is run directly (i.e., not imported as a module). This starts the interaction with the chatbot.
