########################
# INI1
########################
# import this

########################
# INI2
########################
# a = 957
# b = 896
# print(a ** 2 + b ** 2)

########################
# INI3
########################
# content = "E3Wk1Ch23fWnYIpE8pk2plMEW2CHpJuVLimnodromusNZgH9AFwaNgobio76gKHpuZwMLAprJiGzSviKnVxP2Oy7CZzU7EZwoSDtmGt8aUSeubc3D8Kkphbpg1znJSgKnnB9tP4AfPzbx5cl6W47NNTJyLUhHT4MRZ0IvAbIxDzyrHv."
# a = 32
# b = 42
# c = 53
# d = 57
# print(content[a:b+1] + " " + content[c:d+1])

########################
# INI4
########################
# a = 4066
# b = 8877
# result = 0
# for i in range(a, b+1):
#     if i % 2 != 0:
#         result += i
# print(result)

########################
# INI5
########################
# new_file = []
# number = 0
#
# file_input = open('input.txt', 'r')
# for line in file_input:
#     if number % 2 != 0:
#         new_file.append(line)
#     number += 1
# print(new_file)
#
# file_output = open('output.txt', 'w')
# for line in new_file:
#     file_output.write(str(line))

########################
# INI6
########################
text = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

wordCount = {}

for word in text.split(" "):
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

for key, value in wordCount.items():
    print(key, value)
