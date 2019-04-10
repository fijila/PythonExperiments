import re
zenPython = ('''

The Zen of Python, by Tim Peters



Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough to break the rules.

Although practicality beats purity.

Errors should never pass silently.

Unless explicitly silenced.

In the face of ambiguity, refuse the temptation to guess.

There should be one-- and preferably only one --obvious way to do it.

Although that way may not be obvious at first unless you're Dutch.

Now is better than never.

Although never is often better than *right* now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!

''')
words=[]
count=0
words_f=zenPython.split(" ")
words=[x.strip(',') for x in words_f]
words=[x.strip('.') for x in words]
words=[x.strip('-') for x in words]
words=[x.strip('*') for x in words]
words=[x.strip('!') for x in words]
words=[x.strip('' '') for x in words]
words=[x.lower() for x in words]
wordsn=['the','on','off','on','in']
unique_words=set(words)
word_frequency_one = {word:words.count(word) for word in words}
print(word_frequency_one)
freq={k:v for(k,v) in word_frequency_one.items() if v>5}
print(freq)
my_long_string='dsdsds--fdfdfdfd--dsdds'
# m = re.match(r"-- \ --", my_long_string)
match = re.search('--(.*)--',my_long_string)
print (match.group(1))
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
