#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix

def learn():
    #データの読み込み
    digits = load_digits()
    
    #トレーニングデータとテストデータに分割
    data_train, data_test, label_train, label_test = train_test_split(digits.data, digits.target)
    
    #分類器にパラメータを与える
    estimator = LinearSVC(C=1.0)
    
    #トレーニングデータで学習する
    estimator.fit(data_train, label_train)
    
    #テストデータの予測をする
    label_predict = estimator.predict(data_test)
    
    #結果出力
    print label_predict
    
    #評価
    print confusion_matrix(label_test, label_predict)

if __name__ == "__main__":
    learn()  
