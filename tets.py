"""This Guy is missing"""
#import String

class Text():
    '''Missing'''

    def __init__():
        '''Missing'''
        pass

    def statistic():
        '''Missing'''
        count_words = [",", ".", "?", "!", "(", ")", "=", "%", "_", "-"]
        f = open('Morgen_Kinder.txt', 'r')
        text_save = f.read()

        for i in range(len(count_words)+1):
            text_save = text_save.split(count_words[i])

        print(text_save)
        
if __name__ == "__main__":
    Text.statistic()
