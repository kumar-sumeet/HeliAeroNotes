#!/bin/bash
jupyter-book build .
cp -r assets ./_build/html/.
cp -r screenshots ./_build/html/.

