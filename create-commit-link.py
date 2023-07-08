#!/usr/bin/env python3

import argparse

URL_PREFIX = "https://github.com"
PBCOPY_COMMAND = "/usr/bin/pbcopy"


def create_list_of_url_or_link(args):
    results = []
    for h in args.commit_hash:
        url = f"{URL_PREFIX}/{args.repository}/commit/{h}"
        if args.markdown_format:
            short_hash = h[0:7]
            results.append(f"[{short_hash}]({url})")
        else:
            results.append(url)

    return results


def write_to_clipbaord(output):
    import subprocess
    process = subprocess.Popen(PBCOPY_COMMAND, stdin=subprocess.PIPE)
    process.communicate(output.encode())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GitHubのコミットへのURL(or リンク)を作成する")
    parser.add_argument("commit_hash", help="コミットのハッシュ値", nargs='+')
    parser.add_argument("-r", "--repository", metavar="USER/REPO_NAME", required=True,
                        help="GitHubのユーザー名とリポジトリ名 (形式: <GitHubのユーザー名>/<GitHubのリポジトリ名>)")
    parser.add_argument("-m", "--markdown-format", action='store_true', help="コミットのURLをマークダウンのリンク形式で出力する")
    parser.add_argument("-c", "--copy-to-clipboard", action='store_true', help="pbcopyを使って、出力結果をクリップボードにコピーする。")
    args = parser.parse_args()
    # print(args)

    list = create_list_of_url_or_link(args)
    output = "\n".join(list)
    print(output)
    if args.copy_to_clipboard:
        write_to_clipbaord(output)
        print("   copied to clipboard!")
