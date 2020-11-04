
import json
import random

json_file = open("train_traffic_sign_dataset.json")
json_object = json.load(json_file)

for anno in json_object["annotations"]:
    id = anno["image_id"]
    image_name_txt = open("/content/sample_data/za_traffic_2020/traffic_train/images/"+id+".txt","a+")
    #image_name_txt = open("" + str(id) + ".txt", "a+")
    bbox = anno["bbox"]
    x = bbox[0]
    y = bbox[1]
    w = bbox[2]
    h = bbox[3]

    clazz = str(int(anno["category_id"])-1)
    line = clazz + " " + str((float(x) + float(w / 2)) / 1622) + " " + str((float(y) + float(h / 2)) / 626) + " " + str(
        int(w) / 1622) + " "+ str(int(h)/626)+"\n"
    print(line,end="")
    image_name_txt.write(line)
    image_name_txt.close()
