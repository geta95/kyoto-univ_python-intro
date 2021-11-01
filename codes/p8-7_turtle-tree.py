from turtle import *

# 再帰的に木を描く
def tree(n):
    # 引数が1以下なら5歩すすむ
    if n <= 1:
        forward(5)
    else:
        # 引数は1 より大きいとき
        # 引数の値に応じて前進(幹)
        forward(5*(1.3**n))
        # 今の位置と向きを記録
        xx = pos()
        h = heading()
        # 左へ30度回転
        left(30)
        # 大きさn-2で木を描く(左の枝)
        tree(n-2)
        # ペンを挙げて軌跡を残さない
        up()
        # 先に記録した位置(幹の先端)に戻る
        setpos(xx)
        setheading(h)
        # ペンを降ろす
        down()
        # 右へ15 度
        right(30)
        # 大きさn-1で木を描く(右の枝)
        tree(n-1)
        # ペンを上げてもどる
        up()
        setpos(xx)
        setheading(h)
        # ペンを降ろす
        down()
# 時間がかかるので最も早い描画
speed(0)
# 大きさ12␣の木を描く
tree(11)
