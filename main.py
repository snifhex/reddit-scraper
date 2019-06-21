import csv
import praw
import json

def auth():
    with open('credentials.json', 'r') as json_obj:
        credentials = json_obj.read()
    credentials = json.loads(credentials)
    print(credentials)
    username = credentials['username']
    password = credentials['password']
    client = credentials['client_id']
    secret = credentials['client_secret']
    agent = credentials['user_agent']
    reddit = praw.Reddit( username=username, password=password, 
            client_id=client, client_secret=secret, user_agent=agent)
    # user = reddit.user.me()
    print(reddit.user.me())
    return reddit

def export_upvoted():
    pass

def export_downvoted():
    pass

def export_submissions():
    pass

def export_comments():
    pass

def export_saved(user):
    saved = user.saved()
    links = {str(_id):"reddit.com"+_id.permalink for _id in saved}
    toCsv(links)
    return links

def toCsv(links_dict):
    with open('saved.csv', 'w') as doc:
        writer = csv.writer(doc)
        for key, value in links_dict.items():
            writer.writerow((key, value))

def main():
    reddit = auth()
    user = reddit.user.me()
    links = export_saved(user)
    #print(links[''])

if __name__ == '__main__':
    main()


