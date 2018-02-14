import requests
import json


def get_reps(user_name):
    data = []
    get_url = requests.get('https://api.github.com/users/{}/repos'.format(user_name))
    reps = json.loads(get_url.text)

    try:
        reps[0]['name']
    except:
        return 'Invalid user'

    for repo in reps:
        rep_name = repo['name']
        repo_url = requests.get('https://api.github.com/repos/{}/{}/commits'.format(user_name, rep_name))
        reps_info = json.loads(repo_url.text)
        data.append('Repo: {} Number of commits: {}'.format(rep_name, len(reps_info)))
    return data

def main():
    user_name=input('Please enter a name: ')
    print(get_reps(user_name))
if __name__ == '__main__':
    main()
