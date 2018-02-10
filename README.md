# このリポジトリについて
PythonのPillowというライブラリでモザイクアートを作ります。

モザイクアートの作成ロジックは以下のLTスライドも合わせてご確認ください。

https://speakerdeck.com/ftnext/pillow-mosaic-art-nyumon

# 開発環境
* Python 3.6.3
* Python 3.5.1

2台の端末で開発を進めています。
2018/01/16時点で、Python3.6系では動くが、3.5系では動かないという事象は発生していません。

# 動作させるまで
* このリポジトリをクローン
* 必要なモジュールをpip install
  * `pip install pillow` (必須)
  * `pip install numpy matplotlib jupyter` (notebookで動かす際に使う)

# フォルダ構成
* ┣ env/ :仮想環境
* ┣ image/ :素材画像の元画像
* ┣ material/ :素材画像の縮小画像
* ┣ mosaic_art/ :モザイクアート作成用自作モジュール
* ┣ product/ :作成後のモザイクアートが置かれる

* ┣ README.md
* ┣ my_icon.png :モザイクアート対象画像

  前処理で使うファイル
* ┣ calculate_material_color.py
* ┣ thumbnail_image.py

  前処理で作成されるファイル (3つは.gitignoreに記載)
* ┣ average_color.csv
* ┣ median_color.csv
* ┣ mode_color.csv

  モザイクアート作成に使うファイル
* ┣ mosaic_art.py
* ┣ mosaic_art_median.py
* ┣ mosaic_art_mode.py

  Jupyter notebook
* ┣ mosaic_art.ipynb
* ┗ dot_picture.py :notebookで使っているメソッドの元

# 注意点
* 対象画像は `my_icon.png` という名前で配置してください。
* 素材画像は`image/`フォルダの下に`euph_part_icon`というフォルダを作ってその中に配置してください。
* 前処理で`python thumbnail_image.py`を実行する前に、`material/`フォルダの下に`euph_part_icon`というフォルダを作ってください。
* 対象画像、素材画像ともに 400×400 のサイズでしか正常に動作しないと思われます。
* できあがるモザイクアートのサイズは 1600×1600 になります。対象画像を 10×10 の領域に分割し、各領域に 40×40 のサイズの素材画像のうち一番色が近いものを対応させています。

パスの決め打ち問題や、一定のサイズにしか対応できない点は実装不足なので、今後ソースコードを更新していく。

# 前処理
1. image/フォルダ以下に素材画像を配置する
1. 素材画像の縮小画像を用意する: `python thumbnail_image.py` (実行後、material/フォルダ以下に縮小画像ができる)
1. 素材画像を代表させる色の情報を用意する（実行後、csvファイルができる。このcsvファイルの色情報をモザイクアート作成時に参照する）
* 色の平均値で素材画像を代表させる場合: `python calculate_material_color.py average` → average_color.csvが作成される
* 色の中央値で素材画像を代表させる場合: `python calculate_material_color.py median` → median_color.csvが作成される
* 色の最頻値で素材画像を代表させる場合: `python calculate_material_color.py mode` → mode_color.csvが作成される

# モザイクアート作成
対象画像を my_icon.png として配置する。

モザイクアート作成時、以下の2点を指定している。
* 対象画像を格子状に分割した領域をどのような色で代表させるか (平均値／中央値／最頻値)
* 素材画像をどのような色で代表させるか (平均値／中央値／最頻値)

後者は average_color.csv, median_color.csv, mode_color.csvのうちどれを使うかということ。

色の代表のさせ方については以下の組合せを提供している。
* 平均値×平均値: 対象画像の領域の色を *平均値* で代表させ、素材画像の色を *平均値* で代表させる: `python mosaic_art.py`
* 中央値×中央値: 対象画像の領域の色を *中央値* で代表させ、素材画像の色を *中央値* で代表させる: `python mosaic_art_median.py`
* 最頻値×最頻値: 対象画像の領域の色を *最頻値* で代表させ、素材画像の色を *最頻値* で代表させる: `python mosaic_art_mode.py`

以上3つのコマンドのいずれかを実行すると、product/フォルダにモザイクアートにした画像ができる。
* `python mosaic_art.py` → product/my_icon_mosaic.png
* `python mosaic_art_median.py` → product/my_icon_mosaic_median.png
* `python mosaic_art_mode.py` → product/my_icon_mosaic_mode.png

READMEを書いている時点では **平均値×平均値** の組合せを推奨する。
