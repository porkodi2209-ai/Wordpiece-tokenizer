# Wordpiece-tokenizer

## Project Overview

This project implements a custom WordPiece tokenizer using Python and the Hugging Face Tokenizers library. The application trains a tokenizer using a given text dataset and converts input text into WordPiece subword tokens and their corresponding token IDs.

A Streamlit interface is used to make the tokenizer interactive and easy to test.

## Features
- Train a custom WordPiece tokenizer
- Use a text dataset for tokenizer training
- Split text into subword tokens
- Generate token IDs
- Display the total number of tokens
- Automatically generate tokenizer.json
- Interactive Streamlit interface
- Supports special tokens such as [UNK], [CLS], [SEP], [PAD], and [MASK]

## Technologies Used
- Python
- Streamlit
- Hugging Face Tokenizers
- WordPiece Tokenization

## How It Works
- Training text is stored in data.txt.
- The WordPiece tokenizer is initialized.
- The tokenizer is trained using the provided dataset.
- The trained tokenizer is saved as tokenizer.json.
- The user enters text through the Streamlit interface.
- The text is converted into WordPiece tokens.
- Token IDs and the total number of tokens are displayed.
  
## Example
- Input
 - Natural language processing is useful.
- Output
 - The application displays:

   - WordPiece Tokens
   - Token IDs
   - Number of Tokens

## Demo
## Screenshot
<img width="1920" height="1080" alt="Screenshot (128)" src="https://github.com/user-attachments/assets/fe440c06-cba3-4d55-9472-3d240f4b7a4b" />

<img width="1920" height="1080" alt="Screenshot (131)" src="https://github.com/user-attachments/assets/8d87ec8f-f041-4415-aee1-553b3345ac81" />

<img width="1920" height="1080" alt="Screenshot (130)" src="https://github.com/user-attachments/assets/8d11b072-18fa-4a61-9265-fa7c5c8ded72" />

<img width="1920" height="1080" alt="Screenshot (131)" src="https://github.com/user-attachments/assets/041b490c-ffc0-4fd0-a1d6-b7cb4def59f3" />


## Conclusion

This project demonstrates the implementation of WordPiece subword tokenization using a custom training dataset. It provides an interactive way to understand how text is divided into smaller subword units and converted into numerical token IDs. The project also demonstrates how a trained tokenizer can be saved and reused through the generated tokenizer.json file.
