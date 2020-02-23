import sys
from os import listdir
from os.path import isfile, join
import eyed3
import os
from googlesearch import search
from contextlib import suppress
import shutil

with suppress(AttributeError):

    def check_author(song_name):
        name = "{}".format(song_name)
        song = eyed3.load(name)
        if song != None:

            # if song.tag.artist == 'The' or song.tag.artist == 'G':
            #     song.tag.artist = ''
            #     song.tag.save()

            if song.tag.artist != None:
                return song.tag.artist

    def change_author(song, author):
        name = "{}".format(song)
        # print(name)

        file = eyed3.load(name)
        if file != None:
            file.tag.artist = author
            file.tag.save()

    def change_name(song, author):
        song_name = song.strip(author).strip('-')
        if song_name.startswith('-') or song_name.startswith(','):
            song_name.strip('-')
            song_name.strip(',')
        try:
            os.rename(song, song_name)
        except:
            try:
                os.rename(song, '{}(1)'.format(song_name))
            except:
                os.rename(song, '{}(2)'.format(song_name))

    def main():
        list_of_files = os.listdir()
        list_of_songs = []
        list_of_authors = []
        for i in list_of_files:
            if i.endswith('.mp3'):
                list_of_songs.append(i)

        for i in list_of_songs:

            # print(i)
            try:
                current_author = check_author(i)
            except:
                shutil.move("C:\\Users\\emo\\Documents\\Python_projects\\Music_author_change\\{}".format(
                    i), "C:\\Users\\emo\\Documents\\Python_projects\\Music_author_change\\failed_to_change_author\\{}".format(i))

            list_of_authors.append(current_author)
        list_of_authors = list(dict.fromkeys(list_of_authors))

        for i in list_of_songs:
            for ii in list_of_authors:
                if ii != None:
                    if ii in i:
                        change_author(i, ii)
                        change_name(i, ii)
                        break

        # for i in list_of_songs:
        #     for ii in list_of_authors:
        #         if ii != None:
        #             if ii in i:
        #                 change_name(i, ii)
        #                 break


if __name__ == '__main__':
    main()
