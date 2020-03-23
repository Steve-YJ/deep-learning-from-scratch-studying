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

word_to_id = {}  # dictionary type
id_to_word = {}
# corpora = np.array([1, 2, 3])
# corpora = corpora.reshape(1, -1)
with open(r"C:\Users\stevelee\Documents\deep-learning-from-scratch-studying\05_Deep-Learning-from-Scratch-2-RNN.NLP\dataset\kakao_chat.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        text = line
        text = text.lower()
        text = text.replace('.', ' .')
        words = text.split(' ')  # words: data type is list
        words = words[2:]

        for word in words:
            if word not in word_to_id:
                new_id = len(word_to_id)  # 새로운 단어의 경우, dic에 새로운번호로 추가되겠죠? 
                                        # 새로운 단어는 새로운 인덱스번호로 dic에 추가된다.
                word_to_id[word] = new_id
                id_to_word[new_id] = word

        # corpus = np.array([word_to_id[w] for w in words])
        # corpus = corpus.reshape(1, -1)
        # np.append(corpora, corpus, axis=1)

    # corpus = np.array([word_to_id[w] for w in word_to_id])
corpus = np.array([word_to_id[w] for w in word_to_id])

'''
지금 line을 하나밖에 읽지 않았구나...
loop를 돌려 전체 텍스트를 읽어와야지...!
'''
# print(word_to_id)
# print(id_to_word)
print('corpus: ', corpus)  
# print('word_to_id: ', word_to_id)
# print('id_to_word: ', id_to_word)

window_size = 2
wordvec_size = 100

vocab_size = len(word_to_id)
print('동시발생 수 계산 ...')
C = create_co_matrix(corpus, vocab_size, window_size)
print('동시 발생 행렬: ', C)


print('PPMI 계산 ...')
W = ppmi(C, verbose=True)
print('PPMI: ', W)
# >>> PPMI까지 제대로 출력되는 것을 확인. 그렇다면 뒤에서 문제가 발생한다는 의미인데... -20.03.23.mon-

print('SVD 계산 ...')
try:
    # truncated SVD(빠르다!)
    from sklearn.utils.extmath import randomized_svd
    U, S, V = randomized_svd(W, n_components=wordvec_size, n_iter=5, random_state=None)

except ImportError:
    # SVD(느리다)
    U, S, V = np.linalg.svd(W)

word_vecs = U[:, :wordvec_size]

querys = ['아기', '공주', '영둥', '빵둥']
for query in querys:
    most_similar(query, word_to_id, id_to_word, word_vecs, top=5)


querys = ['아기공주', '영둥이', '뽕아기', '예뽕아기']
for query in querys:
    most_similar(query, word_to_id, id_to_word, word_vecs, top=5)


querys = ['아기둥이', '이영둥', '뽕아기', '예뽕아기']
for query in querys:
    most_similar(query, word_to_id, id_to_word, word_vecs, top=5)
    