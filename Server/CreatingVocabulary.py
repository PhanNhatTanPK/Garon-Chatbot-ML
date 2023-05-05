word2count = {}

for line in clean_ques:
    for word in line.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1
            
for line in clean_ans:
    for word in line.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1
            
del(word, line)


# Thực hiện việc tạo từ điển (vocab) cho các từ xuất hiện trong dataset với giới hạn tần suất tối thiểu là 5
thresh = 5
vocab = {}
word_num = 0
for word, count in word2count.items():
    if count >= thresh:
        vocab[word] = word_num
        word_num += 1
        
## delete
del(word2count, word, count, thresh,word_num)

for i in range(len(clean_ans)):
    clean_ans[i] = '<SOS> ' + clean_ans[i] + ' <EOS>'
    
tokens = ['<PAD>', '<EOS>', '<OUT>', '<SOS>']
x = len(vocab)

for token in tokens:
    vocab[token] = x
    x += 1
    
vocab['cameron'] = vocab['<PAD>']
vocab['<PAD>'] = 0

del(x,token, tokens) 

# Inverse Answers Dictionary 
inv_vocab = {w:v for v, w in vocab.items()}
del(i)