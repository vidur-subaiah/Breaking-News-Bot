Breaking News Bot (Created by Vidur Subaiah) ==>

A command line program to fetch the top news headlines or search for a particular subject using the OpenNewsAPI (https://newsapi.org/docs/get-started).

Running the program ==>

After downloading the files, obtain your free api key from the link above. Paste your api key in the api_key variable string in the newsapi.py file. To run the program run "python newsapi.py" from your command line. 

In either mode, the top 10 results are presented on the command line following the format below. After printing the output, the program prompts the user if they would like more news (y/n). 

Program developed and tested using Python 3.8. 

Example application flow for identifying top headlines ==>

----

Welcome to Command Line News!   

Please make a choice: [1] Top headlines [2] Search   

>> 1  
  
Select which category would you like to headlines for: 

[1] business   

[2] entertainment   

[3] general   

[4] health   

[5] science   

[6] sports   

[7] technology   
  
>> 7   

* Ikea's First Smart Air Purifier Comes Camouflaged as a Side Table - Gizmodo (August 2, 2021)
         The Starkvind will help you breathe easier while also being easy on the eyes.
         
* Freebie alert: Amazon is giving away eight video games (worth over $130) to all Prime members - Yahoo Lifestyle (August 2, 2021)
         Prime Gaming subscribers can get their hands on hits like 'Battlefield V' and indie sensations like 'A Normal Lost Phone.'

----

Example application flow for a search ==>

----

Welcome to Command Line News! 

Please make a choice: [1] Top headlines [2] Search 

>> 2  
  
Enter your search term:   

>> coronavirus    

* Minnesota universities requiring masks on campuses (August 2, 2021)
         Minnesota's public colleges and universities will require masks to be worn on all campuses as the delta variant of the coronavirus surges, ...

* Schools in US state offer $1,000 bonus to vaccinated staff (August 2, 2021)
         Schools in a county in the southeastern US state of Georgia will pay $1,000 bonuses to staff who are vaccinated against Covid-19 in a bid to protect themselves from the resurgent pandemic, authorities said. With that incentive county officials said they hope …

----

Happy browsing!