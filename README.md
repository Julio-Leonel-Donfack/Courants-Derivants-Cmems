# Courants-Derivants-Cmems

This repo contains 
my Study notebooks on the agestrophic components of currents, for my internship in oceanography.

## Working in your own jupyterlab

At present, there are 7 notebooks and 1 folder available to illustrate:

- **Annexe Folder**: Contains notebooks pertaining to our theme.
- [Drifters and currents](1-dériveurs-courants-visualisations.ipynb)  
We visualize the current variables present in our drifter data. These variables are Eastward velocity (ve), Northward velocity (vn), and we also include the visualization of sea surface temperature (SST) present in our data.
- [Drifters and positions](2-drifters-positions.ipynb) 
We gather all the drifters present in our datasets and provide their positions within our study area for a selected collection date. We also visualize the trajectory of our drifters and estimate the percentage of those exhibiting inertial oscillation signatures.
- [Drifters and Cmems](3-interpolation-cmems-drifter.ipynb)
Here, we interpolate the CMEMS geostrophic currents on the spatial and temporal grid of the drifters, and calculate study the degree of linkage between the two products.
- [Tracjectoire sur les profils de SSH et SST](4-courant-combine-drifter-plus-cmems.ipynb) 
IThis notebook aims to add the Ekman current components to the geostrophic components. Then, it extracts the inertial current components from drifter data using the spline smoothing filter with the functional approach of Ramsay and Silverman at a 24-hour resolution.
- [Estimation of the initial velocities of inertial components](5-Estimation-of-u0-and-v0.ipynb)
This notebook aims to estimate the initial velocities of our inertial components.
- [drifter SST and SSH](6-Drifter-SSH-SST.ipynb)
This notebook's main purpose is to plot the drifter's trajectory over a SSH (Sea Surface Height) field for the period, then over a SST (Sea Surface Temperature) field. Time series of u (drifter) and ugeos on the same figure. Similarly with v and vgeo.
- [Methods for calculating surface currents](7-Estimation-of-u0-and-v0.ipynb)
This notebook aims to detail the methods for calculating ocean currents as presented in the articles by Lagerloef (1999) and Picaut (1990).




