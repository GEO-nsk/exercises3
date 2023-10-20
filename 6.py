message = str(input())

def max_message(message):
    if len(message) <= 160:
        return message
    else:
        return message[:160]

print(max_message(message))