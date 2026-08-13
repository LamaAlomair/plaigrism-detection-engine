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

matches = 0 # Counting matches
total_windows = len(submission_words) - Window_Size + 1 # How many chunks of text can be created from the submission

# Go through each window (chunks of text) in submission
for i in range(total_windows):
  # Get words from submission 
  sub_window = ""
  for j in range (Window_Size):
    sub_window = sub_window + submission_words[i + j] + " "
  sub_window = sub_window.strip()

  # Compare with each window (chunks of text) in document
  found_match = False
  for k in range(len(document_words) - Window_Size + 1):
    # Get words from document
    doc_window = ""
    for m in range(Window_Size):
      doc_window = doc_window + document_words[k + m] + " "
    doc_window = doc_window.strip()

    # Check if they match :
    if sub_window == doc_window:
      matches = matches + 1
      found_match = True
      break

# Calculate similarity percentage
if total_windows > 0:
  similarity = (matches / total_windows) * 100
else:
  similarity = 0.0

# Stop timing
end_time = time.time()
total_time = end_time - start_time

print("Plsigirism Detection - Naive Approach")
print(f"DataSet size: {DataSet_Size}")
print(f"Subject: {Subject}")
print(f"Window size: {Window_Size}")
print(f"comparing: {Submission_File} to {Document_File}")
print(f"Similarity Score: {similarity: .2f}%")
print(f"Time: {total_time: .4f} seconds")