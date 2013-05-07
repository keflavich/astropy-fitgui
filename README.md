Fit GUI for astropy.models
--------------------------

To do:

 * generalize to all models (right now only works with 1D gaussian)
 * add sliders or other interactive cursor-based means of adjusting parameters
 * instructions & docs...
 * test for fixed parameters, etc.
 * deal with higher-dimensional models (e.g., WCS fitting - one of the key use cases to replace IRAF's fitcoords)
    * would be nice to show residuals as vector fields in this particular case
 * expose the matplotlib plotting tools within FitGui so that users can modify appearance of plots 
 * allow plotter to be in another window (e.g., for aplpy or pyspeckit, don't
   muck with the plotting tools at all, just provide an interface to fit and
   modify the model)

 * Create GUI-based model builder for initializing, e.g., polynomial models,
   N-gaussian models, etc.
     * currently, not very easy to make a generic model for fitting
