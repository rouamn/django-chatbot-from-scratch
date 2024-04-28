Installation:
mkdir myproject
$ cd myproject
$ python -m venv venv
Activate it:
venv\Scripts\activate
Install PyTorch and dependencies
For Installation of PyTorch see official website.

You also need nltk:

pip install nltk
If you get an error during the first run, you also need to install nltk.tokenize.punkt: Run this once in your terminal:

$ python
>>> import nltk
>>> nltk.download('punkt')
>>> Run

python train.py
This will dump data.pth file. And then run

python chat.py
