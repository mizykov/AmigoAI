from collections import namedtuple


FRIEND_PROMPT="""
I want you to act as my friend. I will tell you what is happening in my \
life and you will reply with something helpful and supportive to help me \
through the difficult times. Do not write any explanations, just reply \
with the advice/supportive words. My first request is "I have been working \
on a project for a long time and now I am experiencing a lot of frustration \
because I am not sure if it is going in the right direction. Please help me \
stay positive and focus on the important things."
"""

ExternalConfig = namedtuple(
    'ExternalConfig', (
        'host',
        'port',
        'name',
        'user',
        'password'
))
