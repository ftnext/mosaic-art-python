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

# フォルダ構成 ※作成中
┣ env/ :仮想環境
┣ image/ :素材画像の元画像
┣ material/ :素材画像の縮小画像
┣ mosaic_art/ :モザイクアート作成用自作モジュール
┣ product/ :作成後のモザイクアートが置かれる

┣ README.md
┣ my_icon.png :モザイクアート対象画像

  前処理で使うファイル
┣ calculate_average_color.py
┣ calculate_median_color.py
┣ calculate_mode_color.py
┣ thumbnail_image.py

  前処理で作成されるファイル (3つは.gitignoreに記載)
┣ average_color.csv
┣ median_color.csv
┣ mode_color.csv

  モザイクアート作成に使うファイル
┣ mosaic_art.py
┣ mosaic_art_median.py
┣ mosaic_art_mode.py

  Jupyter notebook
┣ mosaic_art.ipynb
┗ dot_picture.py :notebookで使っているメソッドの元

# 前処理
# モザイクアート作成
# 注意点
