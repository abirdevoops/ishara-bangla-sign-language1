# ishara/translator.py

DEMO_TRANSLATIONS = {
    "পানি": {
        "text": "আমি পানি চাই।",
        "confidence": 94
    },
    "খাবার": {
        "text": "আমার খাবার দরকার।",
        "confidence": 92
    },
    "সাহায্য": {
        "text": "আমার সাহায্য দরকার।",
        "confidence": 96
    },
    "ধন্যবাদ": {
        "text": "ধন্যবাদ।",
        "confidence": 95
    },
    "হাসপাতাল": {
        "text": "আমাকে হাসপাতালে নিতে হবে।",
        "confidence": 90
    },
    "আবার বলুন": {
        "text": "দয়া করে আবার বলুন।",
        "confidence": 93
    }
}


def demo_translate(sign):
    """
    Demo translation function.
    Later this function can be connected
    with the real AI/ML model.
    """

    result = DEMO_TRANSLATIONS.get(
        sign,
        {
            "text": "এই sign এখনো শনাক্ত করা হয়নি।",
            "confidence": 50
        }
    )

    return result["text"], result["confidence"]


def confidence_message(confidence):
    """
    Returns a simple confidence message.
    """

    if confidence >= 90:
        return "High confidence — sign is recognized clearly."
    elif confidence >= 70:
        return "Medium confidence — please verify the result."
    else:
        return "Low confidence — please try again."
