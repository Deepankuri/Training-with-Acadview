#Question1
"""
We have to extract user id, domain name, and suffix from the given
email addresses. We use '\w' which accepts [a-z], [A-Z], and [0-9] 
characters only. So we will get all of them parameters.
""" 
import re
regex_compile1 = re.compile('\w+')
a = "zuck26@facebook.com" 
b = "page33@google.com"
c = "jeff42@amazon.com"
print(regex_compile1.findall(a))
print(regex_compile1.findall(b))
print(regex_compile1.findall(c))

#Question2
"""
Retrieve all the words starting from 'b' and 'B' from the
given text. '\b' will pick up all the words beginning from 'b' 
and ignore case will pick the words from 'B' as well.
"""
import re
regex_compile = re.compile(r'\bb\w+', re.IGNORECASE)
print(regex_compile.findall('Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better'))

#Queston3 
"""
We have to remove all the characters for an irregular sentence.
I have mentioned two ways to do so.
"""

"""
Method1
"""
import re
regex_compile = re.compile('[^_\W]+')
l = regex_compile.findall('A, very very; irregular_sentence')
print(l)
l = [(i.split('\t',1)[0]) for i in l]
print(" ".join(l))

"""
Method2
"""
import re
text = 'A, very very; irregular_sentence'
split = re.split('[;,\s_]+', text)
print(" ".join(split))

#Question4 (optional)
"""
We have to extract the tweet only, removing all the extra symbols
and unneccesary words and punctuations
"""
import re
text = "'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'"
def clean_up(tweet):
	tweet = re.sub('(!)|RT|(@\S+)','', tweet)
	tweet = re.sub('http\S+','', tweet)
	tweet = re.sub('cc\S+','', tweet)
	tweet = re.sub('#\S+','', tweet)
	tweet = (" ".join(re.split('[\s]+', tweet)))
	print(tweet)

clean_up(text)