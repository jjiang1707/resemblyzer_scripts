# resemblyzer_scripts
scripts to create embeddings and run a test to check if audio is AI generated

To create embeddings (create embeddings from folders containing the AI and Human samples):

python3 run_embeddings2 --human_embeddings=/home/ubuntu/Resemblyzer/embeddings_human.pkl --ai_embeddings=/home/ubuntu/Resemblyzer/embeddings_ai.pkl --target=/home/ubuntu/Resemblyzer/recordings_human/human.wav

to run AI detection test (specify the human and ai embeddings and the target audio file to analyze):

python3 run_ai_test.py --human_embeddings=/home/ubuntu/Resemblyzer/embeddings_human.pkl --ai_embeddings=/home/ubuntu/Resemblyzer/embeddings_ai.pkl --target=/home/ubuntu/Resemblyzer/recordings_ai/ai_1.wav


