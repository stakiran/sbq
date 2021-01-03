# sbq
Command-line Scrapbox Exported JSON processor.

## usage

### property a page with title
With `title` subcommand:

```
sbq -i (YOUR-JSON).json title "(PAGE-NAME)" (METHOD-NAME)
```

Example:

```
$ sbq -i sta.json title "teeting" url
https://scrapbox.io/sta/teeting

$ sbq -i sta.json title "teeting" id
5ea368573cf2cf00178a819f

$ sbq -i sta.json title "teeting" rawstring
teeting
 テキストミーティング
  text + meeting = teeting
  [sta.icon]啓蒙したい場合は「筆談会議」のがわかりやすいかもしれない
 teeting が行えるツールの要件
  [同時編集]ができること
  シームレスなリプライ構造を備えていること
   ≒ 箇条書き
  自動保存されること
 [teetingが行えるツール]
  [sta.icon]上記はいずれも[箇条書き同時編集]がしやすいもの
   将来的には箇条書き以外の同時編集もあるかもしれない
    お絵かきチャットというジャンルが既にある
   そもそも「同時編集」以外の、全く新しい概念も誕生するかもしれない
 teeting のメリット
  [/shokai/ターン制コミュニケーション] の弊害を解消できる
   弊害
    半二重通信による非効率
    話題の記憶がしんどい etc
  [マルチトーキング]ができる（ので生産的で高濃度な議論ができる）
 [teetingのやり方]
 [teetingのコツ]
 [teetingのテンプレート]
```
