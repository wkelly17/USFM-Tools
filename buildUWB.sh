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
USFMSRC=/tmp/UWB-USFM
#USFMSRC=/tmp/UWB-1book
#USFMSRC=/tmp/UWB-1

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

NAME="UWB-$LANG-v$VER-`date +%F`"
USFMPUBDIR="/tmp/UWB-$LANG-v$VER"

# Must run before PDF build below
python transform.py --target=context    --usfmDir=$USFMSRC --builtDir=$USFMPUBDIR --name=$NAME

# Build PDF
echo '     Building PDF..'
. ./support/thirdparty/context/tex/setuptex
rm $USFMPUBDIR/working/tex-working/*
cd "$USFMPUBDIR/working/tex-working"
context ../tex/bible.tex
cp "$USFMPUBDIR/working/tex-working/bible.pdf" "$USFMPUBDIR/$NAME.pdf"

python transform.py --target=md         --usfmDir=$USFMSRC --builtDir=$USFMPUBDIR --name=$NAME
python transform.py --target=html       --usfmDir=$USFMSRC --builtDir=$USFMPUBDIR --name=$NAME
python transform.py --target=singlehtml --usfmDir=$USFMSRC --builtDir=$USFMPUBDIR --name=$NAME
python transform.py --target=reader     --usfmDir=$USFMSRC --builtDir=$USFMPUBDIR --name=$NAME
python transform.py --target=csv        --usfmDir=$USFMSRC --builtDir=$USFMPUBDIR --name=$NAME
python transform.py --target=ascii      --usfmDir=$USFMSRC --builtDir=$USFMPUBDIR --name=$NAME

echo "See $USFMPUBDIR"
