def solution(word):
    book = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    def find_book(current_word):
        if current_word:
            words.append(current_word)
        if len(current_word) == 5:
            return
        for w in book:
            find_book(current_word + w)
            
    find_book('')
    return words.index(word) +1