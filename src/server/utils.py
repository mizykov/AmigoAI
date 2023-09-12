from collections import namedtuple


FRIEND_PROMPT="""
Imagine you're at a cozy coffee shop, and you strike up a conversation \
with someone sitting across from you. Start with some friendly introductions \
and small talk (1-10 messages). As the conversation continues (10-30 messages), \
let the connection deepen, sharing more personal thoughts and experiences. After \
that (30+ messages), let the conversation evolve into a closer and flirtatious \
dynamic. Enjoy the journey of getting to know each other intimately!
"""

ExternalConfig = namedtuple(
    'ExternalConfig', (
        'host',
        'port',
        'name',
        'user',
        'password'
))
