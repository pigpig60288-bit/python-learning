'''
教學：sort(key=...) 會依指定的屬性排序。lambda 是簡短函式；此處會從每個包裹取出 weight 作為排序值。

範例：
class Package:
    def __init__(self, code, weight):
        self.code = code
        self.weight = weight

packages = [Package("X1", 6), Package("X2", 2)]
packages.sort(key=lambda package: package.weight)

for package in packages:
    print(package.code, package.weight)
'''

'''
題目 87：整理測驗成績
定義 Score 類別，在 __init__ 中儲存學生姓名 name 和分數 score。
建立 scores 清單，依分數由低到高排列後逐一印出「姓名 分數」。

標準輸入範例 1：

scores = [Score("小美", 87), Score("小華", 56)]

預期輸出 1：

小華 56
小美 87

標準輸入範例 2：

scores = [Score("安安", 92), Score("東東", 68)]

預期輸出 2：

東東 68
安安 92
'''
class Score:
    def __init__(self, name, score):
        self.name = name
        self.score = score

scores = [Score("小美", 87), Score("小華", 56)]
scores.sort(key=lambda name:name.score)

for number in scores:
    print(number.name, number.score)