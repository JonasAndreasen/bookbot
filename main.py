def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path).lower()
    words = seperate_words(text)
    n_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_report = get_chars_report(chars_dict,n_words)

def get_chars_report(chars_dict,n_words):
    print("--- Begin report of books/frankenstein.txt --- \n" + 
          f"{n_words}" + " words found int the document")
    dict_to_list = list(chars_dict.items())
    for i in range(0,len(dict_to_list)):
            print(f"The '{dict_to_list[i][0]}' character was found {dict_to_list[i][1]} times")

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_num_words(text):
    n_words = text.split()
    return len(n_words)

def seperate_words(text):
    words = text.split()
    return words

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()