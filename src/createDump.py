import urllib.request
import json

flg = True
page = 1

outputPath = "dump.json"

result = []

while flg:
    url = "https://webpark5029.sakura.ne.jp/uta/api/items?page=" + str(page)
    print(url)

    page += 1

    try:

        # dataがあるとPOSTリクエストになる
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)

        # response = urllib.request.urlopen(url)
        response_body = response.read().decode("utf-8")
        data = json.loads(response_body.split('\n')[0])

        if len(data) > 0:
            for i in range(len(data)):
                obj = data[i]
                result.append(obj)

        else:
            flg = False

    except:
        pass

fw = open(outputPath, 'w')
json.dump(result, fw, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
