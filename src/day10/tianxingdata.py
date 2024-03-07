import requests
import json


def main():
    resp = requests.get(
        'https://apis.tianapi.com/ancbooks/index?key=06a40db6c5e3f52d22f25e6878c2e61b&id=9872ed9fc22fc182')
    data_model = json.loads(resp.text)
    # for news in data_model['newslist']:
    #     print(news['title'])
    data_info = data_model['result']
    print(type(data_info))
    print(data_info)

    data_list = data_info
    print(type(data_list))
    print(data_list)


if __name__ == '__main__':
    main()
