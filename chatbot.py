import re
import datetime

def chatbot_response(user_input):
    text = user_input.lower().strip()

    if re.search(r'\b(hi|hello|hey|greetings)\b', text):
        return "Hello! Welcome to CodSoft AI Internship. How can I help you today?"
    elif re.search(r'\b(how are you|how do you do)\b', text):
        return "I'm just a Python program, but I'm doing great! Ready to help you with your tasks."
    elif re.search(r'\b(time|date|today)\b', text):
        now = datetime.datetime.now()
        return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"
    elif re.search(r'\b(task|internship|codsoft)\b', text):
        return "CodSoft offers great internships! For this AI internship, you need to complete at least 3 tasks."
    elif re.search(r'\b(bye|exit|quit)\b', text):
        return "Goodbye! Have a great day and good luck with your internship submission!"
    else:
        return "I'm sorry, I didn't quite understand that. Can you please rephrase?"

def main():
    print("🤖 Welcome to the Rule-Based Chatbot (CodSoft Task 1)")
    print("Type 'bye', 'exit', or 'quit' to end the chat.")
    print("--------------------------------------------------")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower().strip() in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        print(f"Chatbot: {chatbot_response(user_input)}")

if __name__ == "__main__":
    main()