import requests
import itertools

from math import log

#My choice of currencies to look at.
CURRENCIES = ('AED', 'ARS', 'AUD', 'BGN', 'BRL', 'BSD', 'CAD', 'CHF', 'CLP', 'CNY', 'COP', 'CZK', 'DKK',  'DOP', 'EGP', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'MVR', 'MXN', 'MYR', 'NOK', 'NZD', 'RUB', 'SAR', 'SEK', 'SGD', 'THB', 'TRY', 'TWD', 'UAH', 'USD', 'UYU', 'ZAR')
cycles = []

#Graph Class that uses edge list implementation.
class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = []

	def add_edge(self, u, v, w):
		self.graph.append([u, v, w])

	def print_graph(self):
		print

#Reads currency exchange values from a free API by www.exchangerate-api.com into the graph.
def getCurrencies(graph, currencies):
	url = 'https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/'
	i = 0
	j = 0

	for currency in currencies:
		response = requests.get(url+currency)
		if (response.status_code != 200): #I do not think that this does anything.
			print("Request failed for this currency: %s" % currency)
			break 
		for currency2 in currencies:
			graph.add_edge(i, j, response.json().get('conversion_rates').get(currency2))
			j += 1
		i += 1
		j = 0
	return graph

#Takes the negative logarithm of every weight.
def negativeLog(graph):
	for weight in graph.graph:
		weight[2] = -1 * log(weight[2])
		
	return graph

#Bellman-Ford Algorithm to find arbitrage opportunites.
def arbitrage(graph, currencies):
	dist = [float('inf')] * graph.V
	prev = [-1] * graph.V

	dist [0] = 0

	for	i in range(graph.V - 1):
		for u, v, w in graph.graph:
			if dist[u] != float('inf') and dist[u] + w < dist[v]:
				dist[v] = dist[u] + w
				prev[v] = u

	for u, v, w in graph.graph:
		if dist[u] != float('inf') and dist[u] + w < dist[v]:
			cycle = [v]
			while prev[v] not in cycle:
				cycle.append(prev[v])
				v = prev[v]
			cycle.append(prev[v])
			cycles.append(cycle)	

#Eliminates any identical cycles from all cycles
def eliminateSimilarCycles(possibleCycles):
	tempCycles = []
	for cycle in possibleCycles:
		if cycle[0] == cycle[len(cycle) - 1]:
			tempCycles.append(cycle)
	tempCycles.sort()
	actualCycles = list(tempCycles for tempCycles,_ in itertools.groupby(tempCycles))

	return actualCycles

#Prints the cycles.
def printCycles(allCycles, currencies):
	for cycle in allCycles: 
		print("-->".join([currencies[p] for p in cycle[::-1]]))


#Main
if __name__ == '__main__':
	graph = Graph(len(CURRENCIES))
	graph = getCurrencies(graph, CURRENCIES)
	graph = negativeLog(graph)
	arbitrage(graph, CURRENCIES)
	cycles = eliminateSimilarCycles(cycles)
	printCycles(cycles, CURRENCIES)

