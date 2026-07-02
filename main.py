from openai import OpenAI
from openai import RateLimitError
from rag.retriever import retrieve_documents

from config import OPENROUTER_API_KEY, MODEL
from prompt import SYSTEM_PROMPT

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)


from openai import OpenAI
from openai import RateLimitError

from config import OPENROUTER_API_KEY, MODEL
from prompt import SYSTEM_PROMPT
from rag.retriever import retrieve_documents

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)


def chat(user_message):
    try:
        docs = retrieve_documents(user_message)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are a Customer Support AI.

Answer ONLY using the knowledge base below.

If the answer is not present, reply:
"I couldn't find that information in our knowledge base."

Knowledge Base:
{context}

Customer Question:
{user_message}
"""

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except RateLimitError:
        return "The AI model is busy. Please try again."

    except Exception as e:
        return str(e)