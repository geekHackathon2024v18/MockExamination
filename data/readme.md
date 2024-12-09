# データベース操作の仕方

## 1. 準備

`SqlAlchemyControl`クラスを呼び出す

``` python
from data.database.sql_alchemy_control import SqlAlchemyControl
db = SqlAlchemyControl() # SqlAlchemyControlクラスのインスタンスを生成
```

## 2. 基本操作

このクラスでは、それぞれのデータベーステーブルに対して5つの操作をすることができる。

* テーブルの作成（一番最初だけ）
* テーブルにデータを**追加**
* テーブルのデータを**編集**
* テーブルのデータを**読み出す**
* テーブルのデータを**削除**

### テーブルの作成

``` python
db.create_table() # テーブルの作成
```

* `data/table`のフォルダにある、`Base`クラスを継承したクラスのモデルがこの関数を呼び出すことで`sample.db`にテーブル情報が作成される。
* もし`sample.db`ではなく任意のdbファイルを作成したい場合はインスタンス生成時にファイル名を指定する

``` python
db = SqlAlchemyControl(db_path="任意のファイル名.db")
```

### テーブルにデータを追加

* 今現在テーブルは5種類ある。`db.insert.<テーブル名>()`で追加する関数を呼び出せる
* テーブルごとに引数が異なるので、vscodeのサジェストをよく確認すること
  * 引数を渡すときは`引数名="値"`で指定しないとエラーになる

#### subjectテーブル（科目の情報)

``` py
db.insert.subject(subject_name="修学基礎")

```

#### mock_examinationテーブルとquestionテーブル（試験問題の情報）

* この2つはセットで入れる。まず、`db.insert.question_stack()`で問題の内容を関数で追加してから`db.insert.mock_examination()`で問題を追加する
* `db.insert.mock_examination()`の引数`subject_id`は追加の時点でどの科目か、ユーザーに入力してもらうことで引数に渡す
  * もしめんどくさかったら、subjectになんでもっていう科目作っておいて、特に指定がなければそこに追加するようにすればいい
  * idの確認は、readメソッド(後述)から読み取る

``` py
# ごめんだけど、ここだけQuestionTypeクラスのインポートをお願いします
'''
    現状、記述式しか対応できてないんで、DESCRIPTIVEを選択してください
    CHOICE_4 -> 4択問題
    CHOICE_2 -> 2択問題(or マルバツ問題)
    DESCRIPTIVE -> 記述式問題
'''
from data.table.question import QuestionType

# 入れたい問題数分追加する。大量にあるなら、辞書型の配列を作ってfor文で入れるようにするといいと思う。
db.insert.question_stack(
    question_sentence="問題文"
    question_type=QuestionType.DESCRIPTIVE
    answer="問題の正解"
)

db.insert.mock_examination(
    subject_id=1 # 科目に対応するidを入れる
    mock_examination_name="問題名"
    # time_limit=60 # 時間制限(分)をつけるなら、入れる（入れなくてもいい)
)
```

#### mock_examination_responseテーブルとquestion_responseテーブル(回答情報)

* これも上2つと同じように、問題に対する回答情報を入れてからmock_examination_response(どの問題に対しての回答か)を追加する
* もし時終わってなかった場合、解いた問題だけを追加する。読み出したときに問題セットから解いた問題のidを引いて、追加されてない問題を続きから解いてもらう
* `db.insert.mock_examination_response()`の引数`mock_examination_id`は、`db.insert.mock_examination()`のように、readメソッドから読み取って追加する。

```python
db.insert.question_response_stack(
    question_id=1 # 試験問題の問いを特定するid(question_id)を入れる
    response_content="回答文" # 入力された回答を入れる
)

db.insert.mock_examination_response(
    mock_examination_id=1 # どの試験問題を解いたのかを特定するidをつける
    interruption=False # 中断して保存したならTrue
)

```

### テーブルのデータを編集

* 編集は`db.update.<テーブル名>()`を呼び出す
* updateでは、insertの時に追加した引数を基本的に追加する
* どのデータに編集すればいいかを教えるためにidを渡す
  * これもreadとかのメソッドで確認する
* 変更のない部分は既存の情報を再度入れること
* これも、vscodeの引数のサジェストをよく確認すること

#### subjectの例

```py
db.update.subject(
    subject_id=1 # それぞれ入れたい数字を入れる
    subject_name="編集後の科目名"
)
```

* 他の例は省略
* サジェストをよく見て

### テーブルの読み取り

* 読み取りは`db.read.<テーブル名>()`を呼び出す
* 呼び出し方は各テーブルに2種類ずつあって、保存されてるデータを全て呼び出すメソッドと、id指定で1つだけ取り出すメソッドがある
* テーブルごとにどのデータがあるのかは、`data/table`ファイルにあるクラスの情報を確認する

#### subjectの読み取り

```py
# 全て読み出す
subject_list = db.read.subject() # リストが返される
for subject in subject_list:
    print(subject) # Subject型の値
    print(subject.id) # subjectのid
    print(subject.subject_name) # subjectの名前(修学基礎とか)

# 一つだけ読み出す
subject = db.read.subject(subject_id=1)
print(subject.id) # 読み出す時に入れたidと同じのはず
print(subject.subject_name)
```

#### questionとquestion_response

* この2つのテーブルは、mock_examination(_response)ありきのデータで、全部読み出すと多分大量になってしまうと考えて、強制でmock_examination(_response)_idを指定するようにしている

全ての問題を読み出すには次のように書く

``` py
# mock_examination（試験問題）ごとに問題を読み出す
mock_examination_list = db.read.mock_examination()
for mock_examination in mock_examination_list:
    # 取り出されたmock_examinationデータのidをもとにquestionを読み出す
    question_list = db.read.question(mock_examination_id = mock_examination.id)
    for question in question_list:
        print(question)

```

* question_responseについても同じ要領で読み出す

### テーブルの削除

* テーブルの削除は`db.delete.<テーブル名>_by_id()`を呼び出す
* 削除については、全てid指定にしている

#### subjectの削除

``` py
db.delete.subject_by_id(subject_id=1) # 削除したいsubjectのidを指定

```

* readメソッドで確認すると消えてるはず
