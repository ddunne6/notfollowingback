from __future__ import division, unicode_literals 
import codecs
from bs4 import BeautifulSoup

f=codecs.open("followerpage.html", 'r', 'utf-8')
document= BeautifulSoup(f.read(), "lxml")
f2=codecs.open("following.html", 'r', 'utf-8')
followingdoc = BeautifulSoup(f2.read(), "lxml")
#print("iniating div finder")
mydivs = document.findAll("a", {"class": "FPmhX notranslate _0imsa"})
#print("div finder complete")

followingtag = followingdoc.findAll("a", {"class": "FPmhX notranslate _0imsa"})

#print("printing divs")
#print(mydivs[0].text)



n=len(mydivs)
n=int(n)
print(n-1, "followers")
i=0

numFollowing = len(followingtag)
numFollowing = int(numFollowing)

follower = [None] * n
following = [None] * numFollowing

print(numFollowing-1, "following")

while (i<n):
    follower[i]=mydivs[i].text
    #print("\t", follower[i])
    following[i] = followingtag[i].text
    #print("\t", following[i])
    i = i + 1

#print("while loop closed")

i=0
j=0
counter=0
real=False

for i in range(numFollowing):
    real=False
    #print(i)
    for j in range(n):
        #print(j)
        if(follower[j] == following[i]):
            #print("Real", following[j])
            real = True
            counter = counter + 1
            break
    if (real==False):
        print(following[i], "is FAKE")
        
print(counter)
print("program complete")