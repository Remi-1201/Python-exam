'''問6
問題文のプログラムを実行した場合の、出力結果を選びなさい。'''

print("出力結果:")
try:
  raise Exception("開始前","Exception発生")
  print("開始")
except IOError as msg:
  print("IOError発生:",msg.args[0])
except Exception as msg:
  print("予期せぬ問題発生:",msg.args[1])
else:
  print("Else表示")

# 正解
出力結果:予期せぬ問題発生: Exception発生

https://uxmilk.jp/39845

'''問7
クリーンアップ動作を定義してあるオブジェクトに対して、
クリーナップ動作を保証した形で利用するための構文で適切なものを選びなさい。'''

# 正解
with

'''問17
pythonインタプリタにて以下のように入力した場合の出力結果として正しいものを選びなさい。'''

3*3.72/1.5
# 正解
7.44

'''問18
以下のプログラムを実行した際の出力結果を選びなさい。'''

print(range(5))

# 正解 
range(0, 5)

'''問19
以下のプログラムを実行した際の出力結果を選びなさい。 '''

x = ["a","b","c","d","e"]
print(x[:-3])

# 正解 
['a', 'b']

'''問20
以下のプログラムを実行した際と等価の記述を選択肢の中から選びなさい。'''

t = 123,345,'test'

# 正解 
t = (123,345,'test')

'''問23
以下のプログラムを実行した際の出力結果を選びなさい。'''

import json
x = {'name':'yamada','data':[2,3,4]}
print(json.dumps(x))

# 正解 
{"name": "yamada", "data": [2, 3, 4]}

'''問28
以下のプログラムを実行した際の出力結果として正しいものを選択しなさい。 '''

member = {1: 'Noro', 2: 'Nakao', 3: 'Miyaoka'}
member[4] = 'Kimura'
del member[3]

print(list(member.keys()))

# 正解 
[1, 2, 4]

'''問29
以下のプログラムと同じ出力結果を得たい。''' 

dive_into_code = ['Noro', 'Nakao', 'Miyaoka', 'Miyashita', 'Shibata', 'Kimura']
dive_into_code.clear()

print(dive_into_code)

# 下記のプログラムの(A)に記述すべきコードを選択肢から選びなさい。 
dive_into_code = ['Noro', 'Nakao', 'Miyaoka', 'Miyashita', 'Shibata', 'Kimura']
(A)
print(dive_into_code)

# 正解 
del dive_into_code[:]

'''問31
Pythonインタプリタにて以下のように入力した場合の出力結果として正しいものを選びなさい。'''

from math import pi
[str(round(pi, i)) for i in range(0, 5)]

# 正解 
['3.0', '3.1', '3.14', '3.142', '3.1416']

'''問33 
プログラムを実行し、下記の実行結果を得たい。
Noro
Miyaoka
下記のプログラムの(A)に記述すべきコードを選択肢から選びなさい。 '''

class DiveIntoCode:
    def __init__(self, teacher, mentor):
        self.teacher = teacher
        self.mentor  = mentor
(A)

print(dic.teacher)
print(dic.mentor)

# 正解 
dic = DiveIntoCode('Noro', 'Miyaoka')

'''問35
Pythonにおけるタブ補完について正しいものを選択肢から選びなさい。'''

# 正解
変数とモジュール名の補完はインタプリタの起動時に自動で有効になっており、
[Tab]キーで補完機能が呼び出せる。

'''問36
例外の処理の説明として誤っているものを選択肢から選びなさい。'''

# 正解
else節は全てのexcept節より前でなければならない。

'''問37 
Pythonインタプリタにて以下のように入力した場合の出力結果として正しいものを選びなさい。 '''

import reprlib
reprlib.repr(set('diveintocode'))

# 正解
"{'c', 'd', 'e', 'i', 'n', 'o', ...}"
