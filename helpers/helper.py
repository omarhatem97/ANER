from franco import franco_trans
import re
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


def is_ar(s):
    for ch in s:
        if ('\u0600' <= ch <= '\u06FF' or
                '\u0750' <= ch <= '\u077F' or
                '\u08A0' <= ch <= '\u08FF' or
                '\uFB50' <= ch <= '\uFDFF' or
                '\uFE70' <= ch <= '\uFEFF' or
                '\U00010E60' <= ch <= '\U00010E7F' or
                '\U0001EE00' <= ch <= '\U0001EEFF'):
            return True
    return False


def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')


def remove_r(s):
    l = s.split('\r')
    res = " ".join(l)
    return res


def remove_n(s):
    l = s.split('\n')
    res = " ".join(l)
    return res

def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


def prepare_sentence(s):

    temp = remove_n(s)
    temp = remove_r(temp)
    temp = remove_emoji(temp)
    l = temp.split(' ')

    print('list:')
    print(l)
    for i in range(0, len(l)):
        w = l[i]
        if(not is_ar(w)):
            print('word is: {}'.format(w))
            l[i] = franco_trans(w)
    res = " ".join(l)
    return res










if __name__ == '__main__':
    s = "alo alo el shi mnwawa ❤ gamed 🎉"
    text = remove_emoji(s)
    print('alo alo')
    print(text)
    print('done')


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





