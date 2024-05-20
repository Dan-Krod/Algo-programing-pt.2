from typing import List, Dict

def get_longest_chain_length(words: List[str], word_index: Dict[str, int], i: int, memo: Dict[int, int]) -> int:
    """
    Compute the length of the longest chain ending with the word at index `i`.
    
    Args:
        words (List[str]): The list of words.
        word_index (Dict[str, int]): A dictionary mapping words to their indices in `words`.
        i (int): The current index in `words`.
        memo (Dict[int, int]): A memoization dictionary to store the results of subproblems.
        
    Returns:
        int: The length of the longest word chain ending at the word `words[i]`.
    """
    if i in memo:
        return memo[i]

    max_length = 1
    current_word = words[i]
    for j in range(len(current_word)):
        pred = current_word[:j] + current_word[j+1:]
        if pred in word_index:  
            chain_length = 1 + get_longest_chain_length(words, word_index, word_index[pred], memo)
            max_length = max(max_length, chain_length)
    memo[i] = max_length
    return max_length

def longest_word_chain(input_file_name: str, output_file_name: str) -> int:
    """
    Determine the length of the longest word chain and write the result to a file.
    
    Args:
        input_file_name (str): The name of the input file containing words.
        output_file_name (str): The name of the output file to write the result.
        
    Returns:
        int: The length of the longest word chain or -1 if there is an error.
    """
    try:
        words = read_data_from_file(input_file_name)
    except Exception:
        return -1
    
    words.sort(key=lambda word: -len(word))
    word_index = {word: i for i, word in enumerate(words)}

    max_chain_length = 0
    memo = {}
    for i in range(len(words)):
        max_chain_length = max(max_chain_length, get_longest_chain_length(words, word_index, i, memo))
    
    write_file(output_file_name, max_chain_length)
    return max_chain_length

def read_data_from_file(filename: str) -> List[str]:
    """
    Read a list of words from a file.
    
    Args:
        filename (str): The name of the file to read from.
        
    Returns:
        List[str]: A list of words read from the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        number_of_words = int(file.readline().strip())
        word_list = [file.readline().strip() for _ in range(number_of_words)]
    return word_list

def write_file(filename: str, result: int) -> None:
    """
    Write the result to a file.
    
    Args:
        filename (str): The name of the file to write to.
        result (int): The result to write.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(result))