import re
import numpy as np

def split_into_chunks(text, max_words=700):
    para = re.split(r'\n+', text)
    chunks = []
    current_chunk = ""
    current_word_count = 0

    for i in para:
        word_count = len(i.split())
        if current_word_count + word_count <= max_words:
            current_chunk += i + "\n"
            current_word_count += word_count
        else:
            chunks.append(current_chunk.strip())
            current_chunk = i + "\n"
            current_word_count = word_count

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def calculate_cosine_similarity_numpy(user_v, chunks_v):
    dot_product = np.dot(user_v, chunks_v)
    magnitude_a = np.linalg.norm(user_v)
    magnitude_b = np.linalg.norm(chunks_v)
    if magnitude_a == 0 or magnitude_b == 0:
        return 0
    return dot_product / (magnitude_a * magnitude_b)

def mergesort(a):
    if len(a) == 1:
        return a

    mid = len(a) // 2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])

    i = j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i][1] > right[j][1]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged