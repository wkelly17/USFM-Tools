#!/usr/bin/env bash
# -*- coding: utf8 -*-
#
#  Copyright (c) 2014 unfoldingWord
#  http://creativecommons.org/licenses/MIT/
#  See LICENSE file for details.
#
#  Contributors:
#  Jesse Griffin <jesse@distantshores.org>

PROGNAME="${0##*/}"
EXPORT=0
TOOLS=/var/www/vhosts/door43.org/tools
USFMSRC=/tmp/UTB-USFM
TEX2UP=bible-2up.tex
TEXPDF=bible-pdf.tex

help() {
    echo
    echo "Publish unfoldingWord Bible"
    echo
    echo "Usage:"
    echo "   $PROGNAME -v <version> -l <language> [-e <exportfromd43first>]"
    echo "   $PROGNAME --help"
    echo
    exit 1
}

if [ $# -lt 1 ]; then
    help
fi
while test -n "$1"; do
    case "$1" in
        --help|-h)
            help
            ;;
        --version|-v)
            VER=$2
            shift
            ;;
        --language|-l)
            LANG=$2
            shift
            ;;
        --export|-e)
            EXPORT=1
            shift
            ;;
        *)
            echo "Unknown argument: $1"
            help
            ;;
    esac
    shift
done

if [ $EXPORT -eq 1 ]; then
    echo "Exporting USFM from DokuWiki..."
    $TOOLS/uwb/dw2usfm_assembled.sh
    RET=$?
    if [ $RET -ne 0 ]; then
        echo "--> Export failed, bailing..."
        exit 1
    fi
fi

NAME="UDB-$LANG-v$VER-`date +%F`"
USFMPUBDIR="/tmp/UDB-$LANG-v$VER"

buildPDF () {
    # $1 == source dir, $2 source filename, $3 == output filename
    echo 'Building PDF..'
    . ./support/thirdparty/context/tex/setuptex
    WORKING="$1/working/tex-working/"
    [ -d "$WORKING" ] && rm -rf "$WORKING"
    mkdir -p "$WORKING"
    cd "$WORKING"
    context "../tex/$2"
    cp "$WORKING/${2%%.tex}.pdf" "$1/$3"
    cd -
}

buildMD () {
    # $1 == source dir, $2 source filename, $3 == output filename
    echo "     Building Markdown from $2"
    pandoc +RTS -K128m -RTS -s "$1/$2" -o "$USFMPUBDIR/$3"
}

# Must run before PDF build below
python transform.py --target=context    --usfmDir=$USFMSRC --builtDir=$USFMPUBDIR --name=$NAME
cp -f support/introTeXt-2up.tex "$USFMPUBDIR/working/tex/$TEX2UP"
cp -f support/introTeXt-pdf.tex "$USFMPUBDIR/working/tex/$TEXPDF"
cat  "$USFMPUBDIR/working/tex/bible.tex" >> "$USFMPUBDIR/working/tex/$TEX2UP"
cat  "$USFMPUBDIR/working/tex/bible.tex" >> "$USFMPUBDIR/working/tex/$TEXPDF"
sed -i "s/UTBVERSUB/$VER/" "$USFMPUBDIR/working/tex/$TEX2UP"
sed -i "s/UTBVERSUB/$VER/" "$USFMPUBDIR/working/tex/$TEXPDF"

buildPDF "$USFMPUBDIR" "$TEX2UP" "$NAME-2up.pdf"
#buildPDF "$USFMPUBDIR" "$TEXPDF" "$NAME.pdf"

#buildMD "$USFMPUBDIR" "$TEXPDF" "$NAME.md"
#python transform.py --target=md         --usfmDir=$USFMSRC --builtDir=$USFMPUBDIR --name=$NAME

# maybe pandoc for these formats too?
#python transform.py --target=html       --usfmDir=$USFMSRC --builtDir=$USFMPUBDIR --name=$NAME
#python transform.py --target=singlehtml --usfmDir=$USFMSRC --builtDir=$USFMPUBDIR --name=$NAME
#python transform.py --target=csv        --usfmDir=$USFMSRC --builtDir=$USFMPUBDIR --name=$NAME
#python transform.py --target=ascii      --usfmDir=$USFMSRC --builtDir=$USFMPUBDIR --name=$NAME

###python transform.py --target=reader     --usfmDir=$USFMSRC --builtDir=$USFMPUBDIR --name=$NAME

# Build each book individually
#for 
echo "See $USFMPUBDIR"
