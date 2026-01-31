from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    response = generate_ai_response(req.message)
    return {"response": response}

def generate_ai_response(prompt: str) -> str:
    prompt = prompt.lower()

    # Greetings
    if prompt in ["hi", "hello", "hey", "hii", "hlo"]:
        return (
            "👋 Hi! I'm **LearnMate AI**.\n\n"
            "How are you today? 😊\n\n"
            "I can help you understand concepts of **Artificial Intelligence** and "
            "**Machine Learning**, explain topics, or motivate you in your studies."
        )

    # How are you
    if "how are you" in prompt or "how's you" in prompt:
        return (
            "😊 I'm doing great, thank you for asking!\n\n"
            "How can I help you today?\n"
            "You can ask me about **AI concepts, Machine Learning, or Python**."
        )

    # Help / What can you do
    if "help" in prompt or "what can you do" in prompt:
        return (
            "📘 I’m here to help you learn!\n\n"
            "✨ I can:\n"
            "- Explain **Artificial Intelligence** concepts\n"
            "- Teach **Machine Learning** basics\n"
            "- Help with **Python programming**\n"
            "- Motivate you when studies feel overwhelming\n\n"
            "Just ask me a question!"
        )
    if "python list" in prompt:
        return (
            "A Python list is a built-in data structure used to store multiple values in a single variable. "
            "Lists are ordered, mutable, and allow duplicate elements. "
            "Example: my_list = [1, 2, 3, 4]"
        )
 
    if "python" in prompt:
        return (
            "Python is a high-level, interpreted programming language known for its simplicity and readability. "
            "It is widely used in web development, data science, artificial intelligence, and automation."
        )


    # Artificial Intelligence
    if "artificial intelligence" in prompt or "ai" in prompt:
        return (
            "🧠 **Artificial Intelligence (AI)** enables machines to mimic human intelligence.\n\n"
            "🔹 AI includes learning, reasoning, and problem-solving.\n"
            "🔹 Used in chatbots, self-driving cars, recommendation systems, and more."
        )

    # Machine Learning
    if "machine learning" in prompt or "ml" in prompt:
        return (
            "🤖 **Machine Learning (ML)** is a subset of AI where systems learn from data.\n\n"
            "🔹 Types of ML:\n"
            "- Supervised Learning\n"
            "- Unsupervised Learning\n"
            "- Reinforcement Learning\n\n"
            "📌 Example: Email spam detection"
        )

    # Motivation
    if "stress" in prompt or "tired" in prompt or "motivate" in prompt:
        return (
            "💙 It’s okay to feel stressed sometimes.\n\n"
            "Take a deep breath 🌱\n"
            "You’re learning something valuable, and every step counts!"
        )
    if "thankyou" in prompt or "thnx" in prompt or "thanku" in prompt :
        return(
            "That's my pleasure that i helped you in learning things. What can i do more for you."
        )

    # Default response
    return (
        "📚 That’s a great question!\n\n"
        "I’m still learning, but I can definitely help you with:\n"
        "👉 Artificial Intelligence\n"
        "👉 Machine Learning\n"
        "👉 Python basics\n\n"
        "Please ask your question clearly 😊"
    )


import os

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port=8000)
