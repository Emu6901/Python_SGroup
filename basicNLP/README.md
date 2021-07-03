# Creating a TF-IDF Model from Scratch in Python

- The TF-IDF model is a method to represent words in numerical values. “Hello there, how have you been?”, you can easily understand what I am trying to ask you but computers are good with numbers and not with words.

- In order for a computer to make sense of the sentences and words, we represent these sentences using numbers while hoping to preserve the context and meaning.

- TF-IDF model is one such method to represent words in numerical values. TF-IDF stands for “Term Frequency – Inverse Document Frequency”.

## TF-IDF = Term Frequency (TF) * Inverse Document Frequency (IDF)
#### where:
#### tf(t,d) = count of t in d / number of words in d
#### idf(t) = log(N/(df + 1))

## Install
- git clone https://github.com/Emu6901/Python_Sgroup.git
- cd basicNLP  
- Extract Train_Full.rar zip into a folder named dataset
- Create a folder named csv in the project
- pip install -r requirements.txt
- python doctocsv.py (convert from docs into csv)
- python preprocessing.py (convert from csv into number vector)
 