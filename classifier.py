import os
import json

CATEGORIES = ["order", "question", "complaint", "other"]

REPLIES = {
    "order": "Thank you for your order! We have received it and will "
             "confirm the details and delivery time shortly.",
    "question": "Thanks for reaching out! Here is the information you "
                "asked for. Let us know if you need anything else.",
    "complaint": "We are sorry about this experience. We take it "
                 "seriously and will fix the problem or arrange a "
                 "refund as soon as possible.",
    "other": "Thank you for your message. A team member will get "
             "back to you soon.",
}


def classify(message: str) -> dict:
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        return _fake_classify(message)

    import anthropic
    client = anthropic.Anthropic(api_key=key)
    resp = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=500,
        messages=[{
            "role": "user",
            "content": (
                "Classify this customer message into one of "
                f"{CATEGORIES}. Reply ONLY with JSON: "
                '{"category": "...", "draft_reply": "..."}\n\n'
                f"Message: {message}"
            ),
        }],
    )
    return json.loads(resp.content[0].text)


def _fake_classify(message: str) -> dict:
    text = message.lower()
    if any(w in text for w in ("refund", "bad", "broken", "late", "angry")):
        cat = "complaint"
    elif any(w in text for w in ("order", "buy", "purchase", "want",
                                 "need", "looking for", "available")):
        cat = "order"
    elif "?" in text or any(w in text for w in ("price", "how", "when")):
        cat = "question"
    else:
        cat = "other"
    return {"category": cat, "draft_reply": REPLIES[cat]}


if __name__ == "__main__":
    print(classify("Hi, I want to order 3 shirts. Is it available?"))