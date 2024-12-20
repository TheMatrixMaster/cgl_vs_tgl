from tgb.linkproppred.dataset_pyg import PyGLinkPropPredDataset

name = "tgbl-wiki"

dataset = PyGLinkPropPredDataset(name=name, root="datasets")

data = dataset.get_TemporalData()

type(data) #TemporalData object


