from collections import defaultdict
from pathlib import Path
import math
from utils import directory_reader

dir_path = "/Users/apple/Documents/github/pydocsearcher/python-3.14-docs-text"


def get_tf(content: str) -> dict[str, float]:
    """
    Compute normalized term frequency for a single document.
    """
    tf_dict = {}
    words = content.strip().split()  # splits on any whitespace
    for word in words:
        word = word.lower()  # normalize to lowercase
        tf_dict[word] = tf_dict.get(word, 0) + 1

    total_words = sum(tf_dict.values())
    for k in tf_dict:
        tf_dict[k] /= total_words  # normalize TF

    return tf_dict

# -----------------------------
# Compute Inverse Document Frequency (IDF)
# -----------------------------
def get_idf(tf_path_word: dict[Path, dict[str, float]]) -> dict[str, float]:
    """
    Compute IDF for each word in the corpus.
    """
    total_docs = len(tf_path_word)
    doc_freq = defaultdict(int)

    for tf_dict in tf_path_word.values():
        for word in tf_dict.keys():
            doc_freq[word] += 1

    idf_dict = {}
    for word, df in doc_freq.items():
        idf_dict[word] = math.log(total_docs / (1 + df))  # add 1 to avoid division by zero

    return idf_dict


def get_tf_idf(tf_path_word: dict[Path, dict[str, float]], idf_dict: dict[str, float]) -> dict[str, dict[Path, float]]:
    """
    Compute TF-IDF for each word per document.
    Returns: {word: {doc_path: tf-idf value}}
    """
    tfidf_dict = defaultdict(dict)

    for path, tf_dict in tf_path_word.items():
        for word, tf_val in tf_dict.items():
            tfidf_dict[word][path] = tf_val * idf_dict[word]

    return tfidf_dict

tf_path_word = {}

for path, content in directory_reader(dir_path):
    tf_path_word[path] = get_tf(content)

print(f"Total documents processed: {len(tf_path_word)}")

# Compute IDF
idf_dict = get_idf(tf_path_word)

# Compute TF-IDF
tfidf_dict = get_tf_idf(tf_path_word, idf_dict)

print(tfidf_dict)
