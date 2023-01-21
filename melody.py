"""
Cody Choo-Foo
261116178
"""

import note

class Melody:
    def __init__(self,file):
        '''(str) -> NoneType
        creates an object of type Melody
        
        
        >>> test = Melody("tetris.txt")
        >>> len(test)
        >>> len(test.notes)
        40
        
        >>> test1 = Melody("fur_elise.txt")
        >>> len(test1.notes)
        165
        
        >>> test1.author
        'Ludwig van Beethoven'
        
        >>> test2 = Melody("twinkle.txt")
        >>> len(test2.notes)
        42
        >>> test2.title
        'Twinkle Twinkle Little Star'
        
        
        '''
        
        
        fcon = open(file, "r")
        counter = 1
        self.title = ''
        self.author = ''
        self.notes = []
        repeat=[]
        double = []
        firstt = True

        for i in fcon:
            temp = []
            if counter == 1:
                self.title = i.strip()
      
            elif counter == 2:
                self.author = i.strip()
        

            else:
                temp = i.split()

                if temp[1]== "R":
                    if temp[2] == 'true':
                        if firstt:
                            double.append(note.Note(float(temp[0]), temp[1]))
                            repeat.append(note.Note(float(temp[0]), temp[1]))
                            firstt = False
                            continue

                        elif not firstt:
                            repeat.append(note.Note(float(temp[0]), temp[1]))
                            double.append(note.Note(float(temp[0]), temp[1]))
                            self.notes += repeat
                            self.notes += double
                            repeat = []
                            double = []
                            firstt = True
                            continue
                    else:
                        if not firstt:
                            repeat.append(note.Note(float(temp[0]), temp[1]))
                            double.append(note.Note(float(temp[0]), temp[1]))
                            continue

                        else:
                            self.notes.append(note.Note(float(temp[0]), temp[1]))
                            continue


                if temp[4] == 'true':
                    if firstt:
                        double.append(note.Note(float(temp[0]), temp[1], int(temp[2]), temp[3]))
                        repeat.append(note.Note(float(temp[0]), temp[1], int(temp[2]), temp[3]))
                        firstt = False

                    elif not firstt:
                        repeat.append(note.Note(float(temp[0]), temp[1], int(temp[2]), temp[3]))
                        double.append(note.Note(float(temp[0]), temp[1], int(temp[2]), temp[3]))
                        self.notes += repeat
                        self.notes += double
                        repeat = []
                        double = []
                        firstt = True

                elif temp[4] == 'false':
                    if not firstt:
                        repeat.append(note.Note(float(temp[0]), temp[1], int(temp[2]), temp[3]))
                        double.append(note.Note(float(temp[0]), temp[1], int(temp[2]), temp[3]))

                    else:
                        self.notes.append(note.Note(float(temp[0]), temp[1], int(temp[2]), temp[3]))

            counter += 1

    def play(self, player):
        '''(player) -> NoneType

        takes the user's input for a music player object and plays it

        '''
        
        for i in self.notes:
            i.play(player)


    def get_total_duration(self):
        '''() -> float
        returns the duration of the song
        
        
        >>> test = Melody("twinkle.txt")
        >>> test.get_total_duration()
        24.5
        
        >>> test1 = Melody("weasel.txt")
        >>> test1.get_total_duration()
        9.8
        
        >>> test2 = Melody("fur_elise.txt")
        >>> test2.get_total_duration()
        25.799999999999944
                

        '''
        lsduration = []

        for i in self.notes:
            lsduration.append(i.duration)

        return sum(lsduration)

    def lower_octave(self):
        '''() -> bool
        reduces the octave of each note by 1 and returns True if it has been done, and False otherwise

        >>> test = Melody("twinkle.txt")
        >>> test.lower_octave()
        True
        
        >>> test1 = Melody("weasel.txt")
        >>> test1.lower_octave()
        True
        
        >>> test2 = Melody("tetris.txt")
        >>> test2.lower_octave()
        True

        
        '''
        
        for i in self.notes:
            if i.pitch == 'R':
                continue

            elif i.octave - 1 < note.Note.OCTAVE_MIN:
                return False
        
        for i in self.notes:
            if i.pitch == 'R':
                continue
            else:
                i.octave -= 1

        return True
    
    def upper_octave(self):
        '''() -> bool
        increases the octave of each note by 1 and returns True if it has been done, and False otherwise

        >>> test = Melody("twinkle.txt")
        >>> test.upper_octave()
        True
        
        >>> test1 = Melody("tetris.txt")
        >>> test1.upper_octave()
        True
        
        >>> test2 = Melody("weasel.txt")
        >>> test2.upper_octave()
        True
        '''
        
        for i in self.notes:
            if i.pitch == 'R':
                continue
            elif i.octave + 1 > note.Note.OCTAVE_MAX:
                return False

        for i in self.notes:
            if i.pitch == 'R':
                continue
            else:
                i.octave += 1

        return True
    
    def change_tempo(self, multiplier):
        '''(float) -> NoneType
        takes the user's input for a factor, and increases the duration of each note by that factor

        >>> test = Melody("fur_elise.txt")
        >>> test.get_total_duration()
        25.799999999999944
        >>> test.change_tempo(0.5)
        >>> test.get_total_duration()
        12.899999999999972
        
        >>> test1 = Melody("tetris.txt")
        >>> test1.get_total_duration()
        15.5
        >>> test1.change_tempo(0.5)
        >>> test1.get_total_duration()
        7.75
        
        >>> test2 = Melody("weasel.txt")
        >>> test2.get_total_duration()
        9.8
        >>> test2.change_tempo(0.5)
        >>> test2.get_total_duration()
        4.9
        
        
        '''
        for i in self.notes:
            i.duration *= multiplier 

        




        

