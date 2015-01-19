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

