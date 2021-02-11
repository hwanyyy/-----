import json
import os
from os.path import join
import pickle
import glob

json_path = 'json_labels'           # json_utf-8
yolo_label_path = 'yolo_labels'     # only label

def save_to_utf8():
    # unicode json path
    ori_json_path = './json'
    json_list = [x for x in os.listdir(join(ori_json_path)) if x.endswith('.json')]

    for i in json_list:
        print(i)
        with open(join(ori_json_path, i), 'r', encoding='utf-8') as f:
            json_f = json.load(f)
            with open(join(json_path, i), 'w', encoding='utf-8') as f:
                json.dump(json_f, f, ensure_ascii=False, indent = 4)


def label_to_int():
    json_list = [x for x in os.listdir(join(json_path)) if x.endswith('.json')]

    label_list = []

    for file in json_list:
        with open(join(json_path, file), 'r', encoding='utf-8') as f:
            json_f = json.load(f)
            for i in json_f['annotations']:   
                try:   
                    key = list(i['attributes'].keys())[0]
                    if key == '일반차량' or key == '목적차량(특장차)':
                        label_list.append('차량')
                        continue
                    label_list.append(key)
                except IndexError as e:
                    print('error : ', e, ' |  file name : ', file) # index e
    label_list = list(set(label_list))
    label_dict = dict((v,k) for k,v in enumerate(label_list))

    # save data
    with open('labels.pickle','wb') as fw:
        pickle.dump(label_dict, fw)
        print(label_dict)


def format_yolo_label():
    json_list = [x for x in os.listdir(join(json_path)) if x.endswith('.json')]
    
    # load data
    with open('labels.pickle', 'rb') as fr:
        label_dict = pickle.load(fr)
        print(label_dict)

    for file in json_list:
        with open(join(json_path, file), 'r', encoding='utf-8') as f:
            json_f = json.load(f)
            absolute_width = json_f['metadata']['width']
            absolute_height = json_f['metadata']['height']
            filename = json_f['filename'][:-3] + 'txt' 
            
            with open(join(yolo_label_path, filename), 'w') as f:
                for i in json_f['annotations']:
                    
                    key = list(i['attributes'].keys())[0]            
                    if key == '일반차량' or key == '목적차량(특장차)': key = '차량'

                    # yolo labels format -> <object-class> <x_center> <y_center> <width> <height>
                    object_class = label_dict.get(key)                
                    points = i['points']
                    x_center = round(abs((points[1][0] + points[0][0])) / 2 / absolute_width, 6)
                    y_center = round(abs((points[2][1] + points[1][1])) / 2 / absolute_height, 6)
                    width = round(abs(points[1][0] - points[0][0]) / absolute_width, 6)
                    height = round(abs(points[2][1] - points[1][1]) / absolute_height, 6)

                    # save file
                    print(object_class, x_center, y_center, width, height, file=f)


def remove_none_object():
    label_list = [x for x in os.listdir(yolo_label_path) if x.endswith('.txt')]
    empty_labels = []

    for file in label_list:
        with open(join(yolo_label_path, file), 'r', encoding='utf-8') as f:
            if f.readline() == '': 
                empty_labels.append(file)
    
    print('empty file: ', len(empty_labels))

    # remove empty label & image
    path = 'test'   # include both image and label

    for f in empty_labels:
        name, ext = os.path.splitext(f)
        os.remove(join(path, name + ext))    # remove .txt
        os.remove(join(path, name + '.png')) # remove .png


if __name__ == "__main__":
    # save_to_utf8()
    # label_to_int()
    # format_yolo_label()
    remove_none_object()