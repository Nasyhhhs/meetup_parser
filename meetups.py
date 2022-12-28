from datetime import datetime
import requests
from database import check_database, get_events

url = 'https://www.meetup.com/gql'


cookies = {
    '_cookie-check': 'z_A9DQPOA7G4Mbzw',
    'MEETUP_BROWSER_ID': 'id=f7bf0ff6-df6e-43fc-b5d6-cfe2721278fb',
    'MEETUP_AFFIL': 'affil=meetup&ref=/www.google.com',
    'MEETUP_CSRF': 'ec7335d2-d298-474d-aaaf-cf474c6015ab',
    '_rm': 'b5427005-c834-40a7-afe0-cbcc22a4d4b5',
    'appbanner_accepted': 'dismissed=0',
    '_gid': 'GA1.2.783316150.1670056673',
    'MEETUP_TRACK': 'id=471b5652-2305-41e5-82e8-286d05fe1a9f&l=1&s=6c6ab2687b1710579bce5d04f3af0800dea255b0',
    'MEETUP_SEGMENT': 'member',
    'ab.storage.deviceId.4e505175-14eb-44b5-b07f-b0edb6050714': '%7B%22g%22%3A%220dd79210-4034-211b-0e91-a4869b72f9ab%22%2C%22c%22%3A1670056997563%2C%22l%22%3A1670056998217%7D',
    'ab.storage.userId.4e505175-14eb-44b5-b07f-b0edb6050714': '%7B%22g%22%3A%22332479700%22%2C%22c%22%3A1670056998213%2C%22l%22%3A1670056998219%7D',
    'ab.storage.sessionId.4e505175-14eb-44b5-b07f-b0edb6050714': '%7B%22g%22%3A%22c0cc6c51-85de-b19d-cf42-9d14de03cf29%22%2C%22e%22%3A1670058883236%2C%22c%22%3A1670056998216%2C%22l%22%3A1670057083236%7D',
    'USER_CHANGED_DISTANCE_FILTER': 'false',
    '___uLangPref': 'en_US',
    'MEETUP_MEMBER': 'id=0&status=1&timestamp=1670140461&bs=0&tz=US%2FEastern&zip=&country=us&city=&state=&lat=0.0&lon=0.0&ql=false&s=1b40730242933b6b2821fb0549745a87a27495e8&scope=ALL',
    '_dc_gtm_UA-3226337-19': '1',
    'MEETUP_MEMBER_LOCATION': '{%22__typename%22:%22Location%22%2C%22city%22:%22Moscow%22%2C%22country%22:%22ru%22%2C%22localized_country_name%22:%22ru%22%2C%22state%22:%22%22%2C%22name_string%22:%22Moscow%2C%20Russia%22%2C%22lat%22:55.75%2C%22lon%22:37.619998931884766%2C%22zip%22:%22meetup1%22%2C%22borough%22:%22%22%2C%22neighborhood%22:%22%22}',
    'MROT_NEXTJS_INDOOR_OUTDOOR_SPLIT_TEST_V2': 'variant',
    'SIFT_SESSION_ID': '7668e3e7-f878-4a15-b8d4-182058899a6a',
    'x-mwp-csrf': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiNWQzYTljMWEtNzViNi00N2U0LTg1YmItY2NmY2IxNzIyOGQ4IiwidHlwZSI6ImNvb2tpZSIsImlhdCI6MTY3MDE0MDU0NX0.xXXd99ZOeBeRCoCfogfRREsUqAOCXGn71EetHVaLz5I',
    'x-mwp-csrf-header': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiNWQzYTljMWEtNzViNi00N2U0LTg1YmItY2NmY2IxNzIyOGQ4IiwidHlwZSI6ImhlYWRlciIsImlhdCI6MTY3MDE0MDU0NX0.pqGKa0ssucMITWjJiTZIpheeHMp3OdzY5ACx_DhyId4',
    '__Host-NEXT_MEETUP_CSRF': '8e4463b5-bd5f-4bbf-bae2-6fa3a1a745ae',
    '_ga': 'GA1.2.1447938155.1670056673',
    '_ga_NP82XMKW0P': 'GS1.1.1670140379.3.1.1670140557.12.0.0',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Dec+04+2022+10%3A55%3A57+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.38.0&isIABGlobal=false&hosts=&consentId=57304bcd-12ce-48fd-bdba-9f6c66528609&interactionCount=1&landingPath=NotLandingPage&groups=C0002%3A1%2CC0001%3A1%2CC0004%3A0%2CC0003%3A1&AwaitingReconsent=false',
}

headers = {
    'authority': 'www.meetup.com',
    'accept': '*/*',
    'accept-language': 'ru-RU',
    'apollographql-client-name': 'nextjs-web',
    'content-type': 'application/json',
    # 'cookie': '_cookie-check=z_A9DQPOA7G4Mbzw; MEETUP_BROWSER_ID=id=f7bf0ff6-df6e-43fc-b5d6-cfe2721278fb; MEETUP_AFFIL=affil=meetup&ref=/www.google.com; MEETUP_CSRF=ec7335d2-d298-474d-aaaf-cf474c6015ab; _rm=b5427005-c834-40a7-afe0-cbcc22a4d4b5; appbanner_accepted=dismissed=0; _gid=GA1.2.783316150.1670056673; MEETUP_TRACK=id=471b5652-2305-41e5-82e8-286d05fe1a9f&l=1&s=6c6ab2687b1710579bce5d04f3af0800dea255b0; MEETUP_SEGMENT=member; ab.storage.deviceId.4e505175-14eb-44b5-b07f-b0edb6050714=%7B%22g%22%3A%220dd79210-4034-211b-0e91-a4869b72f9ab%22%2C%22c%22%3A1670056997563%2C%22l%22%3A1670056998217%7D; ab.storage.userId.4e505175-14eb-44b5-b07f-b0edb6050714=%7B%22g%22%3A%22332479700%22%2C%22c%22%3A1670056998213%2C%22l%22%3A1670056998219%7D; ab.storage.sessionId.4e505175-14eb-44b5-b07f-b0edb6050714=%7B%22g%22%3A%22c0cc6c51-85de-b19d-cf42-9d14de03cf29%22%2C%22e%22%3A1670058883236%2C%22c%22%3A1670056998216%2C%22l%22%3A1670057083236%7D; USER_CHANGED_DISTANCE_FILTER=false; ___uLangPref=en_US; MEETUP_MEMBER=id=0&status=1&timestamp=1670140461&bs=0&tz=US%2FEastern&zip=&country=us&city=&state=&lat=0.0&lon=0.0&ql=false&s=1b40730242933b6b2821fb0549745a87a27495e8&scope=ALL; _dc_gtm_UA-3226337-19=1; MEETUP_MEMBER_LOCATION={%22__typename%22:%22Location%22%2C%22city%22:%22Moscow%22%2C%22country%22:%22ru%22%2C%22localized_country_name%22:%22ru%22%2C%22state%22:%22%22%2C%22name_string%22:%22Moscow%2C%20Russia%22%2C%22lat%22:55.75%2C%22lon%22:37.619998931884766%2C%22zip%22:%22meetup1%22%2C%22borough%22:%22%22%2C%22neighborhood%22:%22%22}; MROT_NEXTJS_INDOOR_OUTDOOR_SPLIT_TEST_V2=variant; SIFT_SESSION_ID=7668e3e7-f878-4a15-b8d4-182058899a6a; x-mwp-csrf=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiNWQzYTljMWEtNzViNi00N2U0LTg1YmItY2NmY2IxNzIyOGQ4IiwidHlwZSI6ImNvb2tpZSIsImlhdCI6MTY3MDE0MDU0NX0.xXXd99ZOeBeRCoCfogfRREsUqAOCXGn71EetHVaLz5I; x-mwp-csrf-header=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiNWQzYTljMWEtNzViNi00N2U0LTg1YmItY2NmY2IxNzIyOGQ4IiwidHlwZSI6ImhlYWRlciIsImlhdCI6MTY3MDE0MDU0NX0.pqGKa0ssucMITWjJiTZIpheeHMp3OdzY5ACx_DhyId4; __Host-NEXT_MEETUP_CSRF=8e4463b5-bd5f-4bbf-bae2-6fa3a1a745ae; _ga=GA1.2.1447938155.1670056673; _ga_NP82XMKW0P=GS1.1.1670140379.3.1.1670140557.12.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Dec+04+2022+10%3A55%3A57+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.38.0&isIABGlobal=false&hosts=&consentId=57304bcd-12ce-48fd-bdba-9f6c66528609&interactionCount=1&landingPath=NotLandingPage&groups=C0002%3A1%2CC0001%3A1%2CC0004%3A0%2CC0003%3A1&AwaitingReconsent=false',
    'dnt': '1',
    'origin': 'https://www.meetup.com',
    'referer': 'https://www.meetup.com/ru-RU/find/?source=EVENTS&location=ru--moscow',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-meetup-view-id': '5495b766-9e31-42b8-a104-9a276e6d051e',
}

json_data = {
    'operationName': 'categorySearch',
    'variables': {
        'first': 20,
        'lat': 55.75,
        'lon': 37.619998931884766,
        'topicCategoryId': None,
        'startDateRange': '2022-12-04T04:55:41-05:00[US/Eastern]',
        'sortField': 'RELEVANCE',
    },
    'extensions': {
        'persistedQuery': {
            'version': 1,
            'sha256Hash': '0ca30be8284bba1da75641c66b3c7d7bee9e6995a0941004952eacf4d23b2acd',
        },
    },
}

def get_json(url):
    response = requests.post(url, cookies=cookies, headers=headers, json=json_data)

    r = response.json()
    items = r['data']['rankedEvents']['edges']
    return items


def get_event(item):
    event = {}
    event['event_id'] = item.get('node').get('id')
    event['title'] = item.get('node').get('title')
    #city = item.get('node').get('venue').get('city')
    dt = item.get('node').get('dateTime')[0:-6]
    event['url'] = item.get('node').get('eventUrl')
    event['date'] = datetime.strptime(dt, fmt).strftime("(%d %B %Y - %H:%M)")

    return event



def main():
    data = get_json(url)
    get_events(data)

if __name__ == '__main__':
    main()