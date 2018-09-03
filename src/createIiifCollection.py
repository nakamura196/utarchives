import urllib.request
import json

flg = True
page = 1

outputPath = "../data/collection.json"

prefix = "https://webpark5029.sakura.ne.jp/uta/"

collection = dict()
collection["@context"] = "http://iiif.io/api/presentation/2/context.json"
collection["@id"] = "https://park.itc.u-tokyo.ac.jp/UTArchives/utarchives-dump/collection.json"
collection["@type"] = "sc:Collection"
manifests = []
collection["manifests"] = manifests

while flg:
    url = prefix + "api/items?page=" + str(page)
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

                omeka_id = obj["o:id"]
                if len(obj["o:media"]) > 0:
                    manifest_uri = prefix + "iiif/" + str(omeka_id) + "/manifest"

                    manifest = dict()
                    manifests.append(manifest)
                    manifest["@id"] = manifest_uri
                    manifest["@type"] = "sc:Manifest"
                    manifest["label"] = obj["dcterms:title"][0]["@value"]

        else:
            flg = False

    except:
        pass

fw = open(outputPath, 'w')
json.dump(collection, fw, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
