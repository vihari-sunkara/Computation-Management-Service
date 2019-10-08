# Computation-Management-Service
This project includes two back end servers one for computing math and the other for evaluating string operations. The Computation Management service is a kind of load balancer which splits the load to the appropriate back end server based on the type of computation(i.e., math or string).
The entire code for the back end servers and the load balancer service is written in Python.
The project includes an interface where one can input numbers or string to compute respective computations. The project uses MongoDb as the NOSQL Database to store the computations made by each of the servers.
