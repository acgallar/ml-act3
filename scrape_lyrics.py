#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: demo.py
Author: Ignacio Soto Zamorano
Email: ignacio[dot]soto[dot]z[at]gmail[dot]com
Github: https://github.com/ignaciosotoz
Description: Scrape lyrics from a defined dictionary of artists
"""


import os, sys
import pylyrics3 as pyl
import pandas as pd
from tqdm import tqdm

artists = {'rock': ['Red Hot Chili Peppers', 'The Beatles', 'The Doors', 'System of a Down', 'Oasis', 'Incubus', 'Kiss', 'Nickelback',
                    'Pink Floyd', 'Led Zeppelin', 'The Clash', 'The Smiths', 'Bob Dylan', 'Radiohead', 'Bruce Springsteen', 'Rage Against The Machine',
                    'Faith No More', 'The Smashing Pumpkins', 'Weezer', 'Modest Mouse', 'Rush', 'Queen'],
           'pop': ['Lorde', 'Carly Rae Jepsen', 'Dua Lipa', 'Sam Smith', 'Britney Spears', 'Michael Jackson', 'Nicki Minaj', 'SIA', 'Spice Girls'],
           'hiphop': ['Method Man',  'Raekwon', 'Ghostface Killah', 'Killer Mike', 'Kendrick Lamar', 'Public Enemy', 'NWA', 'De La Soul',
                      'Eminem', 'Mobb Deep', 'Black Star', 'Mos Def', 'MF Doom', 'A Tribe Called Quest', 'Kanye West', 'Dr. Dre', ],
           'metal': ['Slayer', 'Anthrax','Meshuggah', 'Necrophagist', 'Tool', 'Iron Maiden', 'Metallica', 'Mayhem', 'Immortal', 'Megadeth', 'Deicide',
                     'Vital Remains', 'Gorgoroth', 'Cannibal Corpse', 'Opeth']}

def scrape_lyrics(artist, genre):
    """TODO: Wrapper for pylyrics3 query

    :artist: artist name (string)
    :genre: genre (string)
    :returns: returns a list of lists with artist name, genre, song name and lyrics.

    """
    holder = []
    tmp_artist_songs = pyl.get_artist_lyrics(artist)
    total_songs = len(tmp_artist_songs)
    song_counter = 0
    for song in tqdm(tmp_artist_songs):
        print("Scraping {} - {} out of {}".format(song, song_counter, total_songs))
        song_counter += 1
        tmp_song_array = [artist, genre, song, tmp_artist_songs[song]]
        holder.append(tmp_song_array)
    return holder

def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    if 'dump' in os.listdir():
        print("dump folder is already defined. Files in it will be overwritten.\n")
        answer = input("Do you wish to delete dump folder? [Y/N]\n")

        while answer is not "Y" or "N":
            answer = input("Input is not valid. Please try again\n Do you wish to delete dump folder? [Y/N]")
        if answer == "Y":
            os.removedirs('dump')
            os.makedirs('dump', mode=0o77)
        elif answer == "N":
            sys.exit("Scraper will not run.")
    else:
        os.makedirs('dump', mode=0o777)

    for key, value in tqdm(artists.items(), desc='Genres in dictionary'):
        for art in tqdm(value, desc='Artists in each genre'):
            print("\n\nScraping {}\n\n".format(art))
            pd.DataFrame(scrape_lyrics(art, key)).to_csv("./dump/{}_scrape.csv".format(art.lower().replace(" ", "_")))

if __name__ == "__main__":
    main()
