#!/usr/bin/env python
#encoding: utf-8

#Non-keyword variable length argument

def tuple_var(arg1, arg2='default value', *args):
	print('========================')
	print("Format arg1:", arg1)
	print("Format arg2:", arg2)
	print(args) #tuple
	for i in args:
		print(i)

tuple_var('arg1')
tuple_var('arg2')
tuple_var('arg1', 'arg2')
tuple_var('arg1', 'arg2', 'arg23', 'arg24', 'arg25')
tuple_var('arg1', 'arg2', ('arg23', 'arg24', 'arg25'))
#Keyword variable length argument

def keyword_var(arg1, arg2='default value', **kwargs):
	print('========================================')
	print('Format arg1:', arg1)
	print('Format atg2:', arg2)
	print(kwargs) #dict
	for kw in kwargs:
		print(kw)

	

keyword_var('arg1')
keyword_var('arg2')
keyword_var('arg1', arg23=23, arg24=24, arg25=25)
keyword_var('arg1', 'arg2', arg23=23, arg24=24, arg25=25)
keyword_var('arg1', 'arg2', **{'arg23':23, 'arg24':24, 'arg25':25}) 

#Mixed use

def Mixed_use(*args, arg1='default value', **kwargs): #arg1 must keyword argument
	print('=====================================================')
	print('Format:', args)
	print('Format:', arg1)
	print(kwargs)

Mixed_use('a','b','c',arg23=23, arg24=24, arg25=25)
Mixed_use('a','b','c', arg1=10000, arg23=23, arg24=24, arg25=25)
Mixed_use('a','b','c', arg1=10000, **{'arg23':23, 'arg24':24, 'arg25':25})

def test(a=1, b):
	print(a)
	print(b)

test(100)# default argument must behind non default argument