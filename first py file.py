import re
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import xlsxwriter

#opening a file to store the data
fo = open('bckup.txt','a')

#creating workbook for xlsxwriter
workbook=xlsxwriter.Workbook('data.xlsx')
worksheet=workbook.add_worksheet()
worksheet.write('A1','URL')
worksheet.write('B1','WORD')
worksheet.write('C1','FREQUENCY')

#creating two variables for xlsx (row and col)
wr=1
wc=0

#to plot charts for multiple urls
next_chart=0

#checking if the url is correct
while(True):

    #count for frequency
    count = 0
    
    for x in range(endless):
        #obtaining input from the user
        url = input('Enter the url you want to search in : ')

        #regex to make sure that the url is absolute
        pattern = re.compile('http[s]?://[a-z]{2,4}\.(.+)\.(.{2,4})')
        matchobject = pattern.match(url)

        if (matchobject):

            #writing to the file and xlsx
            fo.writelines(url)
            fo.writelines(' ')

            worksheet.write(wr,wc,url)
            wc+=1
            
            break
        else :
            print('Invalid url address. Please enter absolute url address.')
            print('Example: https://www.google.com/')

            #writing to file
            fo.writelines(url)
            fo.writelines(' ')
            
            continue

    try :
        #converting it into readable form
        holder = urlopen(url)
        soup = bs(holder,'html.parser')

    except :
        print("URL could not be downloaded. Please try a downloadable URL.")
        continue

    else :
            
        #removing script and style tags
        for script in soup('script',{'style':'script'}):
            script.extract()

        #getting text
        text=soup.get_text().strip()
        #print(text)

        text_list=[]
        for i in range(endless):
            #obtaining the words to be searched
            words = input('Enter the word you want to search : ')
            words=words.lower()
            word_list=words.split()

            #writing to file
            fo.writelines(words)
            fo.writelines(' ')

            for wordx in word_list:
                worksheet.write(wr,wc,wordx)
                wc+=1

                #searching for the words in the file
                text_lower = text.lower()
                text_lower = text_lower.split()

                for lowertext in text_lower:
                    if wordx in lowertext:
                        count+=1

                    else :
                        continue

                print(wordx, 'has occurred ', count,' time(s).')

                #writing to file and xlsx
                fo.writelines(wordx)
                fo.writelines(' ')

                worksheet.write(wr,wc,count)
                wr+=1
                wc = 1

                #writing to file
                fo.writelines(str(count))
                fo.writelines(' ')

                #to renew the loop
                count = 0
            
            yn = input("""           If you want to search again in the same url, press 1.
           If you want to change the url and search again, press 2.
           If you want to exit, press 3.
           Enter your wish : """)

            if yn == '1':

                #writing to file
                fo.writelines(yn)
                fo.writelines(' ')
                
                wc=1
                
                continue
            
            else :
                break

        if yn == '2' :

            #count becomes zero
            count=0

            #writing to file
            fo. writelines(yn)
            fo.writelines(' ')

            wc=0
            
            continue

        else :

            #writing to file
            fo. writelines('end\n')

            chart = workbook.add_chart({'type': 'line'})
            chart.set_x_axis({'name': 'Word'})
            chart.set_y_axis({'name': 'Frequency'})
            chart.add_series({
                'categories': '=Sheet1!$B${}:$B${}'.format(2,wr),
                'values': '=Sheet1!$C${}:$C${}'.format(2,wr)
                })
            worksheet.insert_chart('E2', chart)
            
            break

fo.close()
workbook.close()


