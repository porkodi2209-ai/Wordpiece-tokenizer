import streamlit as st
from tokenizers import Tokenizer
from tokenizers.models import WordPiece
from tokenizers.trainers import WordPieceTrainer
from tokenizers.pre_tokenizers import Whitespace

st.set_page_config(
    page_title="WordPiece Tokenizer"
)

st.title("WordPiece Tokenizer")
st.write("Train and test a custom WordPiece tokenizer.")

@st.cache_resource
def train_tokenizer():
    tokenizer = Tokenizer(
        WordPiece(unk_token="[UNK]")
    )

    tokenizer.pre_tokenizer = Whitespace()

    trainer = WordPieceTrainer(
        vocab_size=1000,
        min_frequency=1,
        special_tokens=[
            "[UNK]",
            "[CLS]",
            "[SEP]",
            "[PAD]",
            "[MASK]"
        ]
    )

    tokenizer.train(["data.txt"], trainer)
    tokenizer.save("tokenizer.json")

    return tokenizer

tokenizer = train_tokenizer()

text = st.text_area(
    "Enter your text",
    placeholder="Example: Natural language processing is useful."
)

if st.button("Tokenize Text"):
    if text.strip():
        output = tokenizer.encode(text)

        st.subheader("WordPiece Tokens")
        st.write(output.tokens)

        st.subheader("Token IDs")
        st.write(output.ids)

        st.subheader("Number of Tokens")
        st.write(len(output.tokens))
    else:
        st.warning("Please enter some text.")