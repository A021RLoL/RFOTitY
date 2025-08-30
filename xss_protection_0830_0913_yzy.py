# 代码生成时间: 2025-08-30 09:13:39
import numpy as np
import re

"""
XSS Protection Module
This module provides XSS (Cross Site Scripting) protection by sanitizing
input strings to prevent malicious scripts from being executed."""


# Define a list of allowed HTML tags for safe output
ALLOWED_TAGS = [
    "a", "b", "br", "i", "em", "strong", "p", "ul", "ol", "li", "h1", "h2", "h3", "h4", "h5", "h6",
    "img", "span", "div"
]

# Define a list of allowed attributes for each tag
ALLOWED_ATTRIBUTES = {
    "a": ["href", "title", "alt"],
    "img": ["src", "alt", "title"],
    "div": ["id", "class"],
    "span": ["id", "class"]
}


def sanitize_input(input_string):
    """
    Sanitize input string to prevent XSS attacks.

    Parameters:
    input_string (str): The input string to be sanitized.

    Returns:
    str: The sanitized input string.
    """
    try:
        # Use regular expressions to find and remove script tags
        input_string = re.sub(r'<script\b[^<]*(?:(?!</script>)<[^<]*)*</script>', '', input_string)

        # Split string into tags and text nodes
        tokens = re.split(r'(<[^>]+>)', input_string)
        sanitized_string = ''

        for token in tokens:
            if not token.startswith('<'):
                sanitized_string += token
                continue

            # Check if the tag is allowed
            tag = token[1:].split('>')[0]
            if tag.strip() in ALLOWED_TAGS:
                # Check if the tag has any attributes
                attributes = re.findall(r'(\w+)=[\'"].*?[\'"]\s*', token)
                if not attributes:
                    sanitized_string += token
                else:
                    # Check if each attribute is allowed
                    sanitized_attributes = ''
                    for attribute in attributes:
                        attr_name, _ = attribute.split('=')
                        if attr_name.strip() in ALLOWED_ATTRIBUTES.get(tag, []):
                            sanitized_attributes += f' {attribute}'

                    sanitized_string += f'<{tag}{sanitized_attributes}></{tag}>'
            else:
                # Replace disallowed tags with their text content
                text_content = re.sub(r'<.*?>', '', token)
                sanitized_string += text_content

        return sanitized_string
    except Exception as e:
        # Handle any exceptions that occur during sanitization
        print(f"Error sanitizing input: {str(e)}")
        return None

# Example usage
if __name__ == '__main__':
    example_input = "<script>alert('XSS')</script>"
    sanitized_output = sanitize_input(example_input)
    print("Sanitized Output:", sanitized_output)
