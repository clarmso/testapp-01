import argparse

def setUpParser():
    parser = argparse.ArgumentParser(description='Process a message')
    parser.add_argument('--message', '-m',
                        type=int,
                        help='an integer to determine the message')
    return parser

def determineMessage(message):
    if message == 0:
        return "I'm here."
    elif message > 0:
        return "Hello world!"
    else:
        return "Goodbye world!"

def main():
    args = setUpParser().parse_args()
    print(determineMessage(args.message))

if __name__ == "__main__":
    main()