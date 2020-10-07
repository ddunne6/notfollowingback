from __future__ import division, unicode_literals 
import codecs
from bs4 import BeautifulSoup

# INSTRUCTIONS
# All you have to do is create 2 HTML files within this directory 
# 1. Create file 'followerpage.html' and 'followingpage.html'
# 2.    a. On a web browser, navigate to an instagram profile
#       b. Open the followers and keep scrolling down until all followers are loaded
#       c. Press F12 then go to Elements
#       d. Now copy all of the code in Elements into "followerpage.html"
# 3. Repeat step 2 except for following
# 4. On followerpage.html, hit control f and search for a username you know exists from the people in follower list
# 5. Is the a tag class "FPmhX notranslate _0imsa"?
# 6. If so, youre done, run the code!
# 7. If not then copy the class and replace "FPmhX notranslate _0imsa" with your class on line 25 and 28


#Load the HTML documents
f1=codecs.open("followerpage.html", 'r', 'utf-8')
followerdoc= BeautifulSoup(f1.read(), "lxml")
f2=codecs.open("followingpage.html", 'r', 'utf-8')
followingdoc = BeautifulSoup(f2.read(), "lxml")

#Extract the a tags for a specific class which corresponds to usernames
followertag = followerdoc.findAll("a", {"class": "FPmhX notranslate _0imsa"})
followingtag = followingdoc.findAll("a", {"class": "FPmhX notranslate _0imsa"})

numFollowers=len(followertag)
numFollowers=int(numFollowers)

numFollowing = len(followingtag)
numFollowing = int(numFollowing)

follower = [None] * numFollowers
following = [None] * numFollowing

print(numFollowing-1, "following")
print(numFollowers-1, "followers")
i=0

#Save the text part of the tag to lists
while (i<numFollowers):
    follower[i] = followertag[i].text
    following[i] = followingtag[i].text
    i = i + 1

i=0
j=0
real=False

fake = [] #List of people who don't follow you back is stored here
fakeI = 0

#Scans through your followers and following, adds those who don't follow you back to fake[]
for i in range(numFollowing):
    real=False
    for j in range(numFollowers):
        if(follower[j] == following[i]):
            real = True
            break
    if (real==False):
        if(following[i] != None):
            fake.append(following[i])

print()
print("List of people that don't follow you back")

for x in range(len(fake)):
    print("\t",fake[x])

print("program complete, scroll up for full list")