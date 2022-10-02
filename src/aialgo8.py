import copy

import numpy as np

import read_wakachi

# try:
#     import msvcrt
#     msvcrt.setmode(0, os.O_BINARY)
#     msvcrt.setmode(1, os.O_BINARY)
# except ImportError:
#     pass


def is_str(v):
    return type(v) is str


def words_genkei(keywords: str):
    data_list: list = []
    data: dict = {}
    # ここから処理の内容を書く。
    if is_str(keywords):
        keyws = read_wakachi.parsewithelimination(keywords)
        keys = np.array(keyws.split())

    else:
        keys = np.array(["キーワードを入力してください"])

    for i in range(keys.shape[0]):
        data["word"] = keys[i]
        data_list.append(copy.deepcopy(data))
    return data_list


# if os.path.isfile(dir):
#    tfidfpd = pd.read_csv(dir, header=0, index_col=0)
#    tfidfpd.to_html('./cgi-bin/sample.html')
#    f = open('./cgi-bin/sample.html', 'r')
#    table = f.read()
#    f.close()
#
# else:
#    tfidfpd='何もありません'
#    table = ''
