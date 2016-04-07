This project has moved to the Natural Language Processing Collective at
[nlp-api](https://github.com/nlp-collective/nlp-api)

# nlp-api [hard WIP]

A simple API servicing common natural language processing techniques
for the English language, NLP-related data visualization solutions, and a barebones
front-end demo.

## Setup

### Requirements

<pre>
git clone https://github.com/rainiera/nlp-api
cd nlp-api
# If you're using Anaconda (recommended)
conda env create -f environment.yml

# If you're using venv and pip
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
</pre>

### API

The command line argument after the filename is any open port you want to hit
to use the API. We'll use port `8000` for API examples and port `5000` for demo examples.

<pre>
cd nlp-api/api
python api.py 8000
</pre>

### Demo

The API needs to be set up and **running** before you can run the demo (see previous).

The two command line arguments after the filename are `DEMO_PORT` and `API_PORT`.

<pre>
cd nlp-api/demo
python demo.py 5000 8000
</pre>

At this point, you open up your browser and try out the demo at `localhost:5000`.

## Usage

### `POST` **Part of Speech Tagger**

Classifies every input word with a part of speech tag from the Treebank tagset.

Input

<pre>
curl 'http://localhost:8000/postokenize?key=<b>YOUR_API_KEY</b>' --data '{"data":"And now for something completely different"}'
</pre>

Output

<pre>
{
 'And': 'CC',
 'now': 'RB',
 'for': 'IN',
 'something': 'NN',
 'completely': 'RB',
 'different': 'JJ'
}
</pre>

### `POST` **Word Cloud**

Input

<pre>
curl 'http://localhost:8000/wordcloud?key=<b>YOUR_API_KEY</b>' --data '{"data":"The quick brown fox jumps over the lazy dog near the river bank"}'
</pre>

Output

**TODO**: Implement word cloud API

More specific API docs are at [**TODO**: Make documentation](http://example.com).

## What's available
- POS tagger

## What's next
- Word cloud
