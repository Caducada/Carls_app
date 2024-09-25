from functools import lru_cache

@lru_cache(maxsize=128)
def count_vowels(sentence):
    vowels = 'aeiou'
    return sum(1 for char in sentence.lower() if char in vowels)

def is_cached(sentence):
    count_vowels(sentence)
    cache_stats = count_vowels.cache_info()
    return cache_stats

def main():
    sentence = "This is an example sentence."
    cache_info_before = count_vowels.cache_info()
    
    print(f"Cache info before: {cache_info_before}")
    count_vowels(sentence)
    cache_info_after = count_vowels.cache_info()

    print(f"Is '{sentence}' cached? -> {cache_info_before.hits < cache_info_after.hits}")
    print(f"Cache info after: {cache_info_after}")

if __name__ == "__main__":
    main()
