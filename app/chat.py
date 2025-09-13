from openai import OpenAI
from app.config import OPEN_API_KEY
from app.memory import get_recent_messages, save_message


RECENT_MESSAGES_LIMIT = 5

client = OpenAI(api_key=OPEN_API_KEY)


def generate_response(user_id: str, message: str):
    print(f"new message: {message}")
    # Save user message to memory
    save_message(user_id, message, "user")

    # Get Last 5 messages (including the one we just saved)
    history = get_recent_messages(user_id, RECENT_MESSAGES_LIMIT)
    
    # Build messages array for OpenAI API
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    
    # Add conversation history
    for msg in history:
        messages.append({"role": msg["role"], "content": msg["content"]})
    
    print(f"Messages being sent to OpenAI: {messages}")
    
    # Generate response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7
    )
    answer = response.choices[0].message.content.strip()
    save_message(user_id, answer, role="assistant")
    return answer
