# unpickling

import pickle


with open('malimg_data.pkl', 'rb') as f:
    data = pickle.load(f)

    print(data)

print('='*15)
print(data)


