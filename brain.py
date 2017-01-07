 from pybrain.datasets.supervised import SupervisedDataSet
 from pybrain.tools.shortcuts import buildNetwork
 from pybrain.supervised.trainers import BackpropTrainer

 if __name__ == "__main__":
    net = buildNetwork(2, 3, 1)
     ds = SupervisedDataSet(2, 1)
     ds.addSample((1,0),(1,))
     ds.addSample((0,1),(1,))
     ds.addSample((0,0),(0,))
     ds.addSample((1,1),(0,))
     trainer = BackpropTrainer(net, ds)
     trainer.train();
     print "\nResult: ", round(net.activate([0,0]))

