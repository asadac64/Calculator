"""Test cases for lexical analyzer"""

# Standard library

# 3rd Party library
from typing import Literal
import pytest

# Project library
from calculator.token import Token,TokenType
from calculator.lexer import Lexer

#---------------------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text, pos, expected_token,expected_pos",
    [
        ("456",0,Token(TokenType.NUMBER, "456"),3),
        ("705",1,Token(TokenType.NUMBER, "05"),3),
        ("+",0,Token(TokenType.ERROR, ""),0),
    ]
)
def test_get_number(text: Literal['456', '705', '+'],pos: Literal[0, 1],expected_token: Token,expected_pos: Literal[3, 0]):
    """Extract number from text starting at pos"""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_number(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    
#___________________________________________________________
@pytest.mark.parametrize(
    "text, pos, expected_token,expected_pos",
    [
        ("456",0,Token(TokenType.ERROR, ""),0),
        ("705",1,Token(TokenType.ERROR, ""),1),
        ("+",0,Token(TokenType.ADD_OP, "+"),1),
        ("+-",1,Token(TokenType.ADD_OP, "-"),2),
    ]
)
def test_get_add_op(text: Literal['456', '705', '+', '+-'],pos: Literal[0, 1],expected_token: Token,expected_pos: Literal[0, 1, 2]):
    """Extract an addition operator from text starting at pos"""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_token(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    
#___________________________________________________________
@pytest.mark.parametrize(
    "text, pos, expected_token,expected_pos",
    [
        ("456",0,Token(TokenType.ERROR, ""),0),
        ("705",1,Token(TokenType.ERROR, ""),1),
        ("*",0,Token(TokenType.MUL_OP, "*"),1),
       ("/",0,Token(TokenType.MUL_OP, "/"),1),
       ("%",0,Token(TokenType.MUL_OP, "%"),1),
       

    ]
)
def test_get_mul_op(text: Literal['456', '705', '*', '/', '%', '*/', '/%'],pos: Literal[0, 1],expected_token: Token,expected_pos: Literal[0, 1, 2]):
    """Extract an addition operator from text starting at pos"""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_token(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    
#______________________________________________________________________________________________________
@pytest.mark.parametrize(
    "text, pos, expected_token,expected_pos",
    [
        ("456",0,Token(TokenType.ERROR, ""),0),
        ("705",1,Token(TokenType.ERROR, ""),1),
        ("^",0,Token(TokenType.POWER_OP, "^"),1),
        ("^",1,Token(TokenType.EMPTY, ""),1),
       

    ]
)
def test_get_power_op(text: Literal['456', '705', '^'],pos: Literal[0, 1],expected_token: Token,expected_pos: Literal[0, 1]):
    """Extract an addition operator from text starting at pos"""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_token(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    
    
#______________________________________________________________________________________________________
@pytest.mark.parametrize(
    "text, pos, expected_token,expected_pos",
    [
        ("456",0,Token(TokenType.ERROR, ""),0),
        ("705",1,Token(TokenType.ERROR, ""),1),
        ("!",0,Token(TokenType.FAC_OP, "!"),1),
        ("!",1,Token(TokenType.EMPTY, ""),1),
       

    ]
)
def test_get_fac_op(text: Literal['456', '705', '!'],pos: Literal[0, 1],expected_token: Token,expected_pos: Literal[0, 1]):
    """Extract an addition operator from text starting at pos"""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_token(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos    
    
    
#___________________________________________________________
@pytest.mark.parametrize(
    "text, pos, expected_token,expected_pos",
    [
        ("456",0,Token(TokenType.ERROR, ""),0),
        ("705",1,Token(TokenType.ERROR, ""),1),
        ("(",0,Token(TokenType.LEFT_PAREN, "("),1),
        
    ]
)
def test_get_left_paren(text: Literal['456', '705', '+', '+-'],pos: Literal[0, 1],expected_token: Token,expected_pos: Literal[0, 1, 2]):
    """Extract an addition operator from text starting at pos"""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_token(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    

#___________________________________________________________
@pytest.mark.parametrize(
    "text, pos, expected_token,expected_pos",
    [
        ("456",0,Token(TokenType.ERROR, ""),0),
        ("705",1,Token(TokenType.ERROR, ""),1),
        (")",0,Token(TokenType.RIGHT_PAREN, ")"),1),
        
    ]
)
def test_get_right_paren(text: Literal['456', '705', '+', '+-'],pos: Literal[0, 1],expected_token: Token,expected_pos: Literal[0, 1, 2]):
    """Extract an addition operator from text starting at pos"""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_token(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    
#___________________________________________________________
@pytest.mark.parametrize(
    "text, pos, new_pos",
    [
        (" abc ", 0, 1),
        (" xyz ", 0, 1),
        (" xyz ", 1, 1),
        (" xyz ", 2, 2),
        (" xyz ", 3, 3),
        (" xyz ", 4, 5),
        (" xyz ", 5, 5),
        ("   pqr", 0, 3),
    ]
)
def test_skip_white_space(text,pos,new_pos):
    """Extract an addition operator from text starting at pos"""
    # Arrange
    lexer = Lexer()
    
    # Act
    result = lexer.skip_white_space(text, pos)
    
    # Assert
    assert result == new_pos
    

# -------------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text, pos, expected_tokens",
    [
        ("123 + (32 / 4)",0,[
        Token(TokenType.NUMBER, "123"),
        Token(TokenType.ADD_OP, "+"),
        Token(TokenType.LEFT_PAREN, "("),
        Token(TokenType.NUMBER, "32"),
        Token(TokenType.MUL_OP, "/"),
        Token(TokenType.NUMBER, "4"),
        Token(TokenType.RIGHT_PAREN, ")"),
    ])
    ]
)
def test_get_token_list(text,pos,expected_tokens):
    # Arrange
    lexer = Lexer()
    
    # Act
    result = lexer.get_token_list(text,pos)
    
    # Assert
    assert result == expected_tokens