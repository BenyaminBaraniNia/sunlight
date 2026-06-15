import json


def load_json_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_usernames_file(file_name, usernames):
    with open(file_name, 'w', encoding='utf-8') as file:
        for username in sorted(usernames, key=str.lower):
            file.write(username + '\n')


def write_instagram_links_file(file_name, usernames):
    with open(file_name, 'w', encoding='utf-8') as file:
        for username in sorted(usernames, key=str.lower):
            file.write(f'https://www.instagram.com/{username}\n\n')


def get_username_from_label_values(label_values):
    for item in label_values:
        if item.get('label') == 'Username':
            return item.get('value')

    return None


# =====================================================
# Followers
followers_data = load_json_file('followers_1.json')

followers_usernames = [
    item['string_list_data'][0]['value']
    for item in followers_data
    if item.get('string_list_data')
]

number_of_followers = len(followers_usernames)
# =====================================================


# =====================================================
# Following
following_data = load_json_file('following.json')

following_usernames = [
    item['title']
    for item in following_data['relationships_following']
    if item.get('title')
]

number_of_following = len(following_usernames)
# =====================================================


# =====================================================
# People you follow, but they do not follow you back
not_following_you_back = set(following_usernames).difference(set(followers_usernames))

# People who follow you, but you do not follow them back
you_do_not_follow_back = set(followers_usernames).difference(set(following_usernames))

number_of_not_following_you_back = len(not_following_you_back)
number_of_you_do_not_follow_back = len(you_do_not_follow_back)

write_usernames_file('02-Not_Following_You_Back.txt', not_following_you_back)
write_instagram_links_file('03-Not_Following_You_Back_Links.txt', not_following_you_back)

write_usernames_file('04-You_Do_Not_Follow_Back.txt', you_do_not_follow_back)
write_instagram_links_file('05-You_Do_Not_Follow_Back_Links.txt', you_do_not_follow_back)
# =====================================================


# =====================================================
# Recent follow requests
recent_follow_requests_data = load_json_file('recent_follow_requests.json')

# Instagram exports one request as a dictionary,
# but multiple requests as a list. This makes both cases work.
if isinstance(recent_follow_requests_data, dict):
    recent_follow_requests_data = [recent_follow_requests_data]

recent_follow_request_usernames = []

for request in recent_follow_requests_data:
    username = get_username_from_label_values(request.get('label_values', []))

    if username:
        recent_follow_request_usernames.append(username)

number_of_recent_follow_requests = len(recent_follow_request_usernames)

write_usernames_file('06-Recent_Follow_Requests.txt', recent_follow_request_usernames)
write_instagram_links_file('07-Recent_Follow_Requests_Links.txt', recent_follow_request_usernames)
# =====================================================


# =====================================================
# Statistics
with open('01-Page_Statistics.txt', 'w', encoding='utf-8') as file:
    file.write(f'Followers: {number_of_followers}\n')
    file.write(f'Following: {number_of_following}\n')
    file.write(f'Not following you back: {number_of_not_following_you_back}\n')
    file.write(f'You do not follow back: {number_of_you_do_not_follow_back}\n')
    file.write(f'Recent follow requests: {number_of_recent_follow_requests}\n')


print(f'Followers: {number_of_followers}')
print(f'Following: {number_of_following}')
print(f'Not following you back: {number_of_not_following_you_back}')
print(f'You do not follow back: {number_of_you_do_not_follow_back}')
print(f'Recent follow requests: {number_of_recent_follow_requests}')
print('_' * 25)
print('Your files are ready :D')
print('_' * 25)
# =====================================================