from dotenv import load_dotenv
from conversation import ITConversation

load_dotenv()

def main():
    print("IT Support Assistant")
    print("=" * 40)
    print("Type your problem. Commands: 'quit', 'reset', 'history'")
    print()
    
    convo = ITConversation()
    
    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye.")
            break
        
        if not user_input:
            continue
        
        if user_input.lower() == "quit":
            print("Goodbye.")
            break
        elif user_input.lower() == "reset":
            convo.reset()
            continue
        elif user_input.lower() == "history":
            convo.show_history()
            continue
        
        print("\nAssistant: ", end="", flush=True)
        response = convo.ask(user_input)
        print(response)
        print()

if __name__ == "__main__":
    main()