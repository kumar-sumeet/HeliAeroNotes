#!/usr/bin/env python
# coding: utf-8

# # Dynamic Inflow

# The lack of ability to model transient wake i.e. $v_i(t)$, sets the stage for introducing dynamic inflow theory. Note that this only gets us $v_i$, i.e. it is a wake theory. The blade aerodynamics needs to be modelled separately but, as we shall see, the dynamic inflow models that'll be discussed put no restriction on the blade models used. The blade could be undergoing highly non-linear aerodynamics - for e.g. dynamic stall - and the blade model could be coupled with the dynamic inflow model and still be valid within the purview of dynamic inflow modelling.

# The flow velocity normal to the rotor disk i.e. $v_i$ is modelled as given by the Eq ...
# 
# 
# 
# 

# In[ ]:





# In[ ]:





# Refs. - P116_1, P127

# 

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
# Euler eq.
# 
# 

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
# ```{figure} ../screenshots/11_DynamicInflow/T16_1.png
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

# ## Pitt-Peters inflow model

# Look into the below
# ```{figure} ../assets/T16_3.png 
# ```
# ```{figure} ../assets/T16_4.png 
# ```

# 

# ## Peters-He inflow model
# 
# sdfd

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 
