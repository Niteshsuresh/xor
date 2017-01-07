 from pybrain.datasets import SupervisedDataSet, ClassificationDataSet
 from pybrain.tools.shortcuts import buildNetwork
 from pybrain.supervised.trainers import BackpropTrainer

 if __name__ == "__main__":
   #regression
   #net = buildNetwork(2, 3, 1)
   #ds = SupervisedDataSet(2, 1)
	 
	 #classification
	 net = buildNetwork(12, hidden_nodes, 3, outclass=SoftmaxLayer, hiddenclass=TanhLayer)
     ds = ClassificationDataSet(2, 1, nb_classes=4)
  
  
     ds.addSample((1,0),(1,))
     ds.addSample((0,1),(1,))
     ds.addSample((0,0),(0,))
     ds.addSample((1,1),(0,))
     trainer = BackpropTrainer(net, ds)
     trainer.train();
     print "\nResult: ", round(net.activate([0,0]))