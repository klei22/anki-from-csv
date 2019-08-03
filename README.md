# CSV to Anki

Anki is great, use this script to create your own flashcards straight from a csv file.

## Installation

To install have python3 and run:

```sh
./install_deps.sh
```

This repo depends on [genanki](https://github.com/kerrickstaley/genanki).

## Workflow

Using the `csv_to_anki.py` script is very simple two step process, see steps below:

### Step 1/2: Create vocabulary csv with the vocab, e.g. `mandarin_numbers.csv`

With vim/emacs or preferred editor create a csv file.

See example below, `mandarin_numbers.csv`:

```sh
1,一,yī
2,二,èr
3,三,sān
4,四,sì
5,五,wǔ
6,六,liù
7,七,qī
8,八,bā
9,九,jiǔ
10,十,shí
```

### Step 2/2: run `csv_to_anki.py` specifying vocab set

Run the following replacing `<vocab_set_basename>` with your vocab list:

`python3 csv_to_anki.py <vocab_set_basename>`

For example

```sh
python3 csv_to_anki.py mandarin_numbers
```

Make sure to omit the extension `.csv`

This last example will create a `mandarin_numbers.apkg` which you can open with any Anki app : )

## Modifications

There are just two sections you'll need to modify if you'd like to add more fields or reduce to just two.

We'll show below an example for moving from English to Mandarin to just English to say French.


### Create English to French Vocab CSV


create `french_numbers.csv`

```sh
1,un
2,deux
3,Trois
4,quatre
5,cinq
6,six
7,Sept
8,huit
9,neuf
10,Dix
```


#### edit the fields of the model


before:
```python
    my_model = genanki.Model(
	    1000000000,
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
```

after:
```python
    my_model = genanki.Model(
	    1000000000,
	    deck_name,
	    fields=[
		{'name': 'English'},
		{'name': 'French'},
		],
	    templates=[
		{
		    'name': 'Card Template 1',
		    'qfmt': '<center style="font-size:30px">{{English}}</center>',
		    'afmt': '{{FrontSide}} <hr> <p align=center style="font-size:30px"> {{French}}</p>',
		    },
		])
```


### modify the number of rows that `csv_to_anki.py` reads


before
```python
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
```

after
```python
    # english, pinyin, simplified
    with open(csv_name, newline='') as csvfile:
        anki_reader = csv.reader(csvfile)
        for row in anki_reader:
            new_card = genanki.Note( 
                    model = my_model,
                    fields = [row[0],row[1]])
            my_deck.add_note(new_card)
    my_package = genanki.Package(my_deck)
    my_package.write_to_file(package_name)
```

### run the `csv_to_anki.py` script

```sh
python3 csv_to_anki.py french_numbers
```

and you should now have apkg called `french_numbers.apkg` ready to import to Anki from and Anki app : )


