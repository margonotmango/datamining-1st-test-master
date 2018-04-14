# coding: utf-8
import pandas as pd
import csv
import codecs
import numpy
import matplotlib.pyplot as plt
import statsmodels.api as sm

path = "/Users/margo/Downloads/Building_Permits.csv"
data = pd.read_csv(path, encoding='utf-8')
csvFile = codecs.open(path, 'r', 'utf-8')

NominalAttribute = ['Permit Type', 'Block', 'Lot', 'Street Number', 'Street Number Suffix', 'Street Name', 'Street Suffix',
                    'Current Status', 'Structural Notification', 'Voluntary Soft-Story Retrofit', 'Fire Only Permit',
                    'Existing Use', 'Proposed Use', 'Plansets', 'TIDF Compliance', 'Existing Construction Type',
                    'Proposed Construction Type', 'Site Permit', 'Supervisor District', 'Neighborhoods - Analysis Boundaries']
# 数值属性
NumericalAttribute = ['Number of Existing Stories', 'Number of Proposed Stories',
                      'Estimated Cost', 'Revised Cost', 'Existing Units', 'Proposed Units']


def frequency(NominalAttribute, data):
    for n in NominalAttribute:
        doc = open('frequencyOfNominalAttribute.txt', 'a')
        print('*************** %s ***************' % n, file=doc)
        print(data[n].value_counts(), file=doc)
        doc.close()


def describeNumericalAttribute(NumericalAttribute, data):
    for n in NumericalAttribute:
        doc = open("describeNumericalAttribute.txt", 'a')
        print('*************** %s ***************' % n, file=doc)
        print("max:%s" % (data[n].max()), file=doc)
        print("min:%s" % (data[n].min()), file=doc)
        print("mean:%s" % (data[n].mean()), file=doc)
        print("median:%s" % (data[n].median()), file=doc)
        print("quantile1:%s" % (data[n].quantile(0.25)), file=doc)
        print("quantile2:%s" % (data[n].quantile(0.5)), file=doc)
        print("quantile3:%s" % (data[n].quantile(0.75)), file=doc)
        print("theNumberOfNull:%s" % (data[n].count()), file=doc)
        doc.close


rowSize = 3
colSize = 3
cellSize = rowSize * colSize


def histogram(NumericalAttribute, data):
    for i, col in enumerate(NumericalAttribute):
        if i % cellSize == 0:  # 一页有cellSize张子图，如果第i列是第cellSize+1张图，就另起一页
            fig = plt.figure()
        ax = fig.add_subplot(rowSize, colSize, (i % cellSize) + 1)
        data[col].hist(ax=ax, grid=False,
                       bins=50, facecolor='red', edgecolor='black')
        plt.title(col)
        if (i + 1) % cellSize == 0 or i + 1 == len(NumericalAttribute):
            plt.subplots_adjust(wspace=0.3, hspace=0.3)
            plt.show()


def qq(NumericalAttribute, data):
    for i, col in enumerate(NumericalAttribute):
        if i % 6 == 0:
            fig = plt.figure()
        ax = fig.add_subplot(2, 3, (i % 6) + 1)
        sm.qqplot(data[col], ax=ax)
        ax.set_title(col)
        if (i + 1) % 6 == 0 or i + 1 == len(NumericalAttribute):
            plt.subplots_adjust(wspace=0.3, hspace=0.3)
            plt.show()


def boxplot(NumericalAttribute, data):
    for i, col in enumerate(NumericalAttribute):
        if i % cellSize == 0:
            fig = plt.figure()
        ax = fig.add_subplot(colSize, rowSize, (i % cellSize) + 1)
        data[col].plot.box(ax=ax)
        if (i + 1) % cellSize == 0 or i + 1 == len(NumericalAttribute):
            plt.subplots_adjust(wspace=0.3, hspace=0.3)
            plt.show()


def compare(df1, df2, columns, bins=50):
    for col in columns:
        mean1 = df1[col].mean()
        mean2 = df2[col].mean()

        fig = plt.figure()
        ax1 = fig.add_subplot(121)
        df1[col].hist(ax=ax1, grid=False, figsize=(15, 5),
                      bins=bins, edgecolor='black', facecolor='red')
        ax1.axvline(mean1, color='r')
        plt.title('original\n{}\nmean={}'.format(col, str(mean1)))
        ax2 = fig.add_subplot(122)
        df2[col].hist(ax=ax2, grid=False, figsize=(15, 5),
                      bins=bins, edgecolor='black', facecolor='green')
        ax2.axvline(mean2, color='b')
        plt.title('filled\n{}\nmean={}'.format(col, str(mean2)))
        plt.subplots_adjust(wspace=0.3, hspace=10)
        plt.savefig('/Users/margo/Desktop/ScreenShot/%s.jpg' %
                    col, format='jpg')


#frequency(NominalAttribute, data)
#describeNumericalAttribute(NumericalAttribute, data)
#histogram(NumericalAttribute, data)
#qq(NumericalAttribute, data)
#boxplot(NumericalAttribute, data)
# 缺失值处理
# 剔除缺失值，进行直方图比较

NullValue = ['Structural Notification', 'Voluntary Soft-Story Retrofit',
             'Fire Only Permit', 'TIDF Compliance']
'''df_dropna = data.dropna()
print(df_dropna.shape)'''


df_fillna = data[NullValue].fillna('NA')

doc = open('frequencyOfNominalAttribute.txt', 'a')
print('original:', file=doc)
doc.close()
frequency(NullValue, data)

doc = open('frequencyOfNominalAttribute.txt', 'a')
print('\nnew:', file=doc)
doc.close()
frequency(NullValue, df_fillna)
