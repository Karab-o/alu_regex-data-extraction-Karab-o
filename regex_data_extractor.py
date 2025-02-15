import re

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

def extract_urls(text):
    url_pattern = r'https?://[^\s]+'
    return re.findall(url_pattern, text)

def extract_phone_numbers(text):
    phone_pattern = r'\(?\b\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'
    return re.findall(phone_pattern, text)

def extract_credit_card_numbers(text):
    cc_pattern = r'\b(?:\d[ -]*?){13,16}\b'
    return re.findall(cc_pattern, text)

def extract_time(text):
    time_pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d\b|\b(?:[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM)\b'
    return re.findall(time_pattern, text)

def extract_html_tags(text):
    html_tag_pattern = r'<[^>]+>'
    return re.findall(html_tag_pattern, text)

def extract_hashtags(text):
    hashtag_pattern = r'#\w+'
    return re.findall(hashtag_pattern, text)

def extract_currency_amounts(text):
    currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(currency_pattern, text)

if __name__ == "__main__":
    with open('sample_data.txt', 'r') as file:
        data = file.read()

    print("Extracted Emails:", extract_emails(data))
    print("Extracted URLs:", extract_urls(data))
    print("Extracted Phone Numbers:", extract_phone_numbers(data))
    print("Extracted Credit Card Numbers:", extract_credit_card_numbers(data))
    print("Extracted Time:", extract_time(data))
    print("Extracted HTML Tags:", extract_html_tags(data))
    print("Extracted Hashtags:", extract_hashtags(data))
    print("Extracted Currency Amounts:", extract_currency_amounts(data))