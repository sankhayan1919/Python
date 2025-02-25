def sort(input):
    input = input("Enter: ")
    words_lower = input.lower()
    words = words_lower.split()
    sorted_words = sorted(words)
    sorted_input = ' '.join(sorted_words)
    result = sorted_input
    print(f"Original sentence: {input}")
    print(f"Sorted sentence: {result}")
sort(input)