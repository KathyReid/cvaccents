# Tools for working with Mozilla Common Voice accent data 

## Overview and rationale for the tools

The [Mozilla Common Voice project](https://commonvoice.mozilla.org) is the world's largest open source voice data project. From around 2019, data contributors to Common Voice have been able to specify an accent in their Profile data. However, the accents they could select from were constrained to an enumerated list. In early 2022, the Profile user interface was changed to allow data contributors to self-specify accents. 

However, this change presents challenges to ML practitioners and those using accent data for downstream applications. Firstly, the accent data is free text which is comma delimited. However, the contributor-specified accent descriptors may also contain commas, requiring the use of regular expressions to separate accent descriptors accurately. Secondly, because the accent data is contributor-specified, there is no restrictive taxonomy. Contributors may specify accents without the use of a constraining taxonomy - for example "Midwestern United States English", "Midwest", "Midwestern, and "Midwestern United States" all represent the _same_ accent descriptor. This necessitated a set of heuristics to merge identical descriptors. Thirdly, contributors may specify accent descriptors that are compounds. For example, "heavy Cantonese" actually contains two descriptors - "heavy" to indicate accent strength, and "Cantonese" as a geographical regional marker. 

The tools here include: 

* `cvaccents.py` - a set of Python classes to represent `Accent`, `AccentCollection` and `AccentDescriptor`
* `cvaccents-v{version}` -  Jupyter notebook that provides a worked example of extracting AccentDescriptor information and applying heuristics with `cyvaccents.py`. This notebook _also_ creates nodes and edges `JSON` files suitable for data visualisation in network diagrams, [as shown here](https://observablehq.com/@kathyreid/phd-mozilla-cv-accent-relationships-v13?collection=@kathyreid/phd-work). 

TODO: The Jupyter notebook should be renamed to something more user friendly 
TODO: The Jupyter notebook has a lot of "working out" cruft that needs to be removed, but while the paper is being reviewed and revised I might still need it... 

## Accent taxonomy provided for English 

The `MCV-get-demographic-details-from-dataset-11.ipynb` notebook provides the following taxonomy of Accent Descriptors. Practitioners may wish to extend this taxonomy for their own purposes, or may use this taxonomy as a structure with which to assess voice datasets or models for _accent bias_. 

| Taxonomic category | 
| Geographic descriptors |
|   - Supranational region ||
|   - Country |
|   - Subnational region |
|   - City | 
|   - Other | 
| Register | 
| First or other language marker | 
| Accent strength descriptor | 
| Phonetic descriptors | 
|   - Specific phonetic changes | 
|   - Rhoticity |
|   - Inflection |
| Vocal quality descriptor | 
| Mixed or variable accent | 
| Uncertainty marker |
| Accent effects due to physical change |

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

```
@Booklet{EasyChair:9678,
  author = {Kathy Reid and Elizabeth T. Williams},
  title = {Common Voice and Accent Choice: Data Contributors Self-Describe Their Spoken Accents in Diverse Ways},
  howpublished = {EasyChair Preprint no. 9678},

  year = {EasyChair, 2023}}

```

[https://easychair.org/publications/preprint/gFLz](https://easychair.org/publications/preprint/gFLz)



## License 

These tools use the Mozilla Public License (MPL) to align with Mozilla's broader ecosystem.
