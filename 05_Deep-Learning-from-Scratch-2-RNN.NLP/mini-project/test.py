import sys
sys.path.append('..')
import numpy as np
# from common.util import most_similar, create_co_matrix, ppmi
from common.util import preprocess, create_co_matrix, ppmi, most_similar

# python with 파일 읽기
# https://wikidocs.net/26

with open(r"C:\Users\Lee\Documents\steve-home\05_Deep-Learning-from-Scratch-2-RNN.NLP\dataset\kakao_chat.txt", "r", encoding='utf-8') as f:
    print(f.read())
