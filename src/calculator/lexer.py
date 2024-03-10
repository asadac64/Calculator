"""A simple lexical analyzer."""

# Standard library

# 3rd Party library

# Project library
from calculator.token import Token,TokenType

# ------------------------------------------------------------------------------------------
class Lexer:
    """A simple lexical analyzer."""
    
    def get_number(self, text, pos):
        """Extract numbrt from text starting at pos.
        
        Args:
            text (str): Text to be scanned.
            pos (int): The starting position to scan.
            
        Returns:
            token:      The extracted token
            pos:        The position after the scanning
        """
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme),pos
        
        if not text[pos].isdigit():
            return Token(TokenType.ERROR, lexeme),pos
        
        while pos < length and text[pos].isdigit():
            lexeme = lexeme + text[pos]
            pos = pos + 1
        return Token(TokenType.NUMBER, lexeme),pos
    
    
    
    def get_token(self, text, pos):
        """Extract an addition operator."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme) ,pos
        
        input_text = text[pos]
        if input_text == "+" or text[pos] == "-" :
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.ADD_OP, lexeme),pos

        if input_text == "*" or input_text == "/" or text[pos] == '%':
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.MUL_OP, lexeme),pos
       
        if input_text == "^" :
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.POWER_OP, lexeme),pos
        
        if input_text == "!" :
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.FAC_OP, lexeme),pos

        if input_text == "(" :
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.LEFT_PAREN, lexeme),pos
 
        if input_text == ")" :
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.RIGHT_PAREN, lexeme),pos
        else:
            return Token(TokenType.ERROR, lexeme),pos
        
    def skip_white_space(self, text, pos):
        """Skip all white spaces.

        Args:
            text (str): Text to be scanned.
            pos (int):  The starting position to scan.

        Returns:
            new_pos (int): The position after the last white space.
        """
        length = len(text)
        while pos < length and text[pos].isspace():
            pos += 1
        return pos
    
    def get_token_list(self, text, pos):
        """
        Extract all tokens from the text.

        Args:
            text (str): Text to be scanned.
            pos (int):  The starting position to scan.

        Returns:
            list_of_tokens (list): The list of all tokens.
        """
        list_of_tokens = []
        length = len(text)

        while pos < length:
            pos = self.skip_white_space(text, pos)

            if pos >= length:
                break  

            if text[pos].isdigit():
                token, pos = self.get_number(text, pos)
            else: 
                token, pos = self.get_token(text, pos)

            list_of_tokens.append(token)

        return list_of_tokens
