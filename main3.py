#*-------------- 標準入力 --------------*#

#　標準入力で与えたものは文字列型!

# example >>> 2 (なんでもいい)
n = input()      #　標準入力から受け取る(str型)
print(type(n))   # <class 'str'>
print(n)         # 標準入力で与えたもの

# example >>> 3 (int型)
n = int(input()) #　標準入力から受け取った文字列型を整数型になおす
print(type(n))   # <class 'int'>
print(n * 2)     # 標準入力で与えた値(int型)の2倍

# example >>> 2 5 (int型)
a,b = map(int,input().split()) # 標準入力から空白区切りで値を受け取って(str型)整数型に直す(int型)
print(a + b)     # 空白区切りで受け取った値を足す(数値同様に演算可能)

# example >>> 2 3 4 5 2 4
a = list(map(int,input().split())) # 標準入力から空白区切りで値を受け取って、int型に直して、リストに格納する
print(type(a)) # <class 'list'>
print(a) # [2, 3, 4, 5, 2, 4] リストが出力される

# example >>> 2 3 4 5 2 4
a = list(map(float,input().split())) # 標準入力から空白区切りで値を受け取って、float型に直して、リストに格納する
print(type(a)) # <class 'list'>
print(a) # [2.0, 3.0, 4.0, 5.0, 2.0, 4.0] リストが出力される

# example >>> 2 3 4 5 2 4
a = list(map(str,input().split())) # 標準入力から空白区切りで値を受け取って(str型)リストに格納する
print(type(a)) # <class 'list'>
print(a) # ['2', '3', '4', '5', '2', '4'] リストが出力される

#*-------------- 標準入力 --------------*#
