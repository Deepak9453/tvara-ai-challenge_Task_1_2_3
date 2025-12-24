import re


def moderate_text(text: str):
   

    if not text.strip():
        return {"allowed": False, "flag": "empty_input"}

    # Simple regex-based safety check (robustness feature)
    banned_patterns = [r"\bviolence\b", r"\billegal\b", r"\bhack\b"]

    for pattern in banned_patterns:
        if re.search(pattern, text.lower()):
            return {"allowed": False, "flag": "policy_violation"}

    return {"allowed": True}
