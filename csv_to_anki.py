import genanki
import csv
import sys
import os


#usage:
# python3 csv_to_anki.py base_name
#for example, if input is `numbers.csv`:
# python3 csv_to_anki.py numbers
# which will create numbers.apkg
#afterwards use any anki app to open the .apkg file

#import args
deck_name=sys.argv[1]
package_name=deck_name + '.apkg'
csv_name=deck_name + '.csv'

my_deck = genanki.Deck(
        2000000000,
        deck_name)

def add_new_card(my_deck):

    my_model = genanki.Model(
	    1000000000,
# create package from files
	    deck_name,
	    fields=[
		{'name': 'English'},
		{'name': 'Pinyin'},
		{'name': 'Simplified'},
		],
	    templates=[
		{
		    'name': 'Card Template 1',
		    'qfmt': '<center style="font-size:30px">{{English}}</center>',
		    'afmt': '{{FrontSide}} <hr> <p align=center style="font-size:30px"> {{Simplified}} <br /> {{Pinyin}}</p>',
		    },
		])

    # english, pinyin, simplified
    with open(csv_name, newline='') as csvfile:
        anki_reader = csv.reader(csvfile)
        for row in anki_reader:
            new_card = genanki.Note( 
                    model = my_model,
                    fields = [row[0],row[1],row[2]])
            my_deck.add_note(new_card)
    my_package = genanki.Package(my_deck)
    my_package.write_to_file(package_name)

add_new_card(my_deck)
