import argparse
import pickle
import numpy as np
from resemblyzer import VoiceEncoder, preprocess_wav

# Define the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--human_embeddings", type=str, help="Location of the human voice embeddings file")
parser.add_argument("--ai_embeddings", type=str, help="Location of the AI voice embeddings file")
parser.add_argument("--target", type=str, help="Location of the input audio file")
args = parser.parse_args()

# Load the human and AI voice embeddings from the files
with open(args.human_embeddings, "rb") as f:
    human_embeddings = pickle.load(f)

with open(args.ai_embeddings, "rb") as f:
    ai_embeddings = pickle.load(f)

# Preprocess the input audio file
wav = preprocess_wav(args.target)

# Get the embedding of the input audio file
encoder = VoiceEncoder()
input_embedding = encoder.embed_utterance(wav)

# Calculate the cosine similarities between the input embedding and the human and AI embeddings
human_similarities = np.dot(human_embeddings, input_embedding) / (np.linalg.norm(human_embeddings, axis=1) * np.linalg.norm(input_embedding))
ai_similarities = np.dot(ai_embeddings, input_embedding) / (np.linalg.norm(ai_embeddings, axis=1) * np.linalg.norm(input_embedding))

# Determine the maximum similarity among the human and AI embeddings
if np.max(human_similarities) > np.max(ai_similarities):
    print("The input audio is most similar to a human voice")
else:
    print("The input audio is most similar to an AI voice")
