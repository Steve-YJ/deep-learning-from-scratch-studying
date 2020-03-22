import sys
sys.path.append('..')
import numpy as np
# from common.util import most_similar, create_co_matrix, ppmi
from common.util import preprocess_mini, create_co_matrix, ppmi, most_similar

# python with 파일 읽기
# https://wikidocs.net/26


# Q1. 기존에 사용했었던 preprocess()함수를 사용해서 전처리를 할 수 있을까? 각이 안나오는데?? -20.03.22-
# 채팅 내용을 한 줄씩 받아온다?
# 자료형을 list로 받어서 append하는 방법? => 알고리즘을 조금 변경해야겠군!

# text = np.array([])
# with open(r"C:\Users\Lee\Documents\steve-home\05_Deep-Learning-from-Scratch-2-RNN.NLP\dataset\kakao_chat.txt", "r", encoding='utf-8') as f:
#     np.append(text, f.readline())

with open(r"C:\Users\Lee\Documents\steve-home\05_Deep-Learning-from-Scratch-2-RNN.NLP\dataset\kakao_chat.txt", "r", encoding='utf-8') as f:
    line = f.readline()
    text = line
    corpus, word_to_id, id_to_word = preprocess_mini(text)
    
    

with open(r"C:\Users\Lee\Documents\steve)

for line in text:
    line.reshape(1, len())

corpus, word_to_id, id_to_word = preprocess_mini(text)
print(corpus)
print(len(word_to_id))


window_size = 2
wordvec_size = 100

corpus, word_to_id, id_to_word = ptb.load_data('train')
vocab_size = len(word_to_id)
print('동시발생 수 계산 ...')
C = create_co_matrix(corpus, vocab_size, window_size)
print('PPMI 계산 ...')
W = ppmi(C, verbose=True)

print('SVD 계산 ...')
try:
    # truncated SVD(빠르다!)
    from sklearn.utis.extmath import randomized_svd
    U, S, V = randomized_svd(W, n_components=wordvec_size, n_iter=5, random_state=None)

except ImportError:
    # SVD(느리다)
    U, S, V = np.linalg.svd(W)

word_vecs = U[:, :wordvec_size]

querys = ['you', 'year', 'car', 'toyota']
for query in querys:
    most_similar(query, word_to_id, id_to_word, word_vecs, top=5)