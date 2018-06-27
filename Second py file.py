from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

url_set_temp = input('Enter the the websites you want to search in with a space in between them : ')
url_set = url_set_temp.split()
#print(url_set)

#removing empty spaces in the url_set
for x in url_set:
    if ' ' in x:
        url_set.pop()
#print(url_set)

#Using urlopen to download the websites and store it in the list called holder, then using beautiful soup to beautify the layout of it and store it in the list called
#soup. Both done using one for loop and temporary variables called holder_temp and soup_temp
holder=[]
soup=[]
i=0
for x in range(len(url_set)):
    holder_temp=urlopen(url_set[x])
    holder.append(holder_temp)
    soup_temp=bs(holder_temp,'html.parser')
    soup.append(soup_temp)
#print(soup)

#removing the script and style tags from soup
for s in range(len(soup)):
    for script in soup[s](["script","stlye"]):
        script.extract()
#print(soup)

#to get only text from the downloaded pages and storing it into the list called soup_str
soup_str=[]
for i in range(len(soup)):
    text=soup[i].get_text()
    text=text.lower()
    text=text.strip()
    soup_str.append(text)
#print(soup_str)

#creating a ditionary called soup_dict to pair the name of the website with the content of the website and adding to the dictionary using comprehension
soup_dict=dict()
soup_dict={url_set[x]:soup_str[x] for x in range(len(soup_str))}
#print(soup_dict)

#splitting all the words of soup_str in the dictionary with the spaces inbetween the words. It would result a group of lists wihtin a list
for url in range(len(url_set)):
    soup_dict[url_set[url]]=soup_dict[url_set[url]].split()

#obtaining the input of user to check for occurrance in the dicionary
user_input=input('Enter the words you want to search with a space inbetween: ')
user_input = user_input.lower()
user_input=user_input.split(' ')
#print(user_input)

#finding the frequecy for the user input words in each website
count=0
for url in url_set:
    for x in soup_dict[url]:
        for uInput in user_input:
            if uInput in x:
                    count+=1
            else :
                    continue
    print('In',url)
    print(uInput,':',count)
    count=0
        
            




    
