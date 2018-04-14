# coding: utf-8
import pandas as pd
import codecs
import matplotlib.pyplot as plt
import statsmodels.api as sm

path = "/Users/margo/Downloads/NFL Play by Play 2009-2017 (v4).csv"
data = pd.read_csv(path)
csvFile = codecs.open(path, 'r', 'utf-8')

NominalAttribute = ['Date', 'GameID', 'Drive', 'qtr', 'down', 'time', 'TimeUnder', 'TimeSecs', 'SideofField', 'GoalToGo', 'FirstDown', 'posteam', 'DefensiveTeam', 'desc', 'PlayAttempted', 'sp', 'Touchdown', 'ExPointResult', 'TwoPointConv', 'DefTwoPoint', 'Safety', 'Onsidekick', 'PuntResult', 'PlayType', 'Passer', 'Passer_ID', 'PassAttempt', 'PassOutcome', 'PassLength', 'QBHit', 'PassLocation', 'InterceptionThrown', 'Interceptor',
                    'Rusher', 'Rusher_ID', 'RushAttempt', 'RunLocation', 'RunGap', 'Receiver', 'Receiver_ID', 'Reception', 'ReturnResult', 'Returner', 'BlockingPlayer', 'Tackler1', 'Tackler2', 'FieldGoalResult', 'Fumble', 'RecFumbTeam', 'RecFumbPlayer', 'Sack', 'Challenge.Replay', 'ChalReplayResult', 'Accepted.Penalty', 'PenalizedTeam', 'PenaltyType', 'PenalizedPlayer', 'HomeTeam', 'AwayTeam', 'Timeout_Indicator', 'Timeout_Team', 'Season']
NumericalAttribute = ['PlayTimeDiff', 'yrdln', 'yrdline100', 'ydstogo', 'ydsnet', 'Yards.Gained', 'AirYards', 'YardsAfterCatch', 'FieldGoalDistance', 'Penalty.Yards', 'PosTeamScore', 'DefTeamScore', 'ScoreDiff', 'AbsScoreDiff', 'posteam_timeouts_pre', 'HomeTimeouts_Remaining_Pre', 'AwayTimeouts_Remaining_Pre', 'HomeTimeouts_Remaining_Post',
                      'AwayTimeouts_Remaining_Post', 'No_Score_Prob', 'Opp_Field_Goal_Prob', 'Opp_Safety_Prob', 'Opp_Touchdown_Prob', 'Field_Goal_Prob', 'Safety_Prob', 'Touchdown_Prob', 'ExPoint_Prob', 'TwoPoint_Prob', 'ExpPts', 'EPA', 'airEPA', 'yacEPA', 'Home_WP_pre', 'Away_WP_pre', 'Home_WP_post', 'Away_WP_post', 'Win_Prob', 'WPA', 'airWPA', 'yacWPA']
# dict_reader = csv.DictReader(csvFile)
# reader = csv.reader(csvFile)


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
            fig = plt.figure(FIGSIZE=(15, 15))
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

NullValue = ['No_Score_Prob', 'Opp_Field_Goal_Prob', 'Opp_Safety_Prob', 'Opp_Touchdown_Prob', 'Field_Goal_Prob',
             'Safety_Prob', 'Touchdown_Prob', 'ExpPts', 'EPA', 'airEPA', 'yacEPA', 'Home_WP_pre', 'Away_WP_pre',
             'Home_WP_post', 'Away_WP_post', 'Win_Prob', 'WPA', 'airWPA', 'yacWPA']
'''index = data[NullValue].isnull().sum(axis=1) == 0
df_fillna = data[index]
compare(data, df_fillna, NullValue)
'''

# 最高频率值填补，比较
'''df_filled = data.copy()
for col in NullValue:
    most_frequent_value = df_filled[col].value_counts().idxmax()
    df_filled[col].fillna(value=most_frequent_value, inplace=True)
compare(data, df_filled, NullValue)'''


df_filled_inter = data.copy()
# 对每一列数据，分别进行处理
for col in NullValue:
    df_filled_inter[col].interpolate(inplace=True)

compare(data, df_filled_inter, NullValue)
