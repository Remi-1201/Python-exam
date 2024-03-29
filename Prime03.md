#### 9.次のコードの出力結果として正しいものはどれか。 

fruits = ['apple', 'kiwi', 'plum'] <br>
for f in fruits[:]: <br>
    if len(f) < 5: <br>
        fruits.insert(0, f) <br>
        fruits.pop() <br>

print(fruits, end = ' ') <br>
あなたの回答: ['kiwi', 'apple', 'plum'] <br>
正答: ['plum', 'kiwi', 'apple'] <br>

#### 19.コードAの1行目を代替するコードBがある。コードBの【A】～【C】のうち、【A】と【B】に入るものとして正しいものはどれか。

[ コードA ] <br>
cubes = [ a ** 3 for a in range(5)] <br>
print(cubes) <br>

[ コードB ] <br>
cubes = 【A】(【B】(【C】 a: a ** 3, range(5))) <br>
あなたの回答: 【A】list　【B】loop <br>
正答: 【A】list　【B】map <br>

#### 31.
次の実行結果を得たい場合、コードの【A】【B】【C】【D】【E】に入る組み合わせとして適切なものはどれか。 <br>

[ 実行結果 ] <br>
Magatama is a <br>
Saya's <br>
reliable <br>
partner <br>

[コード] <br>
class kusanagi(Exception): <br>
    pass <br>
 <br>
def raise_character(a): <br>
    print("【A】") <br>
    raise kusanagi <br>
    print("【B】") <br>

def func(name: int): <br>
    try: <br>
        print(name, "【C】") <br>
        raise_character(name) <br>
    except kusanagi: <br>
        print("【D】") <br>
        raise Exception <br>

name = "Magatama" <br>
try: <br>
    func(name) <br>
except Exception: <br>
    print("【E】") <br>
あなたの回答: 【A】reliable【B】goofy【C】is a【D】Saya's【E】partner <br>
正答: 【A】Saya's【B】goofy【C】is a【D】reliable【E】partner <br>

---

#### 1.Pythonの特徴に関する次の記述のうち、誤っているものはどれか。
**[ F ]** Pythonの特徴の一つが可読性の高さである。複雑な操作も単一文で表記可能であり、文のグルーピングがインデントで行われるためコードの見通しが良いなど、プログラムを小さく読みやすく書けるようになっている。ただ変数の宣言は必要であり行わないとエラーとなる。

**[ T ]** 機械学習、AI、データ分析の分野でPythonが用いられる理由の一つは、Numpyやpandas、scikit-learnなど機械学習向けのサードパーティ製パッケージやそれを用いた環境（Jupyter Notebookなど）が充実していることである。

**[ T ]** Pythonは柔軟な配列や集合、ディクショナリといった、高水準のデータ型を組み込みで持つ。データ型の一般性が高いためPythonの対応可能な問題領域はAwkやPerlと比較して広い。
 
**[ T ]** Pythonは簡単に使えるとはいえ本格的なプログラム言語であり、大きなプログラムを書くために提供された構造やサポート、エラーチェック機構が、シェルスクリプトなどに比べはるかに多く存在する。
 
**[ T ]** PythonはWindows、MacOS、Linuxなど多くの環境で動作する、拡張可能なフリーのオープンソースソフトウェアである。
 
 #### 2.Pythonインタープリタに関する次の記述のうち、誤っているものはどれか。
**[ T ]** Pythonモジュールを呼び出すには、「python -m モジュール名 [引数] …」という方法があり、例えば「python -m timeit -h」を実行すると、timeitモジュールの詳細が出力される。
 
**[ F ]** インタープリタの起動方法として、「python -cmd コマンド [引数] …」という方法があり、例えば「python -cmd 'print("hello")'」を実行すると、「hello」が出力される。
 
**[ T ]** 対話モードの終了方法には、関数の入力によるものと、キー操作によるものとがある。前者の具体的な方法は、quit()の入力である。後者の具体的な方法は、ファイル終端キャラクタの入力である。
 
**[ T ]** インタープリタがスクリプト名（スクリプトのファイル名）と続く引数群を知らされると、これらは文字列のリストとなる。import sys を実行することで、このリストにアクセスできる。
 
**[ T ]** デフォルトでは、PythonのソースファイルはUTF-8でエンコードしてあるものとして扱われる。

#### 3.数値に関する次の記述のうち、誤っているものはどれか。
**[ T ]**  ほとんどの演算子は左から演算が行われるが、例外的にべき乗は右から演算が行われる。例えば「48 // 6 // 4」の演算結果は「2」であり、「2 ** 1 ** 3」の演算結果は「2」である。
 
**[ T ]**  切り下げ除算を行って整数解を得たい場合（剰余を捨てたい場合）は「//」演算子を使い、剰余のみを得たい場合は「%」演算子を使う。
 
**[ T ]**  等号（=）は、変数を代入するのに使う。変数に代入すると参照先が代入され、値のコピーは行われない。
 
**[ T ]**  対話モードでは、最後に表示した式は変数「_」（アンダースコア）に代入される。
 
**[ F ]**  整数はint型、小数点を伴う数はfloat（浮動小数点数）型を持つ。演算対象の型が混合していた場合、浮動小数点数は整数に変換される。また除算は常にfloatを返す。
 
 #### 5.文字列に関する次の記述のうち、誤っているものはどれか。なお「￥」はバックスラッシュに読み替えること。
**[ T ]**  Pythonの文字列は改変ができない「変更不能体（immutable）」なものであるが、文字列のインデックス指定（連番による指定）やスライシング（切取）は可能である。

**[ F ]**  列挙された文字列リテラルは連結される。例えば対話モードで「>>> 'Py' 'thon'」とした場合には、間にスペースを挟んだ形で自動的に連結され「'Py thon'」（yとtの間に半角スペース）となる。

**[ T ]**  トリプルクオート「"""」を使うと、文字列リテラルを複数行にわたって書くことができる。docstring（ドキュメンテーション文字列）でもこの記述方法が使われる。

**[ T ]** バックスラッシュを前置した文字を特殊文字として解釈させないようにするには、raw文字列を使う。具体的には最初の引用符の前に「r」を置いて「print(r'C:￥some￥name')」のように記述する。

**[ T ]** 文字列は「*」で繰り返すことができる。「'He' + 3 * 'y'」は対話型インタープリタで出力「'Heyyy'」が得られる。

#### 17.次の記述のうち、誤っているものはどれか。
**[ T ]** PEP8では、クラスや関数には一貫した命名を行うべきであり、クラスには「CamelCase」を、関数やメソッドには「lower_case_with_underscores」を使うべきとされている。

**[ T ]** トリプルクート「"""」で関数内に記述されたdocstringの内容は、関数の__doc__属性に文字列として格納され、help関数でドキュメントとして表示させることができる。
 
**[ F ]** 関数注釈（アノテーション）は関数の__annotations__属性にリストとして格納され、注釈の内容によっては関数のほかの部分に影響を与えることもある。

**[ T ]** PEP 8では、識別子に非ASCIIキャラクタを使うべきでないとされている。ASCII 範囲内で識別子として有効な文字は、大文字と小文字のアルファベット、アンダースコア、0 から 9の数字である。なお先頭文字は数字以外でなければならない。

**[ T ]** docstringの1行目は、常にオブジェクトの目的の短く簡潔な要約を記述し、2行目以降がある場合、2行目は空行としてようやくと他の記述を視覚的に分離すべきである。

#### 23.データ構造に関する次の記述のうち誤っているものはどれか。
**[ T ]** 集合の生成には中カッコ{}またはset()関数を使用する。ただし空の集合を生成するには、{}ではなくset()を使う必要がある。例えば「empty = {}」とすると空のディクショナリが生成される。

**[ T ]** ディクショナリに対する帰属性判定演算子「in」「not in」による判定において、「含まれるかどうか」の判定の対象は「値」ではなく「キー」である。
 
**[ T ]** リストと集合は変更可能（mutable）、タプルは変更不能（immutable）である。
 
**[ T ]** ディクショナリは変更可能（mutable）であるが、キーの型は変更不能（immutable）であり、その値は一意でなければならない。
 
**[ F ]** ディクショナリにループをかけるときにenumerate()関数を使うと、キーとそれに対応した値を同時に得られる。

#### 25.モジュールに関する次の記述のうち、正しいものはどれか。
**[ F ]** sys.pathが初期化されている場所は、PYTHONPATHとインストールごとのデフォルトであり、入力スクリプトのあるディレクトリは含まれない。
 
**[ F ]** あるモジュールがインポートされるときにインタープリタが検索する順序は、まずビルトインモジュール、次にsys.path変数で得られるディレクトリ、そしてシンボリックリンクを置いてあるディレクトリである。
 
**[ F ]** モジュール読み込みの高速化のため、Pythonはコンパイル済みのモジュールを「__python_cache__」ディレクトリにmodule.バージョン名.pyの名前でキャッシュする。
 
**[ F ]** モジュールの中では、グローバル変数「__modname__」の値としてモジュール名（文字列）がセットされている。
 
**[ T ]** 実行中のスクリプトのあるディレクトリは、検索パスの最初、標準ライブラリのパスよりも前方に置かれる。
 
 #### 27.入出力に関する次の記述のうち、誤っているものはどれか。
**[ T ]** 文字列オブジェクトのrjust()メソッドは、文字列の左側にスペースを追加して、指定の幅に右揃えするものである。
 
**[ T ]** 文字列オブジェクトのzfillメソッドは、プラスとマイナスの記号も含めて指定文字数となるように、数字の文字列の左側をゼロでパディングするものである。
 
**[ T ]** 標準モジュールjsonは、Pythonのデータ階層構造を取って文字列表現にコンバートすることができる。このプロセスを「シリアライズ」という。シリアライズで文字列表現されたオブジェクトは、「デシリアライズ」という。
 
**[ F ]** open()はファイルオブジェクトを返す関数である。open関数は第1引数にファイル名を、第2引数にモードを与えて使う。モードはファイルを読み込み専用で開くなら「r+」、書き出し専用なら「w」、追加なら「r」、読み書き療養なら「a」を指定する。
 
**[ T ]** 値を書き出す方法には、print()関数やwriteメソッドなどがある。出力のフォーマット方法には、文字列スライシングと連結操作で行う方法や、formatメソッドを利用する方法などがある。
 
 #### 29.エラーと例外に関する次の記述のうち誤っているものはどれか。
**[ T ]** raise文を用いることで、指定の例外を意図的に発生させることができる。raiseの引数は送出する例外を示すものであり、例外インスタンスでも、Exceptionクラスの派生クラスであるクラス（例外クラス）でも構わない。
 
**[ T ]** 発生した例外に値が付随することもあり、これを例外の引数と呼ぶ。except 節では、例外名の後に変数を指定することができる。この変数には例外インスタンスが結び付けられており、例外インスタンスには「__str__()」が定義してある。
 
**[ T ]** [Ctrl]+[c]キーなどでユーザーがプログラムに割り込みをかけると、KeyboardInterrupt例外が送出される。
 
**[ F ]** パーサ（構文解釈器）は違反のある行を表示し、最初にエラーが検知された点に下線が引かれる。エラーは矢印より前のトークンが原因である。
 
**[ T ]** 例外のほとんどはプログラムでは処理されず、その結果はエラーメッセージにあらわれる。エラーメッセージの最終行には、NameError、TypeErrorなど例外の型が記されている。
 
 #### 36.モジュールに関する次の記述のうち誤っているものはどれか。
 **[ F ]** processingモジュールを使うと、コード処理の実行時間を計測できる。
 
 **[ T ]** smtplibモジュールを使うと、任意のインターネット上のホストにメールを送ることができる。
 
 **[ T ]** randomモジュールを使うと、疑似乱数を生成することができる。
 
 **[ T ]** urllib.request モジュールを使うと、URLにあるデータを取得することができる。
 
 **[ T ]** statisticsモジュールを使うと、数値データの基本統計量（平均、中央値、分散など）を取得することができる。
 
 #### 39.仮想環境とパッケージに関する次の記述のうち正しいものはどれか。
**[ F ]**  pip install でパッケージ名を指定し、そのパッケージ名の後ろに「=」とバージョン名を付けると、そのバージョンのパッケージをインストールできる。

**[ F ]**  「pip upgrade パッケージ名」とすることで、当該パッケージを最新バージョンにアップグレードすることができる。

**[ F ]**  pip freezeはその仮想環境にインストールされたすべてのパッケージを表示する。pip listも同様の働きをするが、両者は出力形式が異なる。pip listはその仮想環境にインストールされたすべてのパッケージを、pip install向けの形式で出力する。

**[ F ]**  pip uninstall にパッケージ名を指定すると、その仮想環境からパッケージを削除できる。削除対象となるパッケージの複数指定はできない。

**[ T ]**  仮想環境を作成、管理するのに使われるスクリプトはpyvenvである。
 
 #### 40.次の記述に関して正しいものはどれか。
**[ F ]**  デフォルト設定ではユーザーディレクトリの「.pyhistory」ファイルにヒストリが保存される。ヒストリは対話型インタープリタセッションで利用できる。
 
**[ F ]** [Ctrl]+[t]キーを押すと補完機能が呼び出せる。この機能はPythonの文（命令）の名前、現在のローカル変数、使用できるモジュール名を検索するものである。
 
**[ F ]**  拡張された対話型インタープリタとしてBythonがある。これはオブジェクト探索、高度なヒストリ管理などの機能を持つ。
 
**[ F ]**  IPythonは「pip install ipython」でインストールできる。IPythonの対話モードはipythonコマンドで起動できる。終了時はdeactivateコマンドを実行すればよい。
 
**[ T ]** 変数とモジュールの補完機能は、インタープリタの起動時に自動で有効になっている。
