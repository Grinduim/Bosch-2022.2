# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:38:59 2022

@author: DISRCT
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn

df = pd.read_csv("Dados/iris.csv", header=0)

x= df.iloc[:,:-1]
y= df.iloc[:, -1]


labels=["Setosa", "Versicolor", "Virginica"]

print("\nTamanho do Dataset Completo {} amostras".format(len(x)))
print("{} {} amostras, {} {} amostras, {} {} amostras".format(
        labels[0], y.value_counts()[0],
        labels[1], y.value_counts()[1],
        labels[2], y.value_counts()[2]))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=1500, shuffle=True)

model = svm.LinearSVC(max_iter=10000, random_state=0)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

cm = confusion_matrix(y_test, y_pred)

ST, VcFS, VgFS, SFVc, VcT, VgFVc, SFVg, VcFVg, VgT = cm.ravel()

group_names = ['ST', 'VcFS', 'VgFS', 'SFVc', 'VcT', 'VgFVc', 'SFVg', 'VcFVg', 'VgT']
group_counts = ['{0:0.0f}'.format(value) for value in
                cm.flatten()]
group_percentages = ['{0:.2%}'.format(value) for value in
                      cm.flatten()/np.sum(cm)]

labels = [f'{v1}\n{v2}\n{v3}' for v1, v2, v3 in
          zip(group_names,group_counts,group_percentages)]
labels = np.asarray(labels).reshape(3,3)
seaborn.heatmap(cm, annot=labels, fmt='', cmap='Greens', cbar=False)
plt.xlabel("Valor Previsto")
plt.ylabel("Valor Verdadeiro")

print("\n\nConfusion Matrix :\n")

accuracy = (ST + VcT + VgT)/(ST + VcFS + VgFS + SFVc + VcT + VgFVc + SFVg + VcFVg + VgT)
print("Acurácia de {0:0.2f}%\n".format(accuracy*100))
     
print("Precisões de cada classe:")
setosa_precision = (ST)/(ST + SFVc + SFVg)
versicolor_precision = (VcT)/(ST + SFVc + SFVg)
virginica_precision = (VgT)/(ST + SFVc + SFVg)
print("Precisão da classe Setosa: {0:0.0f}%".format(setosa_precision*100))
print("Precisão da classe Versicolor: {0:0.0f}%".format(versicolor_precision*100))
print("Precisão da classe Virginica: {0:0.0f}%\n".format(virginica_precision*100))

print("Recall de cada classe:")
setosa_recall = (ST)/(ST + VcFS + VgFS)
versicolor_recall = (VcT)/(SFVc + VcT + VgFVc)
virginica_recall = (VgT)/(SFVg + VcFVg + VgT)
print("Recall da classe Setosa: {0:0.2f}%".format(setosa_recall*100))
print("Recall da classe Versicolor: {0:0.2f}%".format(versicolor_recall*100))
print("Recall da classe Virginica: {0:0.2f}%\n".format(virginica_recall*100))

print("F1-Score de cada classe:")
setosa_f1 = (2*setosa_precision*setosa_recall)/(setosa_recall+setosa_precision)
versicolor_f1 = (2*versicolor_precision*versicolor_recall)/(versicolor_recall+versicolor_precision)
virginica_f1 = (2*virginica_precision*virginica_recall)/(virginica_recall+virginica_precision)
print("F1 - Score da classe Setosa: {0:0.2f}%".format(setosa_f1*100))
print("F1 - Score da classe Versicolor: {0:0.2f}%".format(versicolor_f1*100))
print("F1 - Score da classe Virginica: {0:0.2f}%".format(virginica_f1*100))
