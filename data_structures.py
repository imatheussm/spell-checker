class Character:
    """Node of the dictionary tree.
    
    Will contain references to the sons (if any) and the father. The paths are the existing words.
    """
    def __init__(self,character,previous_character=None,next_characters=[]):
        """Class builder.
        
        Parameters
        ----------
        
        Returns
        -------
        """
        self.character = character
        self.previous_character = previous_character
        self.next_characters = next_characters
    
    def __repr__(self):
        """Character representation
        
        Parameters
        ----------
        
        Returns
        -------
        """
        return "<Character object>\n         Character: {}\nPrevious Character: {}\n   Next Characters: {}".format(self.character,
                                                                                                                   self.previous_character,
                                                                                                                   ", ".join(self.next_characters))
    def __eq__(self,other):
        """Checks if two Character objects contain the same characters (and previous and next as well).
        
        In other words: checks if the three attributes (character, previous_character and next_characters) are the same.
        
        Parameters
        ----------
        
        Returns
        -------
        """
        return self.character==other.character and self.previous_character==other.previous_character and self.next_characters==other.next_characters