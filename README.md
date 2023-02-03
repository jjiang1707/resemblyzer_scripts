

# resemblyzer_scripts
scripts to create embeddings and run a test to check if audio is AI generated

To create embeddings (create embeddings from folders containing the AI and Human samples):

> python3 run_embeddings.py --mode=ai --folder="/home/ubuntu/Resemblyzer/recordings_ai/"

to run AI detection test (specify the human and ai embeddings and the target audio file to analyze):

> python3 run_ai_test.py --human_embeddings=/home/ubuntu/Resemblyzer/embeddings_human.pkl --ai_embeddings=/home/ubuntu/Resemblyzer/embeddings_ai.pkl --target=/home/ubuntu/Resemblyzer/recordings_ai/ai_1.wav

# Example output

ubuntu@ip-172-31-30-206:/home/ubuntu/Resemblyzer# python3 run_ai_test.py --human_embeddings=/home/ubuntu/Resemblyzer/embeddings_human.pkl --ai_embeddings=/home/ubuntu/Resemblyzer/embeddings_ai.pkl --target=/home/ubuntu/Resemblyzer/recordings_human/human.wav
Loaded the voice encoder model on cpu in 0.01 seconds.
The input audio is most similar to a human voice

ubuntu@ip-172-31-30-206:/home/ubuntu/Resemblyzer# python3 run_ai_test.py --human_embeddings=/home/ubuntu/Resemblyzer/embeddings_human.pkl --ai_embeddings=/home/ubuntu/Resemblyzer/embeddings_ai.pkl --target=/home/ubuntu/Resemblyzer/recordings_ai/ai_1.wav
Loaded the voice encoder model on cpu in 0.01 seconds.
The input audio is most similar to an AI voice

# Dependencies

This is dependent on the Resemblyzer repo: https://github.com/resemble-ai/Resemblyzer



