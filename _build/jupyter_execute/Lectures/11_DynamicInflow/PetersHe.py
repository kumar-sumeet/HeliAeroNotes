#!/usr/bin/env python
# coding: utf-8

# # Peters-He Inflow Model

# ## Motivation
# 
# - For what its worth - it is used extensively in control studies

# ## Assumptions
# 
# - Euler equation
# $$
#   a=b
# $$ (euler)
# - Actuator disk assumptions
#     - Flow velocity continuous
#     $$
#       a=b
#     $$ (continuity)
#     - Pressure distribution continuous over the rotor disk, discontinuous across it
#     - Flat rotor disk
# 

# # Fundamental ideas
# 
# - 3D, incompressible, potential flow equations for a rotor with arbitrary blade loadings
# - completely analytical solution, no numerical discretization involved!
# 
# - The result is a set of ordinary differential equations in time for a finite number of
# aerodynamic states that describe the induced flow field at the rotor disk. Thus, the theory
# includes implicitly all effects of shed and trailing vorticity including tip relief, dynamic inflow,
# and conventional Theodorsen/Loewy unsteady aerodynamics. 
# 
# - find a basis of functions that can be superimposed to give inflow
#     - *fidelity varies with number of basis functions included (read somewhere this is not always true)*
# - 

# In[ ]:





# The lack of ability to model transient wake i.e. $v_i(t)$, sets the stage for introducing dynamic inflow theory. Note that this only gets us $v_i$, i.e. it is a wake theory. The blade aerodynamics needs to be modelled separately but, as we shall see, the dynamic inflow models that'll be discussed put no restriction on the blade models used. The blade could be undergoing highly non-linear aerodynamics - for e.g. dynamic stall - and the blade model could be coupled with the dynamic inflow model and still be valid within the purview of dynamic inflow modelling.

# The flow velocity normal to the rotor disk i.e. $v_i$ is modelled as given by the Eq ...
# 
# 
# 
# 

# In[ ]:





# Refs. - P116_1, P127

# 

# Description of the step increase in blade pitch study (bot old and the UT Austin paper)
# 
# figures
# 
# 
# The aerodynamic analysis discussed until now is incapable of predicting the results observed from the above studies. Momentum theory and BEMT based on quasi-steady airfoil aerodynamics. The aerodynamics, as it relates to the above experiments, due to sudden blade pitch changes cannot be modelled as quasi-steady anymore - the approximation fails here. Hence the need for a theory that accounts for the observed transient effects
# 
# 
# 

# 

# # Description
# 
# - When rotor loads change as a function of time, so does the induced velocity
# -
# -
# - Dynamic inflow models help estimate induced velocity as a function of changing rotor loads
# - This is a wake model only!
#     - needs to be coupled with a blade aerodynamics model for rotor aerodynamics analyses

# ## Mathematical form
# 
# T16 says -
# 
# F =ma
# 
# Euler eq. (linearised - small $v_i$ assumption)
# 
# In ellipsoidal coordinates leads to - 
# 
# ```{figure} ../../assets/P116_1.png
# ---
# height: 150px
# name: P116_1
# ---
# ...
# ```
# <!--- the above should be written separately using individual solutions of A2.4.2-A2.3.4 in T16 --->
# - Legendre polynomials properties 
#     - T16 Appendix A2.3-A2.6
# <!--- use Figs 3.8 and 3.9 from T24 here --->
# 
# ```{figure} ../../assets/P116_1-2.png
# ---
# height: 150px
# name: P116_1-2
# ---
# ...
# ```
# <!--- From P116_1, things go in the following order - Eq 2-9, 22-28, 29,  --->

# In[ ]:





# Now that a mathematiccal model exists relating pressure with induced velocity,  
# pressure can in turn be obtained using a suitable blade model.

# ## Characteristics
# 
# - Equations simple in form
#     - 
# - Computationally light 
#     - used in real time flight simulators
# - Heirarchical in nature
#     - increasing number of states improves *accuracy* of the results [^DynInfl1]
#     - literature suggests that this might not always be the case, the blade aero and elastic deformation play a role as well 
#     
# - Extensively used in aeroelastic stability analysis
# - 
# 
# ```{figure} ../../assets/T16_1.png
# ---
# height: 150px
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# [^DynInfl1]: The governing differential equations that the dynamic inflow equations are based on are themselves an approximation of the *true* governing equations (if one assumes the Navier-Stokes equations to the governing fluid equations that result in *exact* solutions). So by increasing the number of states, the dynamic inflow model tends towards the model represented by Eq. ...
# 
# 

# 

# 
