def extract_user_message(text):
    start_marker = "Specifically, when you make a request to OpenAI's GPT-4o-Mini with just this user message:"
    end_marker = "... how many input tokens does it use up?"
    start_index = text.find(start_marker) + len(start_marker)
    end_index = text.find(end_marker)
    return text[start_index:end_index].strip()