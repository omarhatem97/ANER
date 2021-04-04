from franco import franco_trans
import emoji

def final_result (l):
    s = ''
    print('l is :')
    print (l)
    for t in l:
        print(t)
    return s

def is_english(s):
    for l in s:
        if((65 <= ord(l) <= 90) or (97 <= ord(l) <= 122)):
            return True
    return False

def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')


def remove_r(s):
    l = s.split('\r')
    return l

def remove_n(s):
    l = s.split('\n')
    res = " ".join(l)
    return res


def prepare_sentence(s):

    # temp = deEmojify(s)

    temp = remove_n(s)
    l = remove_r(temp)
    print ('list:')
    print(l)
    for i in range(0, len(l)):
        w = l[i]
        if(is_english(w)):
            l[i] = franco_trans(w)
    res = " ".join(l)
    return res



# def is_emoji(s):
#     count = 0
#     for emoji in UNICODE_EMOJI:
#         count += s.count(emoji)
#         if count > 1:
#             return False
#     return bool(count)


# def extract_emojis(s):
#     for c in s:
#         if( in emoji.UNICODE_EMOJI):
#             return True
#     return False
#   # return ''.join(c for c in s if c in emoji.UNICODE_EMOJI)





if __name__ == '__main__':
    print('doda')