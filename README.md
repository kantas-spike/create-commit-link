# create-commit-link

GitHubのコミットへのリンクを作成します。

## インストール方法

リポジトリをクローンして、`make`してください。`~/bin`に`create-commit-link.py`がインストールされます。

~~~shell
$ git clone https://github.com/kantas-spike/create-commit-link.git
$ cd create-commit-link
$ make
~~~

## 使い方

使い方は以下になります。
引数に`コミットのハッシュ値`を指定し、`-r`オプションで、GitHubのユーザー名とリポジトリ名を指定します。

~~~shell
$ ~/bin/create-commit-link.py -h
usage: create-commit-link.py [-h] -r USER/REPO_NAME [-m] [-c] commit_hash [commit_hash ...]

GitHubのコミットへのURL(or リンク)を作成する

positional arguments:
  commit_hash           コミットのハッシュ値

options:
  -h, --help            show this help message and exit
  -r USER/REPO_NAME, --repository USER/REPO_NAME
                        GitHubのユーザー名とリポジトリ名 (形式: <GitHubのユーザー名>/<GitHubのリポジトリ名>)
  -m, --markdown-format
                        コミットのURLをマークダウンのリンク形式で出力する
  -c, --copy-to-clipboard
                        pbcopyを使って、出力結果をクリップボードにコピーする。
~~~

例えば、以下を実行すると、該当プロジェクトのコミットのURLを出力します。

~~~shell
$ ~/bin/create-commit-link.py "9d2e311c52b3359972dffe603964c1bdba3cba99" -r "kantas-spike/learn_react"
https://github.com/kantas-spike/learn_react/commit/9d2e311c52b3359972dffe603964c1bdba3cba99
~~~

また、`-m`オプションをつけると、ハッシュ値の先頭7文字をラベルにしたマークダウン形式のリンクを出力します。

~~~shell
$ ~/bin/create-commit-link.py "9d2e311c52b3359972dffe603964c1bdba3cba99" -r "kantas-spike/learn_react" -m
[9d2e311](https://github.com/kantas-spike/learn_react/commit/9d2e311c52b3359972dffe603964c1bdba3cba99)
~~~

さらに、`-c`オプションをつけると、出力したリンクをクリップボードにコピーします。

以下を実行後に、

~~~shell
$ ~/bin/create-commit-link.py "9d2e311c52b3359972dffe603964c1bdba3cba99" -r "kantas-spike/learn_react" -m -c
[9d2e311](https://github.com/kantas-spike/learn_react/commit/9d2e311c52b3359972dffe603964c1bdba3cba99)
~~~

テキストエディタを開いて、ペーストすると以下が貼りつけられます。

~~~text
[9d2e311](https://github.com/kantas-spike/learn_react/commit/9d2e311c52b3359972dffe603964c1bdba3cba99)
~~~

## 動作環境

以下の環境でのみ動作確認しました。

- Python 3.11.2
- macOS 13.4
  - pbcopyを使って、リンク出力をクリップボードにコピーしています。
