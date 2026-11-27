import os
import json

CATEGORIES = ["order", "question", "complaint", "other"]


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
    if "order" in text or "buy" in text:
        cat = "order"
    elif "?" in text:
        cat = "question"
    elif "bad" in text or "refund" in text:
        cat = "complaint"
    else:
        cat = "other"
    return {"category": cat, "draft_reply": f"[demo reply for {cat}]"}


if __name__ == "__main__":
    print(classify("Hi, I want to order 3 shirts. Is it available?"))
