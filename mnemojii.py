import emoji
import mnemonic
import random
import os
import json

def mnemojii(emoji_mapping):    
    
    mnemojii_found = False
    emoji_words = list(emoji_mapping.keys())
    random.shuffle(emoji_words)
    while mnemojii_found != True:
        random_words = random.choices(emoji_words, k=11)
        partial_mnemonic = ' '.join(random_words)      
        m = mnemonic.Mnemonic('english') 
        for word in emoji_words:
            full_mnemonic = partial_mnemonic + ' ' + word
            if m.check(full_mnemonic):
                mnemojii_found = True
                break
                
    for word in full_mnemonic.split(' '):
        print(emoji.emojize(':{}:'.format(emoji_mapping[word])), end =" ")
    print("\n")


if __name__ == '__main__':
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_object = open(os.path.join(__location__, 'emojiimapping.json'))
    emoji_mapping = json.load(file_object)
    mnemojii(emoji_mapping)
