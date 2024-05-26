def what_to_do(instructions):
    length = len("Simon says")
    if instructions.startswith('Simon says'):
        return 'I ' + instructions[length + 1:]
    if instructions.endswith('Simon says'):
        return 'I ' + instructions[:length + 1]
    return "I won't do it!"
