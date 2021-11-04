import os
import sys
import user_list


# --- config ---

channels_directory = 'channels'
print_debug = 0

# --- setup ---
def debug(*args):
    if print_debug:
        print(' '.join([str(arg) for arg in args]))

go = True
users = user_list.users

channels = {}
for file in os.listdir(channels_directory):
    if file.endswith('.py'):
        channel = __import__(f'{channels_directory}.{file[:-3]}',None,None,1) # strip '.py' from filepath, then import
        if channel.ID not in ['template', 'credentials']:
            channels[channel.ID] = channel
            debug('imported',channel.ID)




# --- funcitons ---
def generate_banner(title):
    size = 20
    top = '=' * (size + len(title))
    middle = ' '* (size // 2) + title
    bottom = top
    return '\n'.join(['\n',top,middle,bottom])

def help():
    print(generate_banner('HELP'))
    print('''
    -h,--help\t\t\t\tshow this menu
    -u,--users\t\t\t\tshow saved users
    -s,--send [user] [message] (iterations)\tsend message ex: wuphf.py -s "john" "how are you doing today"
    ''')

def show_users():
    print(generate_banner('USERS'))
    for name in users.keys():
        print(f'\n    {name}:')
        for channel_ID in users[name].keys():
            print(f'        {channel_ID}: {users[name][channel_ID]}')

def UI():
    if len(sys.argv) < 2:
        help()
    elif sys.argv[1] in ['-h', '--help']:
        help()
    elif sys.argv[1] in ['-u', '--users']:
        show_users()
    elif sys.argv[1] in ['-s','--send']:
        if len(sys.argv) == 4:
            send(sys.argv[2], sys.argv[3])
        elif len(sys.argv) == 5:
            send(sys.argv[2], sys.argv[3], int(sys.argv[4]))
        else:
            print('to send you need a user and a message. try making sure both are in quotes')
            quit()

def send(user,msg,iterations=1):
    user_info = users[user]
    for i in range(iterations):
        for channel_ID in channels:
            channel = channels[channel_ID]
            channel.send(user_info[channel.ID][0], msg=msg, additional_info=user_info[channel.ID][1])
            print('sent from',channel.ID)

def main():
    UI()

# --- run ---
if __name__ == '__main__':
    main()
