# -*- coding: utf-8 -*-
import tweepy
import time
from random import choice, shuffle


def get_word_matches(word, lines):
    matches = []
    for headline in HEADLINES_FILE:
        words = headline.split(" ")
        if word in words:
            matches.append(headline)
    return matches


def test_common_word(word, lines):
    # verifica se a palavra de ligação pode ser usada
    matches = get_word_matches(word, lines)
    if not len(matches) > 1:
        return False
    return True


def get_dada_headline(lines, wordlist):
    # escolher uma palavra para dividir e ver se podemos usar
    common_word = choice(wordlist).strip()
    while not test_common_word(common_word, lines):
        common_word = choice(wordlist).strip()

    # apanhar duas linhas e combiná-las
    matches = get_word_matches(common_word, lines)
    shuffle(matches)
    line1 = matches.pop()
    line2 = matches.pop()
    # assegurar que não são iguais
    while not line1 != line2:
        line1 = matches.pop()
        line2 = matches.pop()

    # repartir as linhas e recombiná-las de seguida
    part1 = line1.split(" %s " % common_word)[0].strip()
    part2 = line2.split(" %s " % common_word)[-1].strip()

    output = "%s %s %s" % (part1, common_word, part2)

    # assegurar que é um resultado novo e não uma cópia do anterior
    if output == line1 or output == line2:
        output = get_dada_headline(lines, wordlist)

    return output


if __name__ == "__main__":
    keys = open("keys.txt", 'r')
    CONSUMER_KEY = keys.readline().rstrip("\n")
    CONSUMER_SECRET = keys.readline().rstrip("\n")
    ACCESS_KEY = keys.readline().rstrip("\n")
    ACCESS_SECRET = keys.readline().rstrip("\n")

    success = False
    while not success:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)

        WORDLIST_PT = open("wordlist-pt.txt", "r").readlines()
        HEADLINES_FILE = open("headlines.txt", "r").readlines()

        stringParaEnviar = get_dada_headline(HEADLINES_FILE, WORDLIST_PT)
        # print "post:", stringParaEnviar
        if api.update_status(status=bytes(stringParaEnviar)):
            success = True
        else:
            # print "vou esperar 5 segundos e tentar de novo"
            time.sleep(5)
