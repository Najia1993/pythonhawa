file = open("stop-words.txt")
stopwords = file.readlines()

def removeStopwords(message):
 for word in stopwords:
    next = word.strip()
    message = message.replace(" " + next + " "," ")
    return message    

while True:

#greeting------------------------------

    input = raw_input("Hye there, tell me what is your name :  ")
    #input = " " + input.title() + " "
    filtered = removeStopwords(input)
    filtered = filtered.replace("my","")
    filtered = filtered.replace("name","")
    filtered = filtered.replace("is","")
    print("-->> Hye, " + filtered.strip())  

#user ask quetion----------------------
    
    phrase = raw_input(">> ")
    if "" in phrase:
        if "what" in phrase and "name" in phrase:
            print "-->> My name is Kevin, I am your Artificial Intelligent friend"
        elif "from" in phrase:
            print "-->> Im from this computer"
        elif "who" in phrase and "you" in phrase:
            print "-->> Im Kevin, your best friend"
        elif "robot" in phrase:
            print "-->> No, Im not a robot. I am a cat"
        else:
            print "-->> Haha, sorry I don't understand what you want to say"
    
#computer ask questions----------------
    
    input = raw_input("Where are you from: ")
    #input = " " + input.title() + " "
    filtered = removeStopwords(input)
    filtered = filtered.replace("i'm","")
    filtered = filtered.replace("i","")
    filtered = filtered.replace("am","")
    filtered = filtered.replace("from","")
    print("-->>" + filtered.strip() + "?? Beautiful place!!")

    input =raw_input("How is the weather: ")
    filtered = removeStopwords(input)
    filtered = filtered.replace("the","")
    filtered = filtered.replace("weather","")
    filtered = filtered.replace("is","")
    varWeather = filtered
    if varWeather == 'sunny':
        print ("-->> Nice, I love " + filtered.strip() +" day!")
    elif varWeather == 'cold':
        print ("-->> Lovely, I love " + filtered.strip() +" day!")
    elif varWeather == 'cloudy':
        print ("-->> I love " + filtered.strip() +" day")
    else:
        print ("-->> Wow, such a lovely weather")


#user ask quetion----------------------DUNNO WHAT TO WRITE!!!
        
    phrase = raw_input(">> ")
    if "" in phrase:
        if "know" in phrase and "name" in phrase:
            print "-->> My name is Kevin, I am your Artificial Intelligent friend"
        elif "from" in phrase:
            print "-->> Im from this computer"
        elif "who" in phrase and "you" in phrase:
            print "-->> Im Kevin, your best friend"
        elif "robot" in phrase:
            print "-->> No, Im not a robot. I am a cat"
        else:
            print "-->> Sorry I don't understand what you want to say."


        

    input = raw_input("What is your favourite food?")
    input = " " + input.title() + " "
    filtered = removeStopwords(input)
    filtered = filtered.replace(" favourite "," ")
    filtered = filtered.replace(" food "," ")
    filtered = filtered.replace(" love "," ")
    filtered = filtered.replace(" food "," ")
    print("-->> Yummy," + filtered.strip() + ", I wish I could have a taste of it")


    input =raw_input("How does it taste?: ")
    input = " " + input.title() + " "
    filtered = removeStopwords(input)
    filtered = filtered.replace("it","")
    filtered = filtered.replace("taste","")
    filtered = filtered.replace("is","")
    varTaste = filtered
    if varTaste == 'sweet':
        print ("-->> Mmmmm.... I love to eat something sweets")
    elif varTaste == 'spicy':
        print ("-->> You make me salivating and hungry")
    elif varTaste == 'bitter':
        print ("-->> Not good, I don't like bitter food")
    else:
        print ("-->> Sounds delicious, you make me hungry!")


    input =raw_input("Is it your country traditional food?")
    filtered = removeStopwords(input)
    filtered = filtered.replace("it","")
    filtered = filtered.replace("is","")
    varFood = filtered
    x = "-->> I love to eat traditional food. You should cook for me someday"
    y = "-->> You're such a good cook. You can cook so many things"
    if "" in phrase:
        if "yes" in phrase:
            print "-->> I love to eat traditional food. You should cook for me someday"
        else:
            print "-->> You're such a good cook. You can cook so many things"
        
    input = raw_input("Nice chatting with you")
    filtered = removeStopwords(input)
    filtered = filtered.replace("nice","")
    filtered = filtered.replace("chatting","")
    filtered = filtered.replace("too","")
    varWeather = filtered
    if varWeather == 'nice':
        print ("-->> You are lovely")
    else: 
        print ("-->> See ya!")
    
  
    
   

