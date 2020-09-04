# flaskを試してみた。

## 始め方

https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/quickstart.html
より引用

* docker run -it --rm -v $(pwd):/workspace -w /workspace -p 5000:5000 python:3.7-stretch bash
* python3 -m venv venv
* pip install flask
* pip install pytest
* export FLASK_APP=src/main.py
* flask run --host 0.0.0.0

上記でmain.pyをもとにflaskが立ち上がります。

### Debugモード

`export FLASK_ENV=development`を実行し、flask runを実行する

### uWSGIで起動する方法

uWSGIはPython用のAPサーバ実装です。Nginx+uWSGI構成で使います。
使わない場合は`app.run(threaded=True)`などとして実行しないとシングルスレッドで処理するクソ遅いマンになります。

https://www.python.ambitious-engineer.com/archives/1959

* pip install uWSGI
* uwsgi --http=0.0.0.0:5000 --wsgi-file=main.py --callable=app

※srcディレクトリ 内で実行しないとエラーになる。

# Tips

## pipでインストールしたrequirementsをtextに書き出し＆テキストをもとに再インストール

書き出し

```bash
$ pip freeze > requirements.txt
```

再インストール

```bash
$ pip install -r requirements.txt
```

## debugモードで起動する方法

* export FLASK_APP=src/main.py
* export FLASK_ENV=development
* flask run --host 0.0.0.0:5000 --debugger ~~--reload~~

※--reloadをつけておくと、watchしてreloadしてくれる？（.pyファイルのみ？）
→なくてもリロードしてくれる。謎

## venvをvscodeでも使う方法

※推奨
[MS公式のExtension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)をインストールする

* venvを初期化する
  * python3 -m venv .
* vscodeでプロジェクトを開く
* .vscode/setting.jsonに以下のキーを追加
  * key: python.venvPath
    * value: venvを初期化した親ディレクトリ （謎）
  * key: python.pythonPath
    * value: ワークディレクトリ/bin/python3
* cmd + shift + P -> Reload WindowでVSCodeを再起動する
* gitの同期ボタンの隣あたりに指定したvenvのPythonバージョンが表示されていれば成功！
