def check_email(string: str):
    if '@' in string and ' ' not in string and '@.' not in string:
        index_at = string.index('@')
        index_dot = string.rfind('.')
        if index_at < index_dot and index_dot - index_at > 1 and string[index_at + 1] != '.':
            return True
    return False


