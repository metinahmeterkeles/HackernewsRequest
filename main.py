import requests

base_url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'

response = requests.get(base_url)

print(f"Status code : {response.status_code}")

submission_ids = response.json()

submission_dicts = []

for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    response = requests.get(url)

    print(f"id: {submission_id} \t status : {response.status_code}")
    response_dict = response.json()

    submission_dict = {
        'title': response_dict['title'],

        'author': response_dict['by'],

        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",

        'article_score': response_dict['score']
    }
    submission_dicts.append(submission_dict)

for submission_dict in submission_dicts:

    print(f"\nTitle: {submission_dict['title']}")

    print(f"Author: {submission_dict['author']}")

    print(f"Discussion link: {submission_dict['hn_link']}")

    print(f"Article Score: {submission_dict['article_score']}")


