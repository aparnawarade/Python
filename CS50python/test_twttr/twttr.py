"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py,
implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""

def main():
    s=input("Input:")
    print("Output:" ,shorten(s))

def shorten(word):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    #vowels_small=['a','e','i','o','u']
    newword=""
    for c in word:
            if c not in vowels:
                newword=newword+c
    return newword

if __name__=="__main__":
    main()
