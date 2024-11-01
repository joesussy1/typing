import time
from print_color import colored

print(colored("Typing Test", "BLUE"))
prompt = "The quick brown fox jumps over the lazy dog"
print(prompt)
start = time.time()
user_input = input()
end = time.time()

result_string = ""
correct_words = 0
input_word_list = user_input.split(" ")
prompt_word_list = prompt.split(" ")
for i in range(len(input_word_list)):
    letters_correct = 0
    for k in range(len(input_word_list[i])):
        if(input_word_list[i][k] == prompt_word_list[i][k]):
            letters_correct += 1
            result_string += colored(input_word_list[i][k], "GREEN")
        else:
            result_string += colored(input_word_list[i][k], "RED")
    result_string += " "
    if letters_correct == len(input_word_list[i]):
        correct_words += 1

print(f"Time elapsed: {end - start}")
print(result_string)
print(correct_words)