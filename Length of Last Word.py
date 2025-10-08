def lengthOfLastWord( s: str):
    da=s.split()
    return len(da[-1])
print(lengthOfLastWord(s = "Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))