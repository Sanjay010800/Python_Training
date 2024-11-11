def remove_vowels(str):
    result=''
    for c in str:
        if c not in 'aeiouAEIOU':
            result+=c

    print(result)


remove_vowels('Sanjay')