#!/usr/bin/python3
"""
encoding=utf-8
"""
import io


f = io.open('abc.txt', 'wt', encoding='utf-8')
f.write(u'Imagine a non-english text like wakadinali')
f.close()
text = io.open('abc.txt', encoding='utf-8').read()
print(text)
