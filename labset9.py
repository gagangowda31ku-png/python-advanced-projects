# labset 9

'''Text Analysis Tool: Build a tool that analyses a paragraph: 
frequency of each word, longest word, number of sentences, etc. '''

import string
def analyze_text(paragraph):
    text = paragraph.lower()
    sentance_count = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')

    for ch in string.punctuation:
        text = text.replace(ch,"")
        words = text.split()

    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    
    longest_word = max(words ,key= len) if words else ""
    total_words = len(words)
    print("--- Text Analyzor-----")
    print(f"Total Words :{total_words}")
    print(f"Sentance Count: {sentance_count}")
    print(f"Longest Word: {longest_word}")

    print("----- Word Frequqncy------")
    for key,value in freq.items():
        print(f"{key} - {value}")

paragraph = "python is easy. python is great! python is beginer freindly langauge?"
analyze_text(paragraph)
