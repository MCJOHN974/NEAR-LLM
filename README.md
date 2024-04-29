# NEAR-LLM

## About

This is an attempt to create Chat-GPT style Large Language Model, but trained on all near docs, zulip discussions, discussions in issues, in PRs, maybe something more.

## Structure

Currently this repo contains next parts:

Code:
- `extracting-data` web scarping and preparing data for training.
- `train` actually trains a model.
- `app` some code that allows you to play with resulting model.

Data:
- `data` stores data for training, maybe worth to split into `raw` and `prepared` in future
- `results` contains resulting model

# Usage

Generate data for training:
`python3 extracting-data/main.py`
Train model:
`python3 train/main.py`
Play with model:
`python3 app/main.py`


# Status

For now I just tried to do this and get some text. I have very few training data and poor training process, so results are not impressive yet.

Some dialogues with this LLM:
```
Prompt < What is reciept congestion in NEAR? 

Generated Text:
What is reciept congestion in NEAR?
Reciept congestion is the amount of network traffic that is sent to a node. It is the amount of network traffic that is sent to a node that is not connected to the network.
How much is reciept congestion in NEAR?
Reciept congestion is the amount of network traffic that is sent to a node that is not connected to the network.
How much is reciept congestion in NEAR?
```

```
Prompt < What is an epoch in NEAR blockchain?

Generated Text:
 What is an epoch in NEAR blockchain?

An epoch is a block that is created in the blockchain. It is a block that is created in the blockchain. It is a block that is created in the blockchain. It is a block that is created in the blockchain. It is a block that is created in the blockchain. It is a block that is created in the blockchain. It is a block that is created in the blockchain. It is a block that is created in the blockchain.
```

(Hope once here will be a comparison with some top tier LLMs)