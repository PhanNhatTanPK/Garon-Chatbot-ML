# Load dữ liệu
lines = open('/content/drive/MyDrive/movie_lines.txt', encoding='utf-8',
             errors='ignore').read().split('\n')

convers = open('/content/drive/MyDrive/movie_conversations.txt', encoding='utf-8',
             errors='ignore').read().split('\n')

# Tiền xử lý dữ liệu

# Tạo danh sách "exchn" bằng cách duyệt qua từng cuộc trò chuyện trong tập dữ liệu đầu vào "convers"
exchn = []
for conver in convers:
    exchn.append(conver.split(' +++$+++ ')[-1][1:-1].replace("'", " ").replace(",","").split())

# Tạo từ điển "diag" bằng cách duyệt qua từng câu trong tập dữ liệu đầu vào "lines"
diag = {}
for line in lines:
    diag[line.split(' +++$+++ ')[0]] = line.split(' +++$+++ ')[-1]

# delete
del(lines, convers, conver, line)