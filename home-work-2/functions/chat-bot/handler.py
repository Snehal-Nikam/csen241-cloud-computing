import requests
import datetime

def handle_question(question):
    if "name" in question.lower():
        return ["You can call me ChatBot."]
    elif "current time" in question.lower():
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return ["Time now is " + current_time]
    elif "figlet for" in question.lower():
        figlet_text = question.split("figlet for")[1].strip()
        figlet_response = invoke_figlet_function(figlet_text)
        return figlet_response
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
