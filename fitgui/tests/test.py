#from fitgui import fitgui
import fitgui
from numpy.random import randn
import numpy as np

x = np.linspace(0,50,100)
y = randn(100) + 10*np.exp(-(x-20)**2/5.)

#fd = fitgui.fit_data(x,y)
fg = fitgui.FitGui(x,y)#,**kwargs)
fg.modelselector.trait_set(selectedname='Gaussian1DModel')
fg._newmodel_fired(fitgui.Gaussian1DModel)
fg.tmodel.model.mean=21
fg.tmodel.model.amplitude=2
fg.tmodel.model.stddev=0.7
fg._fitmodel_fired()
res = fg.edit_traits(kind='livemodal')
