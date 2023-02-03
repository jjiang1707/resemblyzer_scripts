import argparse
import os
import numpy as np
import pickle
from resemblyzer import VoiceEncoder, preprocess_wav

# Define the command line argument for the file paths location
parser = argparse.ArgumentParser()
parser.add_argument("--folder", type=str, help="Location of the input audio files")
parser.add_argument("--mode", type=str, help="Mode of embedding generation: 'human' or 'ai'")
args = parser.parse_args()

# Set of input audio files
fpaths = []
for filename in os.listdir(args.folder):
    if filename.endswith(".wav"):
        fpaths.append(os.path.join(args.folder, filename))

# Preprocess the input audio files
wavs = [preprocess_wav(fpath) for fpath in fpaths]

# Get the embeddings of the input voices
encoder = VoiceEncoder()
embeddings = np.stack([encoder.embed_utterance(wav) for wav in wavs])

# Save the voice embeddings to a file
embeddings_file = f"embeddings_{args.mode}.pkl"
with open(embeddings_file, "wb") as f:
    pickle.dump(embeddings, f)
