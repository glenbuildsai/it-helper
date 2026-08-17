from anthropic import Anthropic
from config import IT_SYSTEM_PROMPT

class ITConversation:
    """Manages a multi-turn conversation with the IT assistant."""
    
    def __init__(self):
        self.client = Anthropic()
        # This list grows with each exchange.
        # It's the entire conversation Claude "remembers".
        self.history: list[dict] = []
    
    def ask(self, user_message: str) -> str:
        # Add the user's new message to history
        self.history.append({
            "role": "user",
            "content": user_message
        })
        
        # Send the FULL history every time — this is what
        # gives Claude "memory" of previous turns
        response = self.client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system=IT_SYSTEM_PROMPT,
            messages=self.history   # <-- the full history
        )
        
        assistant_reply = response.content[0].text
        
        # Add Claude's reply to history too, so it's included
        # in the next request
        self.history.append({
            "role": "assistant",
            "content": assistant_reply
        })
        
        return assistant_reply
    
    def reset(self):
        """Start a fresh conversation."""
        self.history = []
        print("Conversation reset. Starting fresh.")
    
    def show_history(self):
        """Debug tool: print the raw history."""
        for i, msg in enumerate(self.history):
            print(f"[{i}] {msg['role'].upper()}: {msg['content'][:80]}...")