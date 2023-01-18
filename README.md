# Tools for working with Mozilla Common Voice accent data 

TODO: I think I should rename this repo to `cvaccents` or similar - the name I started with is misleading now. 

## Overview and rationale for the tools

The [Mozilla Common Voice project](https://commonvoice.mozilla.org) is the world's largest open source voice data project. From around 2019, data contributors to Common Voice have been able to specify an accent in their Profile data. However, the accents they could select from were constrained to an enumerated list. In early 2022, the Profile user interface was changed to allow data contributors to self-specify accents. 

However, this change presents challenges to ML practitioners and those using accent data for downstream applications. Firstly, the accent data is free text which is comma delimited. However, the contributor-specified accent descriptors may also contain commas, requiring the use of regular expressions to separate accent descriptors accurately. Secondly, because the accent data is contributor-specified, there is no restrictive taxonomy. Contributors may specify accents without the use of a constraining taxonomy - for example "Midwestern United States English", "Midwest", "Midwestern, and "Midwestern United States" all represent the _same_ accent descriptor. This necessitated a set of heuristics to merge identical descriptors. Thirdly, contributors may specify accent descriptors that are compounds. For example, "heavy Cantonese" actually contains two descriptors - "heavy" to indicate accent strength, and "Cantonese" as a geographical regional marker. 

The tools here include: 

* `cvaccents.py` - a set of Python classes to represent `Accent`, `AccentCollection` and `AccentDescriptor`
* `MCV-get-demographic-details-from-dataset-11.ipynb` - a Jupyter notebook that provides a worked example of extracting AccentDescriptor information and applying heuristics with `cyvaccents.py`. The heuristics apply to the English corpus, and could easily be extended for future Mozilla Common voice accent releases, or adapted to apply to one of the other 100+ languages in the Common Voice project. This notebook _also_ creates nodes and edges `JSON` files suitable for data visualisation in network diagrams, [as shown here](https://observablehq.com/@kathyreid/phd-mozilla-cv-accent-relationships). 

TODO: The Jupyter notebook should be renamed to something more user friendly 
TODO: The Jupyter notebook has a lot of "working out" cruft that needs to be removed, but while the paper is being reviewed and revised I might still need it... 

## Accent taxonomy provided for English 

The `MCV-get-demographic-details-from-dataset-11.ipynb` notebook provides the following taxonomy of Accent Descriptors. Practitioners may wish to extend this taxonomy for their own purposes, or may use this taxonomy as a structure with which to assess voice datasets or models for _accent bias_. 

| Taxonomic category | Count | No. of _a priori_ descriptors | Percentage of total |
|---|---|---|---|
| Geographic descriptors | 113 | 16 | 65.32\% |
|   - Supranational region | 15 | 4 | 8.67\% |
|   - Country | 42 | 12 | 24.28\% |
|   - Subnational region | 45 | - | 26.01\% |
|   - }City | 10 | - | 5.78\% |
|   - Other | 1 | - | 0.58\% |
| Register | 17 | - | 9.83\% |
| First or other language marker | 13 | - | 7.51\% |
| Accent strength descriptor | 11 | - | 6.36\% |
| Phonetic descriptors | 5 | - | 2.89\% |
|   - Specific phonetic changes | 3 | - | 1.73\% |
|   - Rhoticity | 1 | - | 0.58\% |
|   - Inflection | 1 | - | 0.58\% |
| Vocal quality descriptor | 7 | - | 4.05\% |
| Mixed or variable accent | 5 | - | 2.89\% |
| Uncertainty marker | 1 | - | 0.58\% |
| Accent effects due to physical change | 1 | - | 0.58\% |

### Instructions for use 

1. [Fork this repo](https://github.com/KathyReid/cv-analysis-for-bias/fork) under your own GitHub username, or clone this repo into your environment with the command: 
`git clone https://github.com/KathyReid/cv-analysis-for-bias`

2. Use your environment's instructions and create a virtual environment. This will be: ```python3 -m venv [directory]``` if you use `pip` but will differ if you use `conda`. 

3. Activate your virtual environment. If you use `pip` this will be: 

```
cd [directory]
source /bin/activate 
``` 

4. Install the required packages. If you use `pip` the commaned is: ```python3 -m pip install -r requirements.txt``` but will differ if you use `conda`. 

5. Launch Jupyter 

```
jupyter notebook 
```
6. You can then use the notebook from within the Jupyter environment. 

## Citing this toolset 

TODO: Put the `.bib` for the paper here when it is published. 
