import random

messages = [
    'It is certain',
    'Yes, definently',
    'Reply hazy, try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

print(messages[random.randint(0, len(messages) - 1)])
