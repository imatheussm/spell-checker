class Character:
    """Node of the dictionary tree.
    
    Will contain references to the sons (if any) and the father. The paths are the existing words.
    """
    def __init__(self,character,previous_character=None,*args):
        """Class builder.
        
        Parameters
        ----------
        self : Character
            A Character object.
        character : str, int
            The character to be incapsulated into a Character object. If an integer is provided, it will be automatically converted into a Character.
        previous_character : Character (default = None)
            The parent "Node". A TypeError Exception will be raised if an object of another type is provided.
        *args : str, int
            All remaining parameters eventually provided will be interpreted as next_characters (sons), will be incapsulated into Characters if needed and appended as sons of the current character..
        Returns
        -------
        Character
            A Character object.
        """
        if isinstance(character,int) or isinstance(character,Character): character=str(character)
        if not isinstance(character,str) or len(character) != 1: raise ValueError("A Character object can hold only one character.")
        self.character = character
        if previous_character != None and not isinstance(previous_character,Character): raise TypeError("The previous character must be a Character object as well.")
        else: self.previous_character = previous_character
        self.next_characters = sorted([Character(arg) for arg in args if isinstance(arg,str) and len(arg)==1])
    
    def __repr__(self):
        """Character representation.

        Shows the character held by the Character class, as well as the previous one (parent) and next one (children).
        
        Parameters
        ----------
        self : Character
            A Character object.

        Returns
        -------
        str
            The representation of the Character object, containing the aforementioned characteristics.
        """
        return "<Character object>\n         Character: {}\nPrevious Character: {}\n   Next Characters: {}".format(self.character,
                                                                                                                   self.previous_character,
                                                                                                                   ", ".join([character.character for character in self.next_characters]))

    def __eq__(self,other):
        """Checks if two Character objects contain the same characters (and previous and next as well).
        
        In other words: checks if the three attributes (character, previous_character and next_characters) are the same.
        
        Parameters
        ----------
        self : Character
            A Character object, which will be the reference of the comparison.
        other : Character
            Another Character object against which the comparison will be made.

        Returns
        -------
        bool
            The result of the comparison.
        """
        return self.character == other.character and self.previous_character == other.previous_character and self.next_characters == other.next_characters

    def __gt__(self,other):
        """Compares the characters incapsulated in the Character classes, disregarding the previous and next ones.

        Parameters
        ----------
        self : Character
            A Character object, which will be the reference of the comparison.
        other : Character
            Another Character object against which the comparison will be made.

        Returns
        -------
        bool
            The result of the comparison.

        Examples
        --------
        This example takes advantage of this (__gt__()) method.
        >"a" > "b"
        False
        >Character("a") > Character("b")
        False

        This one takes advantage of the __lt__() method.
        >"a" < "b"
        True
        >Character("a") < Character("b")
        True
        """
        return self.character > other.character

    def __lt__(self,other):
        """Compares the characters incapsulated in the Character classes, disregarding the previous and next ones.

        Parameters
        ----------
        self : Character
            A Character object, which will be the reference of the comparison.
        other : Character
            Another Character object against which the comparison will be made.

        Returns
        -------
        bool
            The result of the comparison.

        Examples
        --------
        This example takes advantage of the __gt__() method.
        >"a" > "b"
        False
        >Character("a") > Character("b")
        False

        This one takes advantage of this (__lt__()) method.
        >"a" < "b"
        True
        >Character("a") < Character("b")
        True
        """
        return self.character < other.character

    def __str__(self):
        """Converts the character into a string, omitting previous and next ones.
        
        Parameters
        ----------
        self : Character
            A Character object.
        
        Returns
        -------
        str
            The string representation of the Character object, which simply is the self.character attribute.
        """
        return str(self.character)

