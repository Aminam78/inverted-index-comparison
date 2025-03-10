# Inverted Index Comparison

This project implements an inverted index using Python, comparing search performance between a hashtable (dictionary) and a sorted linked list. It’s designed for an "Advanced Information Retrieval" course exercise, generating random documents and measuring search efficiency.

## Prerequisites
- **Python**: Version 3.10 or higher (tested with Python 3.10)
- **NLTK**: Natural Language Toolkit for tokenization
- **Operating System**: Tested on Windows; should work on Linux/Mac with minor adjustments

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/inverted-index-comparison.git
cd inverted-index-comparison
```

### 2. Create a Virtual Environment
- **Windows (PowerShell)**:
  ```powershell
  C:\path\to\python.exe -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **Linux/Mac**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
  Replace `C:\path\to\python.exe` with your Python installation path (e.g., `C:\Python310\python.exe`).

### 3. Install Dependencies
With the virtual environment active:
```bash
pip install nltk
python -m nltk.downloader punkt_tab
```

### 4. Run the Program
- Ensure `inverted_index.py` is in the directory.
- Run:
  ```bash
  python inverted_index.py
  ```
- Enter inputs when prompted:
  ```
  Enter number of documents to generate: <number> (e.g., 100)
  Enter words per document: <number> (e.g., 25)
  ```

## Output
- **Console**: Displays search results and timing for "fox" using both hashtable and sorted linked list.
- **File**: Generates `inverted_index.txt` with the inverted index (word: doc_id pairs).

## Example
```bash
Enter number of documents to generate: 100
Enter words per document: 25
Search term: 'fox'
Generated 100 documents with 25 words each

Hashtable (Dictionary) Results:
Documents found: [1, 3, 4, ...]
Time taken: 0.000142 seconds

Sorted Linked List Results:
Documents found: [1, 3, 4, ...]
Time taken: 0.000387 seconds
```

## Notes
- Delete `inverted_index.txt` to start fresh:
  ```powershell
  Remove-Item inverted_index.txt  # Windows
  rm inverted_index.txt          # Linux/Mac
  ```
- Timing uses `time.perf_counter()` for precision.
- The sorted linked list may be slower due to O(n) search complexity vs. O(1) for the hashtable.

## Author
Amir Hossein Amin Moghaddam
Master's Student in Computer Software Engineering at Iran University of Science and Technology

Advanced Information Retrieval Course  
March 2025
