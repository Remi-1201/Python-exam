# 2022/06/11

'''問5
ビルドイン関数dir()についての適切なものを選びなさい。'''

# 正解
モジュールが定義している名前を確認することができる。
 

'''問6
正規表現ツールを提供するモジュールを選択肢の中から選びなさい。'''

# 正解
re 

'''問7
コマンドライン引数を取得するためのモジュールを選択肢の中から選びなさい。
'''
# 正解
sys

'''問8
ログを取得するためのモジュールを選択肢の中から選びなさい。'''

# 正解
logging
 
'''問9
バイナリデータレコードの処理を行うモジュールを選択肢の中から選びなさい。'''

# 正解
struct 

'''問12
pythonインタプリタにて

D:\home\name\python
と出力させるための入力として正しいものを選びなさい。'''

# 正解
print(r'D:\home\name\python') 

'''問13
以下のプログラムを実行した際の出力結果を選びなさい。'''

for i in range(20):
    if i%3 == 0:
        print(""{}は3で割り切れます"".format(i), end=' ')
    elif i>8 and i%2 == 0:
        break
    else:
        continue"

# 正解
# 0は3で割り切れます 3は3で割り切れます 6は3で割り切れます 9は3で割り切れます 

'''問15
以下のプログラムを実行した際の出力結果を選びなさい。'''

num_list  = [2, 4, 6, 4, 4, 2, 6]
for i in range(num_list.count(4)):
    print(i, end=' ')"

# 正解
0 1 2 

'''問20
sys.pathの初期化で参照しないものを、
選択肢の中から選びなさい。'''

# 正解
スクリプトが存在するフォルダのシンボリックリンク先

'''問21
コンパイル済Pythonファイルの拡張子を、
選択肢の中から選びなさい。'''

# 正解
pyc 

'''問22
以下のプログラムを実行した際に出力される例外の型を選びなさい。'''

x = 10/0

# 正解 

'''問23
次の中からmutableなものをまとめたものとして適切なものを選びなさい'''

# 正解
リスト 

'''問24
以下のプログラムを実行した際の出力結果を選びなさい。'''

name1,name2,name3,name4= '', 'suzuki','tanaka','sato'
selected_name = name1 or name2 or name3 or name4

print(selected_name)

# 正解
suzuki 

'''問25
以下のプログラムを実行した際の出力結果を選びなさい。'''

d = 'dive\ninto\ncode\t'

print(len(d))

# 正解
15 

'''問27
以下のプログラムを実行した際の出力結果として正しいものを選択しなさい。'''

num = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10]]

col = [row[2] for row in num]

print(col)

# 正解
[3, 8] 

'''問29
以下のプログラムを実行した際の出力結果として正しいものを選択しなさい。'''

dive_into_code = [(1, 'Noro'), (2, 'Nakao'), (3, 'Miyaoka'), (4, 'Kimura')]
dic = dive_into_code
dic.sort(key=lambda dic: dic[1])

print(dic)

# 正解
[(4, 'Kimura'), (3, 'Miyaoka'), (2, 'Nakao'), (1, 'Noro')] 

'''問31
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

'''問32
プログラムを実行し、下記の実行結果を得たい。'''

Miyashita

# 下記のプログラムの(A)に記述すべきコードを選択肢から選びなさい。

dive_into_code = ['Noro', 'Nakao', 'Miyaoka', 'Miyashita', 'Shibata', 'Kimura']

(A)

print(ex_mentor)

# 正解
ex_mentor = dive_into_code.pop(3) 

'''問33
以下のプログラムを実行した際の出力結果として正しいものを選択しなさい。'''

dic = [
    ['Noro', 'Nakao', 'Miyaoka'],
    ['Kimura', 'Miyashita', 'Shibata'],
    ['Matsumoto', 'Tanaka', 'Ivan'],
]

print(list(zip(*dic)))

# 正解
[('Noro', 'Kimura', 'Matsumoto'), ('Nakao', 'Miyashita', 'Tanaka'), ('Miyaoka', 'Shibata', 'Ivan')]
 
'''問34
プログラムを実行し、下記の実行結果を得たい。'''

2017-09-11
# 下記のプログラムの(A)及び(B)に記述すべきコードの組み合わせを選択肢から選びなさい。

from (A) import (B)
now = date.today()
print(now)

# 正解
(A)datetime (B)date 

'''問38
Pythonインタプリタにて以下のように入力した場合の出力結果として正しいものを選びなさい。'''

import reprlib
reprlib.repr(set('diveintocode'))

# 正解
"{'c', 'd', 'e', 'i', 'n', 'o', ...}" 

'''問39
Pythonの変数に関する記述として正しいものを選択肢から選びなさい。'''

# 正解
関数内で変数に代入を行うと、その値がローカル変数のシンボル表に記録される 

'''問40
下のユーザー定義例外について正しいものを選びなさい。'''

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# 正解
このユーザー定義例外は、Exceptionクラスのデフォルトの__init__をオーバーライドしている。 
