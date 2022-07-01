"""
問5
クリーンアップ動作を定義してあるオブジェクトに対して、
クリーナップ動作を保証した形で利用するための構文で適切なものを選びなさい。
"""

# 正解
with

"""
問9
対話環境でのヒストリ情報が保存されているファイルを選択肢の中から選びなさい。
"""
# 正解
.python_history

"""
問16 
以下のプログラムを実行した際の出力結果を選びなさい。 
"""
print(range(5))
# 正解 
range(0, 5)

"""
問19 
リストから、引数の値(x)の最初のアイテムを削除するメソッドを選びなさい。 
"""
# 正解 
list.remove(x)

"""
問22
ファイルの読み書きで使用する「open」関数のモードについて、存在しないものを選択肢の中から選びなさい。
"""
# 正解
r-

"""
問27 
以下のプログラムを実行した際の出力結果として正しいものを選択しなさい。
""" 
dic = 'diveintocode'

print(dic[1:10:2])
# 正解
i

"""
問31 
Pythonの関数について正しいものを選択肢から選びなさい。 
"""
# 正解
関数をコールするときは、必ず位置引数が先でキーワード引数を後にしなければならない。

"""
問32 
以下のプログラムを実行した際の出力結果として正しいものを選択しなさい。 
"""
member = {1: 'Noro', 2: 'Nakao', 3: 'Miyaoka'}
member[4] = 'Kimura'
del member[3]

print(list(member.keys()))
# 正解 
[1, 2, 4]

"""
問35 
プログラムを実行し、下記の実行結果を得たい。 
"""
Noro
Miyaoka
# 下記のプログラムの(A)に記述すべきコードを選択肢から選びなさい。 

class DiveIntoCode:
    def __init__(self, teacher, mentor):
        self.teacher = teacher
        self.mentor  = mentor 

(A)

print(dic.teacher)
print(dic.mentor)

# 正解 
dic = DiveIntoCode('Noro', 'Miyaoka')

"""
問37 
以下のプログラムを実行した際の出力結果を選びなさい。 
"""
a = 2
b = 5

c = 3.0 + b, 5 * a

print(c)

# 正解 
(8.0, 10)