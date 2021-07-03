import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

raw_dict = 'dataset/Train_Full'
csv_path = 'dataset/csv'


def read_from_dir(dir, label=None):
    if label is None:
        label = dir.split('/')[-1]
    label = '_'.join(label.lower().split())
    data = []
    filepaths = os.listdir(dir)
    if filepaths and len(filepaths):
        for file in filepaths:
            with open(f"{dir}/{file}", mode='rb') as f:
                text = f.read()
                data.append(text.decode('utf16').strip())
    return label, data


def save_to_csv(label, data):
    df = pd.DataFrame(data, columns=['text'])
    df.to_csv(f'{csv_path}/{label}.csv')


if __name__ == "__main__":
    folders = os.listdir(raw_dict)
    print(folders)
    for dir in folders:
        label, data = read_from_dir(f"{raw_dict}/{dir}")
        save_to_csv(label, data)
        print(label)
    print(folders)
