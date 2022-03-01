#!/usr/bin/env python
# coding: utf-8

# # Momentum Theory

# 

# In[1]:


#bring tiger model and airfoil cross section to class as prop


# 

# 

# ## Airfoils
# 
# - The most efficient lift generation devices - i.e. high lift per unit drag
# -

# ## Breaking down the physics: airfoils 
# 
# - Aerodynamics problems involving airfoil performance can predominantly be understood in terms of Newton's 3rd law of motion.
# - Presence of airfoils in a moving fluid accelerate the flow 
# - The resulting reaction forces manifest as lift and drag on the airfoil
# - 

# ## Breaking down the physics: rotors
# 
# - Rotors are made up of wings (or blades) that have airfoil cross-section
# 

# ## Fundamentals of momentum theory

# ...
# 
# [//]: # (add inflow image and corresponding eqs here)
# 
# $$
#   w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1} \\
#   a_2=b_2+c_2-d_2+e_2  \\
#   a_2=b_2+c_2-d_2+e_2
# $$ (my_label)
# $$
#   a_2=b_2+c_2-d_2+e_2
# $$ (my_other_label)
# 
# [//]: # (  - A link to an equation directive: {eq}`my_label`  ) 
# 
# 
# The flow velocity at the rotor disk, $v_i$, is called induced velocity and is needed for accurate estimation of blade aerodynamics.
# The flow velocity at far downstream, $w$, is relevant for accounting for different rotor wake interaction phenomena - rotor-wing or rotor-fuselage interference effects, brownout, whiteout etc.
# 
# [//]: # (whiteout/brownout videos here??)

# In[ ]:





# 
# ### Assumptions
# 

# - (induced) flow velocity across the rotor disk is continuous
#     - continuity of fluids
# - 
# 
# infinite number of blades on the rotor
# - *induced velocities are small compared to the ??*

# 

# 

# 

# 
# 
# Momentum theory only takes into account the rotor disc area. It does not take into account other rotor geometry parameters - blade twist, taper, chord, sweep angle (forward and back), anhedral/dihedral angle, or aerodynamic parameters - airfoil type.

# ```{figure} ../assets/1_MomentumTheory/propeller.jpg
# ---
# height: 150px
# name: propeller
# ---
# Propeller [source](https://commons.wikimedia.org/wiki/File:Engine_and_propellers_of_aircraft_close_up.jpg)
# ```

# ```{figure} ../assets/1_MomentumTheory/rotor.jpg
# ---
# height: 150px
# name: rotor
# ---
# Helicopter rotor [source](https://en.wikipedia.org/wiki/Sikorsky_UH-60_Black_Hawk#/media/File:ROCA_UH-60M_Black_Hawk.jpg)
# ```

# In[ ]:





# ## Momentum theory: review

#  - does not model rotor torque
#  - it models the most dominant physics exhibited by rotors in steady state operation
#      - in general, it gets the trends from design parametric variations right
#      - hence can be used in preliminary design

# 

# 

# ## Momentum theory: when is the fidelity sufficient?
# 
# * Provides *good* estimate in steady conditions - climb, hover, descent
# * 
# * 

# ## Momentum theory: when is the fidelity not sufficient?
# 
# * Transient conditions - for e.g. maneuvers
# * Does not include aerodynamic limitations of an airfoil
#     * only maps thrust to induced velocity
# * k
# 
# This is where the blade element momentum theory (BEMT) comes in.

# ## Are there better models?
# 
# - some of the most high-fidelity analyses fall within the realm of CFD methods
# 
# - vortex particle methods {cite}`A9_1` or the vorticity transport *(add citation)*
# 
# - dynamic inflow models {cite}`T20,T16,T24`  
# 
# - prescribed wake methods
# 

# Except CFD methods and prescribed wake methods, all of the above are ways to model the rotor wake only i.e. evolution of the flow once it
# has been *disturbed* by the rotor blades (airfoil surfaces). Another model is needed to quantify this *disturbance* so that the wake models above take that as an input and ...

# In[ ]:





# In[ ]:





# 
