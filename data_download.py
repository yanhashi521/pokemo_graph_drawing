import urllib.request
import json
import datetime
import os

def load_ids():
    ids = ""
    #APIリクエストで得られたjsonを読み込む
    with open("./season_3.json", 'r', encoding='utf-8') as json_open:
        return json.load(json_open)

def check_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def get_response(url, file_name):
    try:
        with urllib.request.urlopen(url) as response:
            body = json.loads(response.read())
            with open(f'resources//split//{file_name}', 'w') as f:
                json.dump(body, f, indent=4)
        return True
    except urllib.error.URLError as e:
        print(e.reason)
        return False

def make_json(ids):
    for season_number in ids['list'].keys():
        for  season_id in ids['list'][season_number].keys():
            rst = ids['list'][season_number][season_id]['rst']
            ts2 = ids['list'][season_number][season_id]['ts2']
            for i in range(1,6,1):
                url = f'https://resource.pokemon-home.com/battledata/ranking/{season_id}/{rst}/{ts2}/pdetail-{i}'
                file_name = f'Season{season_number}_{"Single" if season_id[4]=="1" else "Double"}_{i}.json'
                if get_response(url, file_name):
                    with open('log', 'a') as f:
                        print(f'{datetime.datetime.now()} | Generated: {file_name}', file=f)

def merge_json(ids):
    for i in ids['list'].keys():
        for j in ids['list'][i].keys():
            rule = "Single" if j[4] == '1' else "Double"
            files = []
            for n in range(1,6,1):
                with open(f'.//resources//split//Season{i}_{rule}_{n}.json', 'r', encoding='utf-8') as json_open:
                    files.append(json.load(json_open))
            jsonMerged = {**files[0], **files[1], **files[2], **files[3], **files[4]}
            file_name = f'Season{i}_{rule}_master.json'
            with open(f'resources//{file_name}', 'w') as f:
                json.dump(jsonMerged, f, indent=4)
            with open('log', 'a') as f:
                print(f'{datetime.datetime.now()} | Merged   : {file_name}', file=f)

if __name__ == "__main__":
    ids = load_ids()
    # ここはお好きなディレクトリを指定
    for path in ['.//resources', './/resources//split']:
        check_dir(path)
    make_json(ids)
    merge_json(ids)
    print('Suceeded')