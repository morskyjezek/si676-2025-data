This repo includes data and activities to support SI 676,
the networked services course in Fall 2025.

# Course Description

This course provides information professionals with skills to thrive in a networked 
environment. Technical material in the course will be presented in a context that 
emphasizes its relevance to information professionals. A central theme is programmatic 
access to open source systems, allowing information institutions to build services 
beyond their walls. The full course syllabus can be located at <https://docs.google.com/document/d/1gB5DKamJ38Tt_hfXkIC_lHYeia_Gb_IEqrMP3t7ilPQ/edit?usp=sharing>. 

# Learning Goals

These activities were designed with the intent to:

* Gain confidence in using a non-graphical computer interface (i.e., a text-based command interface to work with local files and those on a remote server);
* Understand how to use web-based services to share metadata (i.e., APIs, OAI-PMH);
* Learn about, explain, and gain confidence in using common data encodings for library/archive/museum (LAM) metadata, including JSON and XML;
* Develop a conceptual understanding of linked data concepts and how they are (or can be) applied in a digital collection environment;
* Conceptualize and design metadata transformations, implement using computational tools (i.e., APIs, Python scripts, and OpenRefine) to extract, transform (crosswalk), and ingest metadata for digital library objects;
* Create and implement a metadata application profile for a digital collection;
* Find and use resources for keeping up with rapid developments, standards, and new tools or concepts for managing the networked environment and LAM metadata space.

# Structure of the Repository

There are a few specific folders:

- `collection-site-materials` contains resources that may be useful for working on the course collection site activities
- `data` contains sample files that illustrate various data formats and can be used for demonstrations, including various examples of CSV, JSON, and XML. Many of the notebooks in the `examples` folder use these data files as a source
- `examples` contains Jupyter notebook files (`.ipynb`) that illustrate various activities that will be undertaken during the semester, as illustrated through blocks of script in Python. These are generally divided into samples that illustrate working with particular metadata formats using Python (such as CSV, XML, JSON, and linked data in JSON-LD), major steps of the ETL assignment sequence (specifically parts of the Exract and Transform steps), and working with APIs (specifically illustrated with data interfaces from the Library of Congress and, generically, Omeka S's built-in API)
- `in-class-notes` contains notebooks or other files that document demonstration sor activities understaken in class

## Sources

Some of these lessons are based on previous iterations of
my digital curation courses, 
including iterations in 2018, 2019, 2022, 2023, and 2024. 
The earliest are recorded at [digccur](https://github.com/morskyjezek/digcur).
