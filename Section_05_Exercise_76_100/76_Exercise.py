"""
Exercise No. 76

Juan loves the Dakti song and wants to memorize the chorus of the song. His friend sent him the chorus in phrases, but
the phrases are somewhat strange; they do not have an order, and they have numbers. His friend helps Juan organize the
chorus of the song.

Use RegEx, natural sorting, sorting, or lambda functions; your imagination has no limits.

First, organize the words based on the numbers they have, then delete the numbers once they are organized.

Three steps:
    "worl2d hello" -> " hello worl2d " -> " hello world "

    "i2s this a3 t4este    " -> "this i2s a3 t4est" -> "this is a test"

    "yo2u cr3azy alre ?" -> "a1re yo2u cr3azy" -> "are you crazy"

Here are some examples:
Examples:
    dakiti("en5tere y2a bab1y y3o 4me s6e not7a cuand8o 9me-ves") -> "baby ya yo me entere se nota cuando me-ves"

    dakiti("quie3res bebe4r dime1 e5s qu6e tu7 er8es m9i-bebe") -> "ahi donde no has llegado sabes que yo te-llevare"

    dakiti("quie3res bebe4r dime1 e5s qu6e tu7 er8es m9i-be") -> "dime que quieres beber es que tu eres mi-bebe"

Notes:
    - Trick, natural sort.
"""
from re import *


def dakiti(setence):
    dakiti = lambda s: ' '.join(sub('\d', '', y) for y in sorted(s.split(), key=lambda x: search('(\d)', x).group()))
    return dakiti

print(dakiti("en5tere y2a bab1y y3o 4me s6e not7a cuand8o 9me-ves"))
