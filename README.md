# FE595_midterm
Midterm Project for FE595
Required Installation: Textblob, nltk, pycountry

## Quick Startup Guide

1.  Packages to install. Easiest way is via pip3

    * textblob

    * nltk

    * pycoountry

2.  Clone/Download this repository.

        git clone https://github.com/j-swamy/FE595_midterm.git
 
3.  Navigate to the place where you downloaded the repo. Go inside that folder and run which will execute the webservice.

        python3 mytextprocessor.py

## Using the text processor service

1.  The text processor webservice can be accessed by making a POST request to the host url with a JSON body containing the "text" tag. The following is an example using curl command in Linux:

        $ curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Read a good book"}' 'http://hostname:8088/analyze?op=sentiment'
        
2.  The operation to be performed on the text body can be specified using any one or more of 4 different operations:

    * _sentiment:_ returns the polarity and subjectivity of the text analyzed.
    
    * _tags:_ returns a list of words and their part of speech tag associated with each word in the text.
    
    * _spelling:_ returns the list of any mis-spelled words and their alternate recommendations.
    
    * _translation:_ returns the English translation of any piece of text that is not originally in English.
    
            $ curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Read a good book"}' 'http://hostname:8088/analyze?op=sentiment&op=spelling'
    
3.  A sample service has been deployed on AWS host:
            
        http://18.218.94.216:8088
    