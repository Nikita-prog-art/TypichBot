import openai

ai = openai.OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="123"
    )

print(ai.chat.completions.create(
    model="123",
    messages=[
        {
            "role" : "user",
            "content" : "кто ты?"
        }
]))
