import time
from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
import random

# Download NLTK data (run once)
nltk.download('punkt_tab', quiet=True)

# Sample base words for generating documents
BASE_WORDS = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog", 
              "sleeps", "high", "day", "quickly", "a", "all"]

class Node:
    def __init__(self, term):
        self.term = term
        self.doc_ids = []
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, term, doc_id):
        if not self.head:
            self.head = Node(term)
            self.head.doc_ids.append(doc_id)
            return
            
        current = self.head
        while current and current.term < term:
            prev = current
            current = current.next
            
        if current and current.term == term:
            if doc_id not in current.doc_ids:
                current.doc_ids.append(doc_id)
        else:
            new_node = Node(term)
            new_node.doc_ids.append(doc_id)
            if current == self.head:
                new_node.next = self.head
                self.head = new_node
            else:
                new_node.next = current
                prev.next = new_node
    
    def search(self, term):
        current = self.head
        while current and current.term < term:
            current = current.next
        if current and current.term == term:
            return current.doc_ids
        return []

def generate_documents(num_docs, words_per_doc):
    documents = {}
    for i in range(1, num_docs + 1):
        text = " ".join(random.choices(BASE_WORDS, k=words_per_doc))
        documents[i] = text
    return documents

def build_inverted_index(docs, output_file="inverted_index.txt"):
    inverted_index = defaultdict(list)
    
    with open(output_file, 'w') as f:
        for doc_id, text in docs.items():
            words = word_tokenize(text.lower())
            for word in words:
                if doc_id not in inverted_index[word]:
                    inverted_index[word].append(doc_id)
                    f.write(f"{word}: {doc_id}\n")
    
    return inverted_index

def build_structures(docs):
    hash_index = build_inverted_index(docs)
    
    linked_list = SortedLinkedList()
    for doc_id, text in docs.items():
        words = word_tokenize(text.lower())
        for word in words:
            linked_list.insert(word, doc_id)
    
    return hash_index, linked_list

def measure_performance(hash_index, linked_list, search_term):
    # Use perf_counter for higher precision
    start_time = time.perf_counter()
    hash_result = hash_index.get(search_term, [])
    hash_time = time.perf_counter() - start_time
    
    start_time = time.perf_counter()
    list_result = linked_list.search(search_term)
    list_time = time.perf_counter() - start_time
    
    return hash_result, hash_time, list_result, list_time

def main(num_docs, words_per_doc):
    documents = generate_documents(num_docs, words_per_doc)
    hash_index, linked_list = build_structures(documents)
    
    search_term = "fox"
    hash_result, hash_time, list_result, list_time = measure_performance(hash_index, linked_list, search_term)
    
    print(f"Search term: '{search_term}'")
    print(f"Generated {num_docs} documents with {words_per_doc} words each")
    print("\nHashtable (Dictionary) Results:")
    print(f"Documents found: {hash_result}")
    print(f"Time taken: {hash_time:.6f} seconds")
    
    print("\nSorted Linked List Results:")
    print(f"Documents found: {list_result}")
    print(f"Time taken: {list_time:.6f} seconds")

if __name__ == "__main__":
    num_docs = int(input("Enter number of documents to generate: "))
    words_per_doc = int(input("Enter words per document: "))
    main(num_docs, words_per_doc)