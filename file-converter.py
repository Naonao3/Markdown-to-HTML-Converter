import sys
import markdown

def main():
    command = sys.argv[1]
    inputFile = sys.argv[2]
    outputFile = sys.argv[3]

    if command == "markdown":
        try:
            with open(inputFile,"r") as f:
                text = f.read()
        except FileExistsError:
            print("no file")
        md = markdown.Markdown(extensions=["toc"])
        html = md.convert(text)
        with open(outputFile,"w") as f:
            f.write(html)
    else:
        ("input correct command")

if __name__ == "__main__":
    main()