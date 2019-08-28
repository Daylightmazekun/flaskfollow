import sys
sys.path.append("..")
from model.models import Words, Grammer

def read_markdown(kodoba_path):
    f = open(kodoba_path, 'r',encoding='UTF-8')
    for line in f.readlines():
        # word = line[0:line.find('|')].strip()
        wordlist = line.split('|', 3)
        list_length = len(wordlist)
        if list_length >= 3:
            if wordlist[0].strip() == '-' or wordlist[0].strip() =='日本語':
                continue
            word_check_exist = Word.objects(word=wordlist[0].strip().strip('\n'))
            if word_check_exist is not None:
                word = Words(word=wordlist[0].strip().strip('\n'),hiragana = wordlist[1].strip().strip('\n'),honnyaku = wordlist[2].strip().strip('\n'))
            else: 
                continue
            
       # elif list_length == 1:
       #     print(wordlist)
        elif 3 > list_length >= 2:
            if wordlist[0].strip() == '-' or wordlist[0].strip() == '日本語':
                continue
            word_check_exist = Word.objects(word=wordlist[0].strip().strip('\n'))
            if word_check_exist is not None:
                word = Words(word=wordlist[0].strip().strip('\n'),hiragana = wordlist[1].strip().strip('\n'))
            else:
                continue
        else:
            continue
        word.save()
 
    f.close()
def read_grammer(grammer_path):
    f = open(grammer_path, 'r', encoding='UTF-8')
    grammer = Grammer()
    grammer_example = ''
    grammer_str = ''
    mark = 0
    for line in f.readlines():
        if line.strip().startswith('*'):
            if mark != 0 :
                grammer.grammer = grammer_str
                grammer.exaple = grammer_example
                grammer.save()
                grammer_str, grammer_example = '', ''
            grammer_str = line.strip().strip('*')
            mark += 1
        if line.strip().startswith('>'):
            grammer_example = grammer_example + line.strip().strip('>') + '\n'
    grammer.save()
    f.close()
if __name__ == '__main__':
    # read_markdown('n2言葉.md')
    read_grammer('n2文法.md')