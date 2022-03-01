#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('html', '', '<style>\n#tum_tower {\n    float: right;\n    margin: 50px;\n}\n#floatleft {\n    float: left; \n    margin: 0 25px 0 0;\n}\n#floatright {\n    float:right;\n}\n.caption {\n    color: grey;\n    font-size: 60%; \n}\n#height_3x3f {  <! –– full screen 3x3 layout ––>\n    height: 280px;\n}\n#height_2x3f {\n    height: 50%;\n\n#height_s {\n    height: 280px;\n}\n#height_m {\n    height: 350px;\n}\n#aligncenter {\n    text-align: center;\n}\n#alignright {\n    text-align: right;\n}\n\n/* First the Grid */\n.gallery-grid {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));\n  grid-gap: 1.5rem;\n  justify-items: center;\n  margin: 0;\n  padding: 0;\n}\n\n/* The Picture Frame */\n.gallery-frame {\n  padding: .5rem;\n  font-size: 1.2rem;\n  text-align: center;\n  background-color: #333;\n  color: #d9d9d9;\n}\n\n/* The Images */\n.gallery-img {\n  max-width: 100%;\n  height: auto;\n  object-fit: cover;\n  transition: opacity 0.25s ease-in-out;\n}\n\n.gallery-img:hover {\n  opacity: .7;\n}\n\n</style>')


# # Rotorcraft Engineering: Preliminary Design
# 
# &nbsp; <!-- extra whitespace -->
# 
# &nbsp;
# 
# <div id="floatright"><img src="assets/tum_pic.png" width="30%" id="tum_tower"/>
# </div>
# 
# <!---<img src="assets/tum_pic.png" width="30%" id="tum_tower"/>  'float right' in the hidden css code at the top. it's the cleanest way to position images -->
# 
# 
# _"We’re living in a changing world.... We need to change how we work as an industry. We can’t get comfortable with our \[high\] barriers to entry, that we can move slowly, that we can create at a slower pace than other industries. We’ve not yet had a Tesla come and rev our engines and show us who we need to be. I’d rather out-innovate myself than wait for someone to show me that."_ 			
# 
# <p id="alignright">
# - MD Helicopters CEO Lynn Tilto, March 2016
# </p>
# 
# <!--- the footer can be edited via Edit > Edit Notebook Metadata -->
# 
# 
# 

# # Purpose of the course
# 
# - Introduce basic physics of rotors
# 
# - ‘Stories’ concerning design and development
# 
# - Rotorcraft community uses a LOT of jargon! 
# 
#   - get a quantitative ‘feel’ of the (non-dimensionalised) parameters <br/>
#     (very important for the exams!!) 
# 

# # Exams and Grading
# 
# - Reading assignments
# 
# - Project
# 
# - Final Exam
# 
# 

# # Helicopters or VTOL (STOVL)
# 
# - The central idea is to take-off and land vertically at BEST EFFICIENCY
# 
# - Which of the below adhere to this principle best? 
# 
#   - why? (hint: large rotor)
#   
# - A century of research has established the conventional design to be the most efficient (for now!) – caveats (weight class, tandem rotors)
# 
# - What about the performance outside this manuever?
# 

# In[2]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('macosx')
im_path = ['assets/spacex.jpeg','assets/carrier.jpg','assets/h160.jpg']
im_attr = ['https://en.wikipedia.org/wiki/SpaceX#/media/File:Falcon_Heavy_Side_Boosters_landing_on_LZ1_and_LZ2_-_2018_(25254688767).jpg',
          'https://en.wikipedia.org/wiki/Harrier_Jump_Jet#/media/File:AV-8B_Harrier_landing_aboard_Principe_de_Asturias_(R11).jpg',
          'https://en.wikipedia.org/wiki/Airbus_Helicopters_H160#/media/File:Airbus_Helicopters_H160_(cropped).jpg']
im_caption = ['SpaceX boosters', 'Harrier jump jet', 'Airbus H160']
rows = 1
cols = 3

f, ax_arr = plt.subplots(rows, cols, figsize=(16,8))

for i, ax in enumerate(ax_arr):
    ax.imshow(plt.imread(im_path[i]))
    ax.axis('off')
    #ax.set_title(f'image {i}')
    ax.annotate("Link", xy=(2,5), xytext=(2.2,5.5),
                    url=im_attr[i], 
                    bbox=dict(color='w', alpha=1e-6, url=im_attr[i]))
    
plt.show() 


# # Helicopters or VTOL (STOVL)
# 
# - The central idea is to take-off and land vertically at BEST EFFICIENCY
# 
# - Which of the below adhere to this principle best? 
# 
#   - why? (hint: large rotor)
#   
# - A century of research has established the conventional design to be the most efficient (for now!) – caveats (weight class, tandem rotors)
# 
# - What about the performance outside this manuever?
# 
# <div class="gallery-grid">
#   <figure class="gallery-frame">
#     <img class="gallery-img" src="assets/spacex.jpeg" alt="Image form https://en.wikipedia.org/wiki/SpaceX#/media/File:Falcon_Heavy_Side_Boosters_landing_on_LZ1_and_LZ2_-_2018_(25254688767).jpg" title="SpaceX">
#     <figcaption>Image Title</figcaption>
#   </figure>
#   <figure class="gallery-frame">
#     <img class="gallery-img" src="assets/spacex.jpeg" alt="Image form https://en.wikipedia.org/wiki/SpaceX#/media/File:Falcon_Heavy_Side_Boosters_landing_on_LZ1_and_LZ2_-_2018_(25254688767).jpg" title="SpaceX">
#     <figcaption>Image Title</figcaption>
#   </figure>
#   <figure class="gallery-frame">
#     <img class="gallery-img" src="assets/spacex.jpeg" alt="Image form https://en.wikipedia.org/wiki/SpaceX#/media/File:Falcon_Heavy_Side_Boosters_landing_on_LZ1_and_LZ2_-_2018_(25254688767).jpg" title="SpaceX">
#     <figcaption>Image Title</figcaption>
#   </figure>
#   <figure class="gallery-frame">
#     <img class="gallery-img" src="assets/spacex.jpeg" alt="Image form https://en.wikipedia.org/wiki/SpaceX#/media/File:Falcon_Heavy_Side_Boosters_landing_on_LZ1_and_LZ2_-_2018_(25254688767).jpg" title="SpaceX">
#     <figcaption>Image Title</figcaption>
#   </figure>
# 
# </div>
# 

# # Helicopters or VTOL (STOVL)
# 
# - The central idea is to take-off and land vertically at BEST EFFICIENCY
# 
# - Which of the below adhere to this principle best? 
# 
#   - why? (hint: large rotor)
#   
# - A century of research has established the conventional design to be the most efficient (for now!) – caveats (weight class, tandem rotors)
# 
# - What about the performance outside this manuever?
# 
# 
# <div id="floatleft"><img src="assets/spacex.jpeg" id="height_2x3f"/>
# <div class="caption">Space X</div></div>
#    
# <div id="floatleft"><img src="assets/carrier.jpg" id="height_2x3f"/>
# <div class="caption">Carrier launch</div></div>
# 
# <div id="floatleft"><img src="assets/h160.jpg" id="height_2x3f"/>
# <div class="caption">H160</div></div>
# 

# # Required power (Bucket) curve
# 
# &nbsp;
# 
# <center>
#     <img src="assets/power_curve.png" width="1200">
# </center>
# 

# # V/STOL aircraft issues<sup>[1]</sup>
# 
# - Large thrust mismatch between vertical flight and cruise 
# 
#   - either engines must be far more oversized for cruise, or that separate thrust devices are needed purely for the vertical flight
# 
# - Distribution of the thrust around the center of gravity for hover
# 
# - Mechanical complexity to facilitate the above
# 
# - Fuel efficiency
# 
#   - powered lift is inherently less efficient form than aerodynamic lift
#   
#   - using more engines and shafts to drive more propulsors decreases efficiencies further
# 

# # Wheel of (Mis)fortune
# 
# <div id="floatright"><img src="assets/wheel.jpg" width="850"/>
# <div class="caption">AHS wheel</div></div>
# 
# 
# <!--- this list next to a float doesn't wrap in slideshow view for some reason 
# possible to insert manual breaks, or use regular text without bullets-->
# 
# - Most V/STOVL aircraft never <br>
#   entered production stage
#   
# - MANY engineering strategies tried <br>
#   out to make helicopters go fast. <br>
#   Almost all failed.  
#   
# - Some strategies making a comeback 
# 
#   - piston/turboshaft power <br>
#     different from electric!
#     
#   - advances in structures (this <br>
#     also makes the conventional <br>
#     design more lucrative)
# 
# 

# # Things to note (no matter the configuration!!)
# 
# <div id="floatright"><img src="assets/forces.png" width="700"/>
# <div class="caption">Forces</div></div>
# 
# 
# Net force and angular momentum of the aircraft should equal zero
# 	
# Vertical component of thrust = aircraft weight
# 
# Horizontal component of thrust = aircraft drag

# # Designs Galore!
# 
# &nbsp;
# 
# <div id="floatleft"><img src="assets/design_1.jpg" id="height_s"/>
# <div class="caption">Wing</div></div>
# 
# <div id="floatleft"><img src="assets/osprey.png" id="height_s"/>
# <div class="caption">Tilt rotor</div></div>
# 
# <div id="floatleft"><img src="assets/tandem.png" id="height_s"/>
# <div class="caption">Tandem rotor</div></div>
# 
# <div id="floatleft"><img src="assets/intermeshing.png" id="height_s"/>
# <div class="caption">Intermeshing rotor</div></div>
# 
# <div id="floatleft"><img src="assets/concept_1.png" id="height_s"/>
# <div class="caption">Concept</div></div>
# 
# <div id="floatleft"><img src="assets/concept_2.png" id="height_s"/>
# <div class="caption">Concept</div></div>
# 
# <div id="floatleft"><img src="assets/concept_3.png" id="height_s"/>
# <div class="caption">Concept</div></div>
# 
# <div id="floatleft"><img src="assets/x3.png" id="height_s"/>
# <div class="caption">Thrust compound</div></div>

# # Conventional
# 
# - The most hover efficient machines.
# 
# - Tail-rotor consumes about 10% power but generates (almost) no vertical or horizontal thrust
# 
# - It helps make this design very responsive directionally (unlike coax, syncropter, tandem designs)
# 
# <!--- video embed in markdown is impossible, so code blocks are used, here with the splitview extension -->
# 
# &nbsp;
# 
# <div id="floatleft"><img src="assets/Bo105.jpeg" id="height_s"/>
# <div class="caption">Bo105</div></div>
# 
# <div id="floatleft"><img src="assets/AH64D.jpeg" id="height_s"/>
# <div class="caption">AH-64D</div></div>
# 

# In[3]:


from IPython.display import YouTubeVideo
YouTubeVideo('Elh0IM7Zp2U', width=500, height=270)


# In[4]:


YouTubeVideo('lslarZiRJhg', width=500, height=270)


# In[5]:


YouTubeVideo('RODMMX3SOBs', width=500, height=270)


# # The tail-rotor conundrum
# 
# - Getting rid of the tail-rotor (somehow) seems the most obvious solution
#   - so no wastage engine power (or is there?)
# 
# - Whenever more than one rotor is involved, the configuration needs to be evaluated VERY CAREFULLY with regard to interactions between the rotors (throughout the flight regime of the rotorcraft!!)
# 
# - Single rotor design is (almost) IMPOSSIBLE!!! 
# 
# - Ingenious ways of placing the second rotor give rise to different configurations
# 
# - Loss in directional control 

# # Tandem
# 
# - Lack of a strong directional stability makes this design relatively insensitive to wind direction landing on a ship (or maneuvering in gusty environment)
# 
# 
# <div><img src="assets/boeing_mh-47g.png" width="900px"/>
# <div class="caption">Boeing MH-47G</div></div>
# 

# &nbsp;
# 
# <div><img src="assets/tandem_2.jpg" width="600px"/>
# <div class="caption">Tandem</div></div>

# In[6]:


from IPython.display import YouTubeVideo
YouTubeVideo('Z2IMTOamZSU?t=70', width=500, height=270)


# # Syncropter
# 
# - Compact design but larger ground clearance needed (cannot approach from the side)
# 
# - No tail rotor but neither rotor generates lift entirely vertically
# 
# - Compensation of yaw directional control using large stabilizers

# In[7]:


from IPython.display import YouTubeVideo
YouTubeVideo('lOgsrRQ0OaQ', width=700, height=400)


# In[8]:


YouTubeVideo('yHcrvO5ZkNI', width=700, height=400)


# # Coaxial
# 
# - Save on swirl losses (but this is low for pretty low for low disk loading rotors anyways)
# 
# - Rotor separation must be low (otherwise lower rotor in climb)
# 
# - Compensation of yaw directional control using large stabilizers
# 
# &nbsp;
# 
# <div id="floatleft"><img src="assets/coaxial_1.jpg" id="height_m"/>
# <div class="caption">Coaxial 1</div></div>
# 
# <div id="floatleft"><img src="assets/coaxial_2.png" id="height_m"/>
# <div class="caption">Coaxial 2</div></div>

# # Compound
# 
# - Rotor in edge-wise flight is not as efficient as a wing (powered vs aerodynamic lift)
# 
# - X-49-like single rotor design with swivelling wings is (THE ONLY?) one possibility of having a single rotor design
# 
#   - _if that is indeed practical is a different question_
#   
# &nbsp;
# 
# &nbsp;
# 
# &nbsp;
# 

# In[9]:


from IPython.display import YouTubeVideo
YouTubeVideo('WGNW-nDw86Q', width=500, height=270)


# In[10]:


YouTubeVideo('_rEfVuwDGaA', width=500, height=270)


# In[11]:


YouTubeVideo('D7fWDOfOcWU', width=500, height=270)


# # Tilt-rotor
# 
# <!--- a 2x3 grid of images and video embeds is difficult. Youtube video object do not have a layout attribute, and can therefore not be used in an IPython display grid. After some trouble, the best workaround seems to be splitview -->
# 
# &nbsp;
# 
# <div id="floatleft"><img src="assets/tilt_1.jpg"  id="height_s"/>
# <div class="caption">Forward flight</div></div>
# 
# <div id="floatleft"><img src="assets/tilt_2.png" id="height_s"/>
# <div class="caption">Multimission Tiltrotor</div></div>
# 
# <div id="floatleft"><img src="assets/tilt_3.jpg" id="height_s"/>
# <div class="caption">Hover flight</div></div>
# 

# In[12]:


from IPython.display import YouTubeVideo

YouTubeVideo('3k8vLetx2ps', width=500, height=270)


# In[13]:


YouTubeVideo('YKC1HzcWZ5s', width=500, height=270)


# In[14]:


YouTubeVideo('VJ6nCpBLHJE', width=500, height=270)


# # eVTOLs
# 
# _“architecture… based on principle and not precendent”_ – (structural architect) Santiago Calvatra
# 
# &nbsp;
# 
# <div id="floatleft"><img src="assets/evtol_1.png"  id="height_s"/>
# <div class="caption">eVTOL 1</div></div>
# 
# <div id="floatleft"><img src="assets/evtol_2.png" id="height_s"/>
# <div class="caption">eVTOL 2</div></div>
# 
# <div id="floatleft"><img src="assets/evtol_3.png" id="height_s"/>
# <div class="caption">eVTOL 3</div></div>
# 
# <div id="floatleft"><img src="assets/evtol_4.png" id="height_s"/>
# <div class="caption">eVTOL 4</div></div>

# # Electric/Hybrid VTOLs<sup>[1]</sup>
# 
# - Obviate need for mechanical power transmission
# 
#   - _Electrical wiring is much lighter than shafts!!_
# 
# - Electric motors can operate at any RPM (unlike Turboshafts)
# 
# &nbsp;
# 
# &nbsp;
# 
# &nbsp;

# In[15]:


from IPython.display import YouTubeVideo

YouTubeVideo('4wbFw165ar0', width=500, height=270)


# In[16]:


YouTubeVideo('0idI3sJJKZw', width=500, height=270)


# In[17]:


YouTubeVideo('gbn0Bnt3iDs', width=500, height=270)

