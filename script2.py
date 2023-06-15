def get_url(word_list):
    result = ""
    for i in range(0, len(word_list)):
        result = result + word_list[i][i % len(word_list[i]):]
    print(result, len(result))
    if len(result) != 12:
        print('Please enter correct list!')
    else:
        print(f"https://rumblebee4.github.io/{result}")
