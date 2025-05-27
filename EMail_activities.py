import email
from email import policy
from email.parser import BytesParser

# Load the .eml file
with open('your_email_file.eml', 'rb') as file:
    msg = BytesParser(policy=policy.default).parse(file)

# Extract content using walk
for part in msg.walk():
    content_type = part.get_content_type()
    content_disposition = str(part.get("Content-Disposition"))

    if content_type == "text/plain" and "attachment" not in content_disposition:
        # Extract plain text
        text_content = part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8')
        print("Plain Text Content:\n", text_content)

    elif content_type == "text/html" and "attachment" not in content_disposition:
        # Extract HTML content
        html_content = part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8')
        print("HTML Content:\n", html_content)
