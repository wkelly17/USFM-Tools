This project comprises a framework for transforming .usfm files into specified targets.

It is primarily used for the Open English Bible, and may need adjustment if used for other purposes.

This fork of USFM-Tools includes basic support for conversion to USX.

# Installation

# Prerequisites

    sudo easy_install pyparsing

# Get code

    git clone https://github.com/kbuildsyourdotcom/USX.git
    cd USX
    python transform.py --setup
 
(This downloads ConTeXt and may take a while.)
 
# Run

    python transform.py --target=usx --usfmDir=./docs/source/ --builtDir=./docs/translation/ --name=MyTranslation

# Production Use
This script will be used in the process of converting USFM text from Etherpad into USX format. The text in Etherpad will first be combined using this script https://github.com/Door43/tools/blob/master/uwb/ep_export.py. The output of the afor mentioned script will then be processed by the script in this repository to transform the USFM to USX. This USX output will at some point become available in the translationStudio api under the Bible translation projects.
