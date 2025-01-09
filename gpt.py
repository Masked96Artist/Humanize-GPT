import random
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('punkt')

def synonym_replacement(word):
    synonyms = wordnet.synsets(word)
    if not synonyms:
        return word
    synonym = random.choice(synonyms).lemmas()[0].name()
    return synonym.replace('_', ' ')

def humanize_sentence(sentence):
    words = nltk.word_tokenize(sentence)
    paraphrased_words = []

    for word in words:
        if word.isalpha() and random.random() > 0.7:
            paraphrased_words.append(synonym_replacement(word))
        else:
            paraphrased_words.append(word)
    
    paraphrased_text = ' '.join(paraphrased_words)
    return paraphrased_text

def humanize_report(text):
    lines = text.splitlines()  
    humanized_lines = []

    for line in lines:
        if line.strip():  
            humanized_line = humanize_sentence(line)
        else:
            humanized_line = line  
        humanized_lines.append(humanized_line)

    return '\n'.join(humanized_lines)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_report(input_file, output_file):
    report_content = read_file(input_file)
    
    humanized_content = humanize_report(report_content)
    
    write_file(output_file, humanized_content)

input_file = '/filelocation/report.txt'  
output_file = '/filelocation/humanized_report.txt'  

process_report(input_file, output_file)
