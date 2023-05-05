# Chuẩn bị dữ liệu đầu vào cho encoder
encoder_inp = []
for line in clean_ques:
    lst = []
    for word in line.split():
        if word not in vocab:
            lst.append(vocab['<OUT>'])
        else:
            lst.append(vocab[word])
        
    encoder_inp.append(lst)

# Chuẩn bị dữ liệu đầu vào cho decoder
decoder_inp = []
for line in clean_ans:
    lst = []
    for word in line.split():
        if word not in vocab:
            lst.append(vocab['<OUT>'])
        else:
            lst.append(vocab[word])        
    decoder_inp.append(lst)

del(clean_ans, clean_ques, line, lst, word)

# Padding các đầu vào cho mô hình LSTM
from tensorflow.keras.preprocessing.sequence import pad_sequences

encoder_inp = pad_sequences(encoder_inp, 13, padding='post', truncating='post')
decoder_inp = pad_sequences(decoder_inp, 13, padding='post', truncating='post')
decoder_final_output = []

for i in decoder_inp:
    decoder_final_output.append(i[1:]) 
decoder_final_output = pad_sequences(decoder_final_output, 13, padding='post', truncating='post')
del(i)

# Mã hóa nhãn sử dụng one-hot encoding
decoder_final_output = to_categorical(decoder_final_output, len(vocab))
print(decoder_final_output.shape)
decoder_final_output[0]