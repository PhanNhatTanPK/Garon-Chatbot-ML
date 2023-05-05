def clean_text(txt):
    txt = txt.lower()
    txt = re.sub(r"i'm", "i am", txt)
    txt = re.sub(r"he's", "he is", txt)
    txt = re.sub(r"she's", "she is", txt)
    txt = re.sub(r"that's", "that is", txt)
    txt = re.sub(r"what's", "what is", txt)
    txt = re.sub(r"where's", "where is", txt)
    txt = re.sub(r"\'ll", " will", txt)
    txt = re.sub(r"\'ve", " have", txt)
    txt = re.sub(r"\'re", " are", txt)
    txt = re.sub(r"\'d", " would", txt)
    txt = re.sub(r"won't", "will not", txt)
    txt = re.sub(r"can't", "can not", txt)
    txt = re.sub(r"[^\w\s]", "", txt)
    return txt

clean_ques = []
clean_ans = []

# Làm sạch dữ liệu câu hỏi
for line in sorted_ques:
    clean_ques.append(clean_text(line))

# Làm sạch dữ liệu câu trả lời  
for line in sorted_ans:
    clean_ans.append(clean_text(line))

# Thực hiện việc giới hạn độ dài của câu trả lời trong tối đa 13 từ
for i in range(len(clean_ans)):
    clean_ans[i] = ' '.join(clean_ans[i].split()[:13])

del(answers, questions, line,sorted_ans, sorted_ques)


# trimming
clean_ans=clean_ans[:35000]
clean_ques=clean_ques[:35000]
