from typing import List


def post_process(text: str, n_stanzas=2):
    # First split by mask tokens to get lines
    lines = text.split('<mask>')
    
    # Process each line
    processed_lines = []
    for line in lines:
        # Clean up special tokens
        line = line.replace('<s>', '')
        line = line.replace('</s>', '')
        line = line.replace('_', ' ')
        line = line.replace('@@', '')
        
        # Clean up whitespace and split into words
        words = line.strip().split()
        # Remove any remaining special tokens
        words = [w for w in words if not w.startswith('<') and not w.endswith('>')]
        
        if words:  # Only add non-empty lines
            processed_lines.append(' '.join(words))
    
    # Capitalize each line and join with newlines
    formatted_lines = [line.capitalize() for line in processed_lines]
    poem = '\n'.join(formatted_lines)
    
    return poem