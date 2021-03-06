#!/usr/bin/env python3
import sys
import click

def vernam(text, key, return_str=False, alphanumerical=False):
    if alphanumerical:  # Set conversion aliases to custom functions using variable 'alphanumerics' rather than unicode points
        alphanumerics = [i for i in "0123456789abcdefghijklmbopqrstuvwxyzABCDEFGHIJKLMBOPQRSTUVWXYZ"]
        to_num = lambda x: alphanumerics.index(x)
        to_char = lambda x: alphanumerics[x]
    else:  # Set conversion aliases to builtins "ord" and "chr" using unicode points
        to_num = ord
        to_char = chr
    
    bintext = [ to_num(x) for x in text ]  # Convet text to integers
    binkey = [ to_num(x) for x in key ]  # Convet key to integers
    
    for i in range( len(bintext) - len(binkey) ):  # Resize key to length of text
        binkey.append( binkey[i] )
    
    vernamed = [ bintext[i] ^ binkey[i] for i in range(len(bintext)) ]  # XOR vernam operation
    result = [to_char(i) for i in vernamed]  # Convert back to text
    
    if return_str:
        return "".join(result)
    
    return result

@click.command()
@click.argument("text")
@click.argument("key")
@click.option('--string/--list', '-s/-l', "return_str", default=False, help="return as string [default: list]")
@click.option('--alphanumerical/--unicode', '-a/-u', "alphanumerical", default=False, help="encode alphanumerically [default: use unicode points]")
def cli(*args, **kwargs): #text, key, return_str, return_long
    click.echo( vernam(*args, **kwargs) )

if __name__ == "__main__":
    pass