def designerPdfViewer(h, word):
    word_len = len(word)
    max_count = 0
    for item in word:
        number = h[ord(item) - 97]
        if number > max_count:
            max_count = number
    return max_count * word_len