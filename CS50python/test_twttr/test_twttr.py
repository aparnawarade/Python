from twttr import shorten
def main():
    test_shorten()

def test_shorten():
    assert shorten("whats up?")=="whts p?"
    assert shorten("WHATS UP?")=="WHTS P??"


if __name__=="__main__":
    main()
