"""
Cody Choo-Foo
261116178
"""

import musicalbeeps

class Note:

    OCTAVE_MIN = 1
    OCTAVE_MAX = 7

    def __init__(self, duration, pitch, octave = 1, accidental = 'natural'):
        '''(float, str, int, str) -> NoneType
        creates an object of type Note
        
        >>> note = Note(2.0, 'C', 2, 'natural')
        >>> note.pitch
        'C'
        >>> note.octave
        2
        >>> note.duration
        2.0
        
        >>> note1 = Note(5.0, 'B', 2, 'natural')
        >>> note1.octave
        2
        >>> note1.accidental
        'natural'
        
        >>> note2 = Note(5.0, 'G', 2, 'sharp')
        >>> note2.duration
        5.0
        >>> note2.pitch
        'G'
        
        '''
        
        if type(duration) != float or duration <= 0:
            raise AssertionError("Invalid duration input")


        

        if type(pitch) != str or len(pitch) != 1 or pitch not in "ABCDEFGR":
            raise AssertionError("Invalid pitch input")


        if type(octave) != int or octave>self.OCTAVE_MAX or octave<self.OCTAVE_MIN:
            raise AssertionError("Invalid octave input")


        if type(accidental) != str or accidental.lower() not in "naturalsharpflat":
            raise AssertionError("Accidental value is an invalid input")
        
        
        self.duration = duration
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental.lower()
    
    def __str__(self):
        '''() -> str
        returns a string with the diration, pitch, octave and accidental values
        
        >>> note = Note(2.0, 'C', 2, 'natural')
        >>> print(note)
        2.0 C 2 natural
        
        >>> note1 = Note(5.0, 'B', 2, 'natural')
        >>> print(note1)
        5.0 B 2 natural

        >>> note2 = Note(5.0, 'G', 2, 'sharp')
        >>> print(note2)
        5.0 G 2 sharp
        '''

        return str(self.duration)+" "+ self.pitch+ " "+str(self.octave)+ " "+self.accidental

    def play(self, player):
        '''(player) -> NoneType

        contructs the note string to be used by method play_note ()

        '''

        if self.pitch == 'R':
            player.play_note('pause', self.duration)

        elif self.accidental == 'sharp':
            player.play_note(self.pitch+str(self.octave)+'#', self.duration)
        
        elif self.accidental == 'flat':
            player.play_note(self.pitch+str(self.octave)+'b', self.duration)
        
        elif self.accidental == 'natural':
            player.play_note(self.pitch+str(self.octave), self.duration)
            







