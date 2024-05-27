def main(text):
    output = ""
    for x in text:
        if 1 <= (ord(x.lower()) - 96) <= 27:
            output += str(ord(x.lower()) - 96)
            output += " "
    return output.rstrip(" ") # Deletes space in the end of the result

if __name__ == '__main__':
    print(main(input('Input your sentence: ')))