original_str = "The quick brown rhino jumped over the extremely lazy fox"
str_list = original_str.split(" ")
num_words_list = []

for word in str_list:
   num_words_list.append(len(word))

print(num_words_list)


