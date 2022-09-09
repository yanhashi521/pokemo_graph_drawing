import json
import networkx as nx
import matplotlib.pyplot as plt
from scipy.sparse.csgraph import floyd_warshall
from networkx.readwrite import json_graph
import math
import random

filename = open('./resources/Season31_Single_master.json','r')
graph = json.load(filename)

data = ["888","145","645","898","132","248","382","598","233","717"]
#data = ["ザシアン","サンダー","ランドロス","黒馬パドレックス","メタモン","バンギラス","カイオーガ","ナットレイ","ポリゴン２","イベルタル"]
#data = [888,145,645,898,132,248,382,598,233,717]


top = {}

#for i in range(10):
#  top[data[i]] = graph[data[i]]["0"]["temoti"]["pokemon"] 

#top

for i in range(10):
  if i == "145":#サンダー
    top[data[i]] = graph[data[i]]["0"]["temoti"]["pokemon"]
  elif i == "645":#ランドロス
    top[data[i]] = graph[data[i]]["1"]["temoti"]["pokemon"]
  elif i == "898":#黒馬
    top[data[i]] = graph[data[i]]["2"]["temoti"]["pokemon"]
  else:
    top[data[i]] = graph[data[i]]["0"]["temoti"]["pokemon"]

#print(top)

for poke in top:
    print(poke)