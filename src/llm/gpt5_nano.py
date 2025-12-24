def mock_gpt5_nano(prompt: str):
    """
    Mock GPT-5-Nano call.
    Replace with OpenAI API once key is provided.
    """

    return {
        "response": f"[MOCK GPT-5-NANO OUTPUT]\nProcessed content:\n{prompt[:300]}..."
    }
