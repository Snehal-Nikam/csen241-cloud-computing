import requests
import time


class ChatBotPerformance:
    def __init__(self, chatbot_url):
        self.chatbotEndpoint = chatbot_url

    def calculate_response_time(self, data, repeat=1):
        totalTime = 0
        for _ in range(repeat):
            startTime = time.time()
            response = requests.post(self.chatbotEndpoint, data=data)
            endTime = time.time()
            totalTime += (endTime - startTime)
            if repeat == 1:
                return endTime - startTime
        return totalTime / repeat

    def start(self):

        # The first request that does not call figlet
        responseTimeA = self.calculate_response_time("name")
        print(f"A. Response time for the first request using no figlet call: {responseTimeA:.4f} seconds")

        # The second request that does not call figlet
        responseTimeB = self.calculate_response_time("name")
        print(f"B. Response time for the second request using no figlet call: {responseTimeB:.4f} seconds")

        # Avg over 10 requests that do not call figlet
        averageResponseTimeC = self.calculate_response_time("What is your name?", repeat=10)
        print(f"C. Average response time over 10 requests using no figlet call: {averageResponseTimeC:.4f} seconds")

        # The first request that calls figlet
        responseTimeD = self.calculate_response_time("figlet for Hello")
        print(f"D. Response time for the first request using with figlet call: {responseTimeD:.4f} seconds")

        # The second request that calls figlet
        responseTimeE = self.calculate_response_time("figlet for Hello")
        print(f"E. Response time for the second request using with figlet call: {responseTimeE:.4f} seconds")

        # The second request that calls figlet following the first request that does not call figlet

        # Measure the first request with no figlet
        self.calculate_response_time("name")

        # The second request with figlet
        responseTimeF = self.calculate_response_time("figlet for Hello")
        print(
            f"F. Response time for the second request using with figlet and after without figlet call: {responseTimeF:.4f} seconds")

        # Avg 10 requests that call figlet
        averageResponseTimeG = self.calculate_response_time("figlet for Hello", repeat=10)
        print(f"G. Average response time over 10 requests using figlet call: {averageResponseTimeG:.4f} seconds")


if __name__ == "__main__":
    # chatbot's endpoint
    endpoint = "http://localhost:8080/function/chat-bot"
    analyzer = ChatBotPerformance(endpoint)
    analyzer.start()

