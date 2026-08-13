import time

# Intial information

Window_Size = 8 # The number of words to compare at once

# Choose size: "small" ~1200-1700 characters, "medium" ~4k-5k characters, "large" ~22k-30k characters
DataSet_Size = "small"

# Choose subject: "Academic", "Literature", "Science"
Subject = "Academic"

# Set file paths for dataset and subject
Submission_File = f"DataSet/{DataSet_Size}/{Subject}/submission.txt"
Document_File = f"DataSet/{DataSet_Size}/{Subject}/document.txt"

Prime = 101 # Prime number for hashing (to keep the hash value between 0-100)
Base = 256 # Base for hash calculation (ASCII has 256 possible values)

# Function to calculate hash of a text
def calculate_hash(text):
    hash_value = 0
    position = 0
    for char in text:
        hash_value = hash_value + ord(char) * pow(Base, position)
        hash_value = hash_value % Prime
        position = position + 1
    return hash_value

# Read submission file
submission_file = open(Submission_File, 'r', encoding='utf-8')
submission_text = submission_file.read()
submission_file.close()

# Split the submission text into lowercase words
submission_words = submission_text.lower().split()

# Read document file 
document_file = open(Document_File, 'r', encoding='utf-8')
document_text = document_file.read()
document_file.close()

# Split the document text into lowercase words
document_words = document_text.lower().split()

# Start timing from here
start_time = time.time()

# Step 1: Pre-compute all document hashes once and store them
doc_hashes = {}
for j in range(len(document_words) - Window_Size + 1):
    # Get words from document
    doc_window = ""
    for k in range(Window_Size):
        doc_window = doc_window + document_words[j + k] + " "
    doc_window = doc_window.strip()

    # Calculate hash for document
    doc_hash = calculate_hash(doc_window)

    # Store hash in window text
    if doc_hash not in doc_hashes: 
        doc_hashes[doc_hash] = []
    doc_hashes[doc_hash].append(doc_window)

# Step 2 : Check submission windows against document hashes (already stored)
matches = 0 # Counting matches
total_windows = len(submission_words) - Window_Size + 1 # How many chunks of text can be created from the submission

for i in range(total_windows):
  # Get words from submission 
  sub_window = ""
  for j in range (Window_Size):
    sub_window = sub_window + submission_words[i + j] + " "
  sub_window = sub_window.strip()

  # Calculate hash for submission
  sub_hash = calculate_hash(sub_window)


  #check if submission hash exits in doucment hash
  if sub_hash in doc_hashes:
     # Verify if the actual text match as well (not just hash) for hash collisions
     if sub_window in doc_hashes[sub_hash]: # Condition to check if submission text in dictionary of document hashes
        matches = matches + 1

# Calculate similarity percentage
if total_windows > 0:
  similarity = (matches / total_windows) * 100
else:
  similarity = 0.0

# Stop timing
end_time = time.time()
total_time = end_time - start_time

print("Plsigirism Detection - Rabin-Karp Approach")
print(f"DataSet size: {DataSet_Size}")
print(f"Subject: {Subject}")
print(f"Window size: {Window_Size}")
print(f"comparing: {Submission_File} to {Document_File}")
print(f"Similarity Score: {similarity: .2f}%")
print(f"Time: {total_time: .4f} seconds")