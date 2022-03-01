# What do I need?

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png" width="128px" align="left" margin="16px" />

We'll use the [**Python**](https://en.wikipedia.org/wiki/Python_(programming_language)) programming language throughout the book.
Python has consistently ranked in the top ten most popular programming languages in the [TIOBE Programming Community Index](https://en.wikipedia.org/wiki/TIOBE_index) since the early 2000s.
While [**MATLAB**](https://en.wikipedia.org/wiki/MATLAB) has long been the *de facto* language to introduce students to scientific computing, universities and Academia all around the world have been transitionning to Python during the past ten years.
This transition is being made possible thanks to the open-source nature of Python as well as to the continued development of its rich ecosystem for scientific computing, **NumPy** and **SciPy** being the workhorses.
Some of the tips and tricks presented in this book will thus be useful only to Python programmers.
Yet, the philosophy remains the same and might be applicable to some extent to other languages such as [**R**](https://en.wikipedia.org/wiki/R_(programming_language)) or [**Julia**](https://en.wikipedia.org/wiki/Julia_(programming_language)).


<img src="https://upload.wikimedia.org/wikipedia/en/c/cd/Anaconda_Logo.png" width="192px" align="right" margin="16px" />

Although we'll only make use of standard Python packages such as NumPy, SciPy or Matplotlib, we strongly advice the reader to install Python using [**Anaconda**](https://www.anaconda.com/products/individual).
It is available for all major operating systems, whether it is Windows, MacOS or Linux and will come with all of the standard Python packages you may possibly need.
It also ships some of the tools from [**Project Jupyter**](https://jupyter.org/).
The most important one is probably the **Jupyter Notebooks**.
We make extensive use of these to ensure some form of interactive learning.
If you are unfamiliar with Jupyter Notebooks, there are plenty of tutorials available on the Internet.
Google is your friend!

</br>

<center>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/1280px-NumPy_logo_2020.svg.png" width="256px">
    <img src="https://docs.scipy.org/doc/scipy/reference/_static/scipyshiny_small.png" width="128px">
    <img src="https://upload.wikimedia.org/wikipedia/fr/thumb/3/37/Logo_Matplotlib.svg/1280px-Logo_Matplotlib.svg.png" width="384px">
</center>

</br>

The scientific computing ecosystem for Python is fairly rich, with packages dedicated to astronomy ([**AstroPy**](https://www.astropy.org/)), symbolic computation ([**SymPy**](https://www.sympy.org/en/index.html)), graph theory and complex networks ([**NetworkX**](https://networkx.org/)), image processing ([**scikit-image**](https://scikit-image.org/)) or machine learning ([**scikit-learn**](https://scikit-learn.org/stable/)) to name just a few.
Yet, the three main players anybody interested in scientific computing needs to know are [**NumPy**](https://numpy.org/), [**SciPy**](https://www.scipy.org/) and [**Matplotlib**](https://matplotlib.org/).
- **NumPy:** It is THE fundamental package for scientific computing in Python.
It provides  a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.
- **SciPy:** It is a free and open-source Python library used for scientific computing and technical computing.
SciPy contains modules for optimization, linear algebra, integration, interpolation, special functions, FFT, signal and image processing, ODE solvers and other tasks common in science and engineering. 
To some extent, SciPy can be seen as an extension of NumPy under steroids.
- **Matplotlib:** It is the most popular plotting library for the Python programming language and its numerical mathematics extension NumPy.
Matplotlib is designed to be as usable as MATLAB, with the ability to use Python, and the advantage of being free and open-source. 

These are the three main packages we'll use throughout the book and we expect the reader to be somewhat familiar with them.
Although a quick tour of NumPy will be given in **Chapter 1**, we strongly advice readers unfamiliar with it to go through the excellent book [**From Python to NumPy**](https://www.labri.fr/perso/nrougier/from-python-to-numpy/) by Nicolas Rougier, as well as his [**NumPy Tutorial**](https://github.com/rougier/numpy-tutorial).
Numerous other resources are freely available online but, from the author's point of view, these are probably some of the best.
Regarding Matplotlib, Nicolas Rougier (once again) has an excellent introductory tutorial ([here](https://github.com/rougier/matplotlib-tutorial)).
The [tutorials](https://matplotlib.org/stable/tutorials/index.html) and [gallery](https://matplotlib.org/stable/gallery/index.html) pages of the Matplotlib website also are good resources to see what can be done in Matplotlib and to get familiar with its syntax.
Finally, the [SciPy Lectures Notes](https://scipy-lectures.org/) are a good starting point to start to learn SciPy if needed.
