import os,thulac,jieba,json
def cut():
    cutmodel = thulac.thulac()
    train_dirs = os.listdir("data/train/")
    ans = {}
    for dir in train_dirs:
        if dir.endswith('.txt'):
            train = open("data/train/" + dir, 'r', encoding='utf-8').read()
            res = cutmodel.cut(train)
            ans[dir] = res
            print(dir + ' Done！')
    with open("data/cutresult.json", 'w') as f:
        json.dump(obj=ans, fp=f)
    f.close()
def reloadjson():
    data=json.load(open("cutresult.json",'r'))

def process_ann():
    pass

if __name__=="__main__":
    reloadjson()







