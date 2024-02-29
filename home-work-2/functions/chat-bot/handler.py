import requests
import datetime
import random

def handle_question(question):
    if "name" in question.lower():
        names = ["Chat Assistant", "Snehal", "Chatbot"]
        return random.choice(["I'm called as {}.".format(names[1]),
                              "I'm your personal {}.".format(names[0]),
                              "I go by the name {}.".format(names[2])])
    elif "current time" in question.lower():
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return random.choice(["The clock shows {}.".format(current_time),
                              "Time now is  {}.".format(current_time),
                              "Current date and time is {}.".format(current_time)])
    elif "figlet for" in question.lower():
        figlet_text = question.split("figlet for")[1].strip()
        figlet_response = invoke_figlet_function(figlet_text)
        return figlet_response
    elif 'figlet' in question.lower():
        start_index = question.lower().find("for ")
        if start_index != -1:
            figlet_text = question.lower()[start_index + 4:].strip()
            if figlet_text:
                return invoke_figlet_function(figlet_text)
            else:
                return "What text would you like me to tranform to the figlet."
        else:
            return "Could you specify the text for the figlet."
    else:
        return ["Sorry, I didn't understand the question."]

def invoke_figlet_function(text):
    # Construct URL to the figlet function deployed in OpenFaaS
    figlet_function_url = "http://10.62.0.4:8080/function/figlet"

    # Make a POST request to the figlet function
    response = requests.post(figlet_function_url, data=text)

    # Return the response from the figlet function
    print(response.text)
    return response.text

def handle(req):
    question = req.strip()
    response = handle_question(question)
    return '\n'.join(response)


#if __name__ == "__main__":
#    print(invoke_figlet_function("HELLO"))
