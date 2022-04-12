#!/bin/bash
jupyter-book build .
cp -r assets ./_build/html/.
cp -r Lectures/WFuelPerformance/mygif.gif ./_build/html/Lectures/WFuelPerformance/.
cp -r screenshots ./_build/html/.



