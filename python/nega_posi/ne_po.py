#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import MeCab
import pandas as pd

# Constants
MECAB_MODE = 'mecabrc'
PARSE_TEXT_ENCODING = 'utf-8'

#単語感情極性辞書読み込み
PN_DIC = pd.read_csv("pn_ja.dic", header=None, names=('word', 'yomi', 'pos', 'score'), encoding='utf-8')

### Functions
def main():
    argvs = sys.argv
    argc = len(argvs)
    if (argc != 2):   # 引数が足りない場合は、その旨を表示
        print 'Usage: # python %s <text>' % argvs[0]
        quit()         # プログラムの終了
    instr = argvs[1]
    print "TEXT=[" + instr + "]"
    print str(score(instr.decode('utf-8')))
    return

def score(unicode_string):
    tagger = MeCab.Tagger(MECAB_MODE)
    # str 型じゃないと動作がおかしくなるので str 型に変換
    text = unicode_string.encode(PARSE_TEXT_ENCODING)
    node = tagger.parseToNode(text)

    sum_score = 0
    cnt = 0
    while node:
        pos = node.feature.split(",")[0]
        if pos != "名詞" and pos != "動詞" and pos != "形容詞" and pos != "副詞":
            node = node.next
            continue
        # unicode 型に戻す
        word = node.surface.decode("utf-8")
#        word = node.feature.decode("utf-8")
        #一つの単語に複数のスコアがつく場合があるが、足し合わせる。例)敵：かたき(-0.018981)、てき(-0.999579)
        tmp = float(PN_DIC[PN_DIC.word==word].score.mean())
        if str(tmp) == "nan":
            node = node.next
            continue
        print "WORD=[" + word + "]\t" + "SCORE=[" + str(tmp) + "]"
        sum_score += tmp
        cnt+=1
        node = node.next
    return sum_score / cnt

### Execute
if __name__ == "__main__":
    main()
