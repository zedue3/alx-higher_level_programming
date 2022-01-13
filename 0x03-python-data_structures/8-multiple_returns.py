#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is not None:
        length = len(sentence)
        if length == 0:
            return (length, None)
        return (length, sentence[0])


if __name__ == '__main__':
    sentence = "At Holberton school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
