# -*- coding: utf-8 -*-

"""Unit tests for xojo module."""

from __future__ import absolute_import
import re
import pytest
from pygments.token import *
from pygments_xojo.xojo import XojoLexer, _FunctionParamsLexer, _DeclareSubLexer

def test_smoke():
    """A basic smoke test."""
    
    assert XojoLexer()

@pytest.mark.parametrize("source", ['x as Ptr)', ')'])
def test_DECLARE_FUNCTION_ARGS(source):
    assert re.search(_DeclareSubLexer.DECLARE_FUNCTION_ARGS, source)



@pytest.mark.parametrize("source, tokens", 
    [
    ('x as Ptr', [
        (Name.Variable, u'x'),
        (Token.Text, u' '),
        (Keyword.Reserved, u'as'),
        (Text, u' '),
        (Name.XojoType, u'Ptr'),
        ]),

    ('x as Ptr, s as String', [
        (Name.Variable, u'x'),
        (Token.Text, u' '),
        (Keyword.Reserved, u'as'),
        (Text, u' '),
        (Name.XojoType, u'Ptr'),
        (Punctuation, u','),
        (Token.Text, u' '),
        (Name.Variable, u's'),
        (Token.Text, u' '),
        (Keyword.Reserved, u'as'),
        (Text, u' '),
        (Name.XojoType, u'String'),        
        ]),
            
    ])
def test_function_params(source, tokens):
    lexer = _FunctionParamsLexer()
    assert [t for t in lexer.get_tokens(source)] == tokens

@pytest.mark.parametrize("source, tokens", [
    ('foo lib "Bar" ()', [
        (Name.Function, u'foo'),
        (Token.Text, u' '),
        (Keyword.Reserved, u'lib'), 
        (Token.Text, u' '),
        (String, u'"Bar"'),     
        (Token.Text, u' '),
        (Punctuation, u'('),
        (Punctuation, u')'),
        ]),
        
    ('setValue lib AppKit.framework selector "setValue" (this as Ptr, value as Integer)', [
        (Name.Function, u'setValue'),
        (Token.Text, u' '),
        (Keyword.Reserved, u'lib'), 
        (Token.Text, u' '),
        (Name, u'AppKit.framework'),     
        (Token.Text, u' '),
        (Keyword, u'selector'),
        (Token.Text, u' '),
        (String, u'"setValue"'), 
        (Token.Text, u' '),
        (Punctuation, u'('),
        (Name.Variable, u'this'),
        (Token.Text, u' '),
        (Keyword.Reserved, u'as'),
        (Text, u' '),
        (Name.XojoType, u'Ptr'),
        (Punctuation, u','),
        (Token.Text, u' '),
        (Name.Variable, u'value'),
        (Token.Text, u' '),
        (Keyword.Reserved, u'as'),
        (Text, u' '),
        (Name.XojoType, u'Integer'),        
        (Punctuation, u')'),
        ]),    
    ])    
def test_declare_sub(source, tokens):
    lexer = _DeclareSubLexer()
    for t in lexer.get_tokens(source):
        print(t)
    assert [t for t in lexer.get_tokens(source)] == tokens

@pytest.mark.parametrize("source, tokens", 
    [
    ('x = 1', [
        (Token.Name.Variable, u'x'),
        (Token.Text, u' '),
        (Token.Operator, u'='),
        (Token.Text, u' '),
        (Token.Literal.Number.Integer, u'1'),
        ]),

    ('declare sub foo lib "Bar" () as String', [
        (Token.Keyword.Reserved, u'declare sub'),
        (Token.Text, u' '),
        (Name.Function, u'foo'),
        (Token.Text, u' '),
        (Keyword.Reserved, u'lib'), 
        (Token.Text, u' '),
        (String, u'"Bar"'),     
        (Token.Text, u' '),
        (Punctuation, u'('),
        (Punctuation, u')'),
        (Token.Text, u' '),
        (Keyword.Reserved, u'as'),
        (Token.Text, u' '),
        (Token.Name.XojoType, u'String'),        
        ]),
            
    ])
def test_lexing(source, tokens):    
    lexer = XojoLexer()
    for t in lexer.get_tokens(source):
        print(t)
    assert [t for t in lexer.get_tokens(source)] == tokens