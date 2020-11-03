# Arbitrage Opportunites
This repository is my take on the arbitrage problem using the Bellman-Ford algorithm in Python.

* In order to get the currencies, I used https://www.exchangerate-api.com/. It was the website with the most currencies available and there was a free option for me to use. 
* The main algorithm I used was the Bellman-Ford algorithm which is able to detect negative weight cycles. The algorithm can be used with this problem since we can use the negative logarithmm of each exchange rate and then detect negative weight cycles.

---
## Note
This code can be optimized a whole lot, there are a lot of unnecessary lines and loops that can be removed. Moreover, I still need to write error codes for when errors might occur. I would also like to add user input which is not an option with this code. Finally, the biggest issue is determining the path of the cycles. I have tried multiple ways but this is the only way I could find, I am sure there is a better way to find the path of the cycles. Also, I think that my implementation does not find all cycles in the graph, but only one which is an issue to be fixed. 
