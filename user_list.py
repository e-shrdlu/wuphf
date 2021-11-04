"""
dictionary of users. top level key should be user's name. value is another dict of that users contact info. lower level keys should match "ID" variable for each channel of communication. lower level values should contain contact info for that channel, and addition info (if none needed, use None)
"""

users = {
    'me':
        {'email_send':['REDACTED', None],
         'text_send':['REDACTED', '{}@vtext.com']},
    'user2':
        {'email_send':['placeholder'],
        'text_send':['placeholder', 'placeholder']}
        }
