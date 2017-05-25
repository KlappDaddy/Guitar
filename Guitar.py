#=========== IMPORTS

import sys
import time

#=========== CHORDS (Work in progress)

g = '[G]'
d = '[D]'
Em = '[Em]'
c = '[C]'
a = '[A7]'
b = '[Bm]'

#=========== FIRST VERSE

def verse(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.06)

print('[Verse]\n--------------------------------------')
print(       '[G]')
verse("Well you done done me and you bet I felt it,\n")
print('   [D]')
verse("I tried to be chill but you're so hot that I melted,\n")
print('  [Em]')
verse("I fell right through the cracks,\n")
print('[C]')
verse("And now I'm tryin to get back...\n")
print('           [G]')
verse("Before the cool done run out, I'll be given it my bestest\n")
print('    [D]')
verse("and Nothin's gonna stop me but divine intervention\n")
print('   [Em]')
verse("I reckon it's again my turn,\n")
print('   [C]         [D]')
verse('To Win some or learn some....\n')

#=========== CHORUS

def chorus(str):
	for roo in str:
		sys.stdout.write(roo)
		sys.stdout.flush()
		time.sleep(0.05)

print('[Chorus]\n--------------------------------------')
print('[G]            [D]')
chorus("But I wont hesitate\n")
print('             [Em]')
chorus("No more, No more\n")
print('            [C]              [G] [D] [Em] [C]')
chorus("It can not wait I'm yours\n")
time.sleep(5)

#=========== 2ND VERSE

print('[Verse]\n--------------------------------------')
print('[G]                                 [D]')
verse("Well, open up your mind and see like me,\n")
print('                            [Em]')
verse("Open up your plans and damn you're free.\n")
print('                              [C]')
verse("Look into your heart and you'll find love, love, love, love.\n")
print('[G]                                               [D]                          [Em]')
verse("Listen to the music of the moment, people dance and sing, we're just one big family\n")
print('                                      [C]                         [A7]')
verse("And it's our god-forsaken right to be loved, loved, loved, loved, loved.\n")

#=========== 2ND CHORUS

print('[Chorus]\n--------------------------------------')
print('[G]             [D]')
chorus("So I won't hesitate\n")
print('             [Em]')
chorus("No more, No more\n")
print('           [C]')
chorus("It cannot wait,\n I'm yours")

#=========== BRIDGE

def bridge(str):
	for hello in str:
		sys.stdout.write(hello)
		sys.stdout.flush()
		time.sleep(0.03)

print('[Bridge]\n--------------------------------------')
print('[G]                    [Bm]') 
bridge("Doo do do doo doo do, doo do doo do doo do\n")
print('[Em]                     [D]                [C]')
bridge("Do you want to come on, scooch on over closer, dear\n")
print('                     [A7]')
bridge("And I will nibble your ear\n")
print('[G] [Bm] [Em] [D] [C] [A7]')





















