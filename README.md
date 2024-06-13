# Courants-Derivants-Cmems

This repo contains 
my Study notebooks on the agestrophic components of currents, for my internship in oceanography.

## Working in your own jupyterlab

4 notebooks and 3 folders are available at present to illustrate:
- Annexe is a folder containing notebooks dealing with our theme but much more improved in the folders CMEMS_notebooks and NOAA_notebooks.
- In the CMEMS_notebooks folder, we have 5 notebooks.
        - Notebook 3 deals with the interpolation of CMEMS data on the spatial and temporal grid of drifting buoys using the linear interpolation method.
        - Notebook 5 deals with the inertial oscillation of drifter velocities.
        - Notebook 7-1 uses Drifter and CMEMS current data to estimate the depth of the Ekman layer and the drag coefficient noted as h_e and r_e respectively.
        - Notebook 7-11 deals with the enhancement of CMEMS currents by adding the Ekman component calculated from NOAA wind data from the product: CoastWatch Caribb-NOAA AOML.
        - Finally, in notebook 7-111, we repeat the same process as in notebook 7-1, this time using CMEMS wind data. 
- [Drifters and currents](1-dériveurs-courants-visualisations.ipynb)  
We visualize the current variables present in our drifter data. These variables are Eastward velocity (ve), Northward velocity (vn), and we also include the visualization of sea surface temperature (SST) present in our data.
- [Dérivants et positions](2-drifters-positions.ipynb) 
We gather all the drifters present in our datasets and provide their positions within our study area for a selected collection date.
- [Interpolation cmems to drifters data](3-interpolation-cmems-drifters.ipynb)
We interpolate the current data from CMEMS to that of the drifters using linear interpolation method.
- [Inertial oscillation](4-oscillation-inertielle-des-dérives.ipynb)
After interpolating CMEMS data onto the drifters, we notice that the period of oscillations is much shorter. The question arises: could this be due to inertial waves? From the frequencies derived from these waves, we conclude that it is indeed the inertial wave because the frequencies obtained are on the order of 10^-5 and 10^-6, which are of the same magnitude as those corresponding to Coriolis forces and thus potentially inertial forces.
- [Oscillation inertielle des drifters et direction du vent](5-oscillation_inertielle_et_vent.ipynb)
This notebook aims to present on a single graph the inertial oscillatory movement of our drifter as well as the direction followed by the wind. Upon visualization, we notice that the wind is directed from the South Pole to the North Pole. This winds are known as polar winds or the southern winds. 
- [Méthodes d'évaluation des courants de surface](Méthodes-de-calcul-des-courants.ipynb)
This notebook aims to detail the methods of calculating ocean currents as presented in the articles by Lagerloef (1999) and Picaut (1990). 




