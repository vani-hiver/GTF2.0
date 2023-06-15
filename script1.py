def get_input(word):
 
    if len(word)<=1:
        return set(word)
 
    input = get_input(word[1:-1])
    output = list()
    for item in input:
        for i in range(0,len(item)):
            out = item[:i+1] + word[0] + item[i+1:]
            if out not in output:
                output.append(out)
    return output
