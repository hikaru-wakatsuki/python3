*This project has been created as part of the 42 curriculum by hwakatsu.*

# Data Quest

## Description / 説明

### English
Data Quest is a Python project focused on mastering collection types for data-engineering style tasks. Its goal is to demonstrate how lists, tuples, sets, dictionaries, generators, and comprehensions can be used to process, transform, and analyze in-memory game-related data.

This repository contains seven exercises:

- `ex0/ft_command_quest.py`: command-line argument handling with `sys.argv`
- `ex1/ft_score_analytics.py`: list-based score analytics from command-line inputs
- `ex2/ft_coordinate_system.py`: tuple-based 3D coordinate parsing and distance calculation
- `ex3/ft_achievement_tracker.py`: set-based achievement analytics
- `ex4/ft_inventory_system.py`: dictionary-based inventory processing
- `ex5/ft_data_stream.py`: generator-based streaming and analytics
- `ex6/ft_analytics_dashboard.py`: list, dict, and set comprehensions for analytics summaries

From the code in this repository, the project demonstrates:

- basic and practical command-line data intake
- sequential score processing with lists
- fixed-position coordinate handling with tuples
- deduplication and comparison with sets
- keyed storage and nested categorization with dictionaries
- memory-efficient streaming with generators
- concise transformations with comprehensions

### 日本語
Data Quest は、データエンジニアリング風の課題を通して Python の collection 型を学ぶプロジェクトです。目的は、lists、tuples、sets、dictionaries、generators、comprehensions を使って、メモリ上のゲーム関連データを処理・変換・分析する方法を示すことです。

このリポジトリには 7 つの exercise があります。

- `ex0/ft_command_quest.py`: `sys.argv` を使ったコマンドライン引数処理
- `ex1/ft_score_analytics.py`: コマンドライン入力をもとにした list ベースのスコア分析
- `ex2/ft_coordinate_system.py`: tuple を使った 3D 座標解析と距離計算
- `ex3/ft_achievement_tracker.py`: set を使った実績データ分析
- `ex4/ft_inventory_system.py`: dictionary を使ったインベントリ処理
- `ex5/ft_data_stream.py`: generator を使ったストリーム処理と分析
- `ex6/ft_analytics_dashboard.py`: list / dict / set comprehension を使った分析表示

このリポジトリの実装では、次の内容が確認できます。

- 実用的なコマンドラインデータ入力
- list を使った順序付きスコア処理
- tuple を使った固定位置データの扱い
- set による重複排除と集合比較
- dictionary によるキー付きデータ保持とカテゴリ分け
- generator によるメモリ効率の良いストリーム処理
- comprehension による簡潔なデータ変換

## Instructions / 実行方法

### English

Requirements:

- Python 3.10 or later
- No external dependencies

Run each exercise from the repository root:

```bash
python3 ex0/ft_command_quest.py
python3 ex1/ft_score_analytics.py 1500 2300 1800 2100 1950
python3 ex2/ft_coordinate_system.py
python3 ex3/ft_achievement_tracker.py
python3 ex4/ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1
python3 ex5/ft_data_stream.py
python3 ex6/ft_analytics_dashboard.py
```

Optional lint check:

```bash
flake8 ex0 ex1 ex2 ex3 ex4 ex5 ex6
```

There is no compilation or installation step. All exercises use only the Python standard library and in-memory data, except for command-line arguments where required.

### 日本語

必要環境:

- Python 3.10 以上
- 外部依存関係なし

リポジトリのルートで、各 exercise は次のように実行できます。

```bash
python3 ex0/ft_command_quest.py
python3 ex1/ft_score_analytics.py 1500 2300 1800 2100 1950
python3 ex2/ft_coordinate_system.py
python3 ex3/ft_achievement_tracker.py
python3 ex4/ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1
python3 ex5/ft_data_stream.py
python3 ex6/ft_analytics_dashboard.py
```

任意の lint チェック:

```bash
flake8 ex0 ex1 ex2 ex3 ex4 ex5 ex6
```

コンパイルやインストールは不要です。すべての exercise は Python 標準ライブラリとメモリ上のデータのみを使い、必要に応じてコマンドライン引数を利用します。

## Features / 主な内容

### English

- Command-line parsing with `sys.argv`
- Score statistics with list accumulation and numeric aggregation
- Tuple parsing, unpacking, and 3D Euclidean distance calculation
- Set operations such as intersection, union, and difference
- Dictionary-based inventory aggregation and categorization
- Generators for event streaming, Fibonacci numbers, and prime numbers
- List, dict, and set comprehensions for compact analytics transformations

### 日本語

- `sys.argv` を使ったコマンドライン解析
- list 集約と数値集計によるスコア統計
- tuple の解析、アンパック、3D ユークリッド距離計算
- intersection、union、difference などの set 操作
- dictionary による在庫集計とカテゴリ分け
- イベントストリーム、フィボナッチ数列、素数列に対する generator
- list / dict / set comprehension による簡潔な分析変換

## Usage Overview / 使い方の概要

### English

- `ex0` and `ex1` focus on command-line data input.
- `ex2` through `ex4` focus on choosing the right collection type for the data model.
- `ex5` focuses on lazy evaluation and streaming.
- `ex6` combines previous ideas into a compact analytics-style summary.

### 日本語

- `ex0` と `ex1` はコマンドライン入力データの扱いに焦点があります。
- `ex2` から `ex4` は、データモデルに合った collection 型の選択に焦点があります。
- `ex5` は遅延評価とストリーミング処理に焦点があります。
- `ex6` はそれまでの考え方をまとめた簡潔な分析表示を示します。

## Resources / 参考資料

### English

Classic references related to the topic:

- [Python Documentation: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Documentation: Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Python Documentation: Generator Functions](https://docs.python.org/3/reference/expressions.html#generator-iterator-methods)
- [Python Documentation: Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Python Documentation: sys.argv](https://docs.python.org/3/library/sys.html#sys.argv)
- [Real Python: Python Comprehensions](https://realpython.com/list-comprehension-python/)
- [Real Python: Introduction to Python Generators](https://realpython.com/introduction-to-python-generators/)
- [flake8 Documentation](https://flake8.pycqa.org/)

AI usage in this project:

- AI was used for documentation support and README drafting.
- It was used to inspect the repository structure, summarize the purpose of each exercise, and provide bilingual English/Japanese wording.
- The README was written to match the existing code in `ex0` through `ex6`, but the implementation details and command-line behavior should still be checked manually before submission and peer review.

### 日本語

この課題に関連する代表的な参考資料:

- [Python Documentation: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Documentation: Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Python Documentation: Generator Functions](https://docs.python.org/3/reference/expressions.html#generator-iterator-methods)
- [Python Documentation: Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Python Documentation: sys.argv](https://docs.python.org/3/library/sys.html#sys.argv)
- [Real Python: Python Comprehensions](https://realpython.com/list-comprehension-python/)
- [Real Python: Introduction to Python Generators](https://realpython.com/introduction-to-python-generators/)
- [flake8 Documentation](https://flake8.pycqa.org/)

このプロジェクトにおける AI の利用:

- AI はドキュメント補助と README 作成支援に使用しました。
- リポジトリ構造の確認、各 exercise の目的整理、英語と日本語の文章作成に利用しました。

## Notes / 補足

### English
This project is intentionally centered on collection mastery rather than large application architecture. The important part is demonstrating when each collection type is the right tool for the job.

### 日本語
このプロジェクトは大規模アプリケーション設計よりも collection の使い分け習得を重視しています。重要なのは、どの collection 型がどの場面に適しているかを示すことです。
