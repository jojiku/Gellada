from src.bot.telegram_bot import init_telegram_bot
from src.model.conversation_model import ConversationHandler as AIConversationHandler

ai_handler = AIConversationHandler()

 
def handle_ai_conversation(user_id: str, message: str) -> str:
    response = ai_handler.handle_conversation(user_id, message)
    return response

def main():
    print("Gellada has awoken...")
    init_telegram_bot(handle_ai_conversation, ai_handler.clear_user_history)
    print("Gellada went resting...")

if __name__ == "__main__":
    main()
