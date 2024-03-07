import json


def main():
    myDict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        with open('json_data.json', 'w', encoding='utf-8') as f:
            json.dump(myDict, f)
    except FileNotFoundError:
        print('写入文件失败！')
    print('写入文件成功！')


if __name__ == '__main__':
    main()
