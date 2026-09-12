def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    text = input()
    result = convert(text)
    print(result)

main()