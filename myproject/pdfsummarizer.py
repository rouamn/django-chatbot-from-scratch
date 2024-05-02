# pdfsummarizer.py
import PyPDF2
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdf_file.open('rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text
   

def summarize_text(text):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
    freqTable = dict()
    
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
            
    sentences = sent_tokenize(text)

    def getsentenceValue():
        sentenceValue = dict()
        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq
        return sentenceValue

    def getsumValues():
        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]
        average = int(sumValues / len(sentenceValue))
        return average

    sentenceValue = getsentenceValue()
    average = getsumValues()

    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence]) > (1.2 * average):
            summary += " " + sentence

    return summary

def summarize_pdf(pdf_file):
    text = extract_text_from_pdf(pdf_file)
    summary = summarize_text(text)
    return summary
