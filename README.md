# MockExamination

## 環境構築

### 1.pipenvのインストール

pipenvが入ってない場合はインストールする

入ってるかどうかの確認

```shell-session
$ pipenv --version
```

バージョンが表示されなければ入ってないので次のコマンドを入力

```shell-session
$ pip pipenv install
```

### 2. 仮想環境上にpipenvでライブラリをインストール

```shell-session
$ pipenv install
```

[参考記事](https://qiita.com/y-tsutsu/items/54c10e0b2c6b565c887a)

## 実行するとき

実行する時、先ほどインストールしたライブラリはpipenvを起動することで読み込めるようになる

### pipenvの起動

```shell-session
$ pipenv shell
```

### pipenvの終了

```shell-session
$ exit
```
