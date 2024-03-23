#!/usr/bin/python3

from twttr import shorten

def test_shorten():
    """test the dhorten function"""
    assert shorten('Twitter') == 'Twttr'
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten('Abdelghani Ait Ben Braim') == 'bdlghn t Bn Brm'
