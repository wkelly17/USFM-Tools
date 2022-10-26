import codecs
import logging
import pathlib

from usfm_tools.support.abstractRenderer import AbstractRenderer
from usfm_tools.support.books import bookKeyForIdValue
from usfm_tools.support.parseUsfm import (
    UsfmToken,
    HToken,
    TOC2Token,
    MTToken,
    MT2Token,
    MT3Token,
    MSToken,
    MS2Token,
    PToken,
    PIToken,
    MToken,
    SToken,
    S2Token,
    S3Token,
    CToken,
    VToken,
    WJSToken,
    WJEToken,
    TEXTToken,
    QToken,
    Q1Token,
    Q2Token,
    Q3Token,
    NBToken,
    BToken,
    IDToken,
    ISToken,
    IEToken,
    NDSToken,
    NDEToken,
    PBRToken,
    SCSToken,
    SCEToken,
    FSToken,
    FTToken,
    FEToken,
    FPToken,
    QSSToken,
    QSEToken,
    # EMSToken,
    # EMEToken,
    # EToken,
    # PBToken,
    # PERIPHToken,
    LIToken,
    LI1Token,
    LI2Token,
    LI3Token,
    S5Token,
    IMT1_Token,
    IMT2_Token,
    IMT3_Token,
    CLToken,
    QRToken,
    FQAToken,
    FQAEToken,
    QAToken,
    QACToken,
    QACEToken,
)


logger = logging.getLogger("usfm_tools")


class SingleHTMLRenderer(AbstractRenderer):
    def __init__(self, filePath: pathlib.Path, outputFilename: str) -> None:
        self.f: codecs.StreamReaderWriter  # output file stream
        self.outputFilename = outputFilename
        self.inputFile: pathlib.Path = filePath
        self.cb = ""  # Current Book
        self.cc = "001"  # Current Chapter
        self.cv = "001"  # Current Verse
        self.indentFlag = False
        self.bookName = ""
        # We need to initialize the localized self.chapterLabel here, which is
        # earlier than the parser gets to it. Why? Before adding this, the
        # first chapter for a non-English language used to
        # print the chapter label in English for the first
        # chapter and subsequent chapters would print the
        # localized chapter label. Now all chapter labels are
        # properly localized.
        with open(self.inputFile, "r") as fin:
            content = fin.read()
            # split is performant:
            # See https://stackoverflow.com/questions/7501609/python-re-split-vs-split
            try:
                self.chapterLabel = content.split("\cl ")[1].split("\n")[0].split()[0]
            except IndexError:  # \cl is apparently not provided by the current language
                # Provide a default chapter label since the USFM
                # didn't provide one, e.g., English language USFM
                # doesn't provide \cl.
                self.chapterLabel = "Chapter"
        self.listItemLevel = 0
        self.footnoteFlag = False
        self.fqaFlag = False
        self.footnotes: dict[str, dict[str, str]] = {}
        self.footnote_id = ""
        self.footnote_num = 1
        self.footnote_text = ""
        self.paragraphOpen = False

    def renderBody(self) -> None:
        self.loadUSFM(self.inputFile)
        self.f = codecs.open(self.outputFilename, "w", "utf_8_sig")
        self.run()
        self.write(self.stopIndent())
        self.write(self.stopLI())
        self.write(self.stopP())
        self.writeFootnotes()
        self.f.close()

    def writeHeader(self) -> None:
        h = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"></meta>
    <title>Bible</title>
    <style media="all" type="text/css">
        .indent-0 {
            margin-left:0em;
            margin-bottom:0em;
            margin-top:0em;
        }
        .indent-1 {
            margin-left:0em;
            margin-bottom:0em;
            margin-top:0em;
        }
        .indent-2 {
            margin-left:1em;
            margin-bottom:0em;
            margin-top:0em;
        }
        .indent-3 {
            margin-left:2em;
            margin-bottom:0em;
            margin-top:0em;
        }
        .c-num {
            color:gray;
        }
        .v-num {
            color:gray;
        }
        .tetragrammaton {
            font-variant: small-caps;
        }
        .footnotes {
            font-size: 0.8em;
        }
        .footnotes-hr {
            width: 90%;
        }
    </style>
</head>
<body>
"""
        self.write(h)

    def writeClosing(self) -> None:
        h = """
        </div>
    </body>
</html>
"""
        self.write(h)

    def startLI(self, level: int = 1) -> str:
        if self.listItemLevel:
            self.stopLI()
        ret = ""
        self.listItemLevel = 0
        while self.listItemLevel < level:
            ret += "<ul>"
            self.listItemLevel += 1
        return ret

    def stopLI(self) -> str:
        ret = ""
        while self.listItemLevel > 0:
            ret += "</ul>"
            self.listItemLevel -= 1
        return ret

    def stopP(self) -> str:
        if self.paragraphOpen:
            self.paragraphOpen = False
            return "\n</p>\n\n"
        return ""

    def escape(self, s: str) -> str:
        return s.replace("~", "&nbsp;")

    def write(self, unicodeString: str) -> None:
        self.f.write(unicodeString.replace("~", " "))

    def writeIndent(self, level: int) -> None:
        if self.indentFlag:
            self.write(
                self.stopIndent()
            )  # always close the last indent before starting a new one
        if level > 0:
            self.indentFlag = True
            self.write(self.stopP())
            self.write('\n<p class="indent-' + str(level) + '">\n')
            self.write(
                "&nbsp;" * (level * 4)
            )  # spaces for PDF since we can't style margin with css

    def stopIndent(self) -> str:
        if self.indentFlag:
            self.indentFlag = False
            return "\n</p>\n"
        else:
            return ""

    def renderID(self, token: IDToken) -> None:
        self.write(self.stopIndent())
        self.write(self.stopLI())
        self.write(self.stopP())
        self.writeFootnotes()
        if self.cb:
            self.write("</div>\n\n")
        self.bookName = ""
        self.cb = bookKeyForIdValue(token.value)
        self.write('<div id="bible-book-' + self.cb + '" class="bible-book-text">\n')

    def renderH(self, token: HToken) -> None:
        self.bookName = token.value
        self.write("<h1>" + self.bookName + "</h1>\n")

    def renderTOC2(self, token: TOC2Token) -> None:
        if not self.bookName:
            self.renderH(HToken(token.value))

    def renderMT(self, token: MTToken) -> None:
        return  # self.write(u'\n\n<h1>' + token.value + u'</h1>') # removed to use TOC2

    def renderMT2(self, token: MT2Token) -> None:
        self.write("\n\n<h2>" + token.value + "</h2>\n")

    def renderMT3(self, token: MT3Token) -> None:
        self.write("\n\n<h2>" + token.value + "</h2>\n")

    def renderMS1(self, token: MSToken) -> None:
        self.write("\n\n<h3>" + token.value + "</h3>\n")

    def renderMS2(self, token: MS2Token) -> None:
        self.write("\n\n<h4>" + token.value + "</h4>\n")

    def renderP(self, token: PToken) -> None:
        self.write(self.stopIndent())
        self.write(self.stopLI())
        self.write(self.stopP())
        self.write("\n\n<p>\n")
        self.paragraphOpen = True

    def renderPI(self, token: PIToken) -> None:
        self.write(self.stopIndent())
        self.write(self.stopLI())
        self.write(self.stopP())
        self.writeIndent(2)

    def renderM(self, token: MToken) -> None:
        self.write(self.stopIndent())
        self.write(self.stopLI())
        self.write(self.stopP())
        self.write("\n\n<p>\n")
        self.paragraphOpen = True

    def renderS1(self, token: SToken) -> None:
        self.write(self.stopIndent())
        self.write(self.stopLI())
        self.write('\n\n<h4 style="text-align:center">' + token.getValue() + "</h4>")

    def renderS2(self, token: S2Token) -> None:
        self.write(self.stopIndent())
        self.write(self.stopLI())
        self.write('\n\n<h5 style="text-align:center">' + token.getValue() + "</h5>")

    def renderS3(self, token: S3Token) -> None:
        self.write(self.stopIndent())
        self.write(self.stopLI())
        self.write('\n\n<h5">' + token.getValue() + "</h5>")

    def renderC(self, token: CToken) -> None:
        self.closeFootnote()
        self.write(self.stopIndent())
        self.write(self.stopLI())
        self.write(self.stopP())
        self.writeFootnotes()
        self.footnote_num = 1
        self.cc = token.value.zfill(3)
        self.write(
            '\n\n<h2 id="{0}-ch-{1}" class="c-num">{2} {3}</h2>'.format(
                self.cb,
                self.cc,
                # At this point in execution self.chapterLabel either includes the word
                # for chapter in the current language being parsed plus the chapter
                # number, e.g., Capítulo 1, or else just the English default chapter
                # label (if the language under consideration does not include the
                # chapter label clause, \cl, in its USFM), 'Chapter'. If the former,
                # then we want only the chapter label used here rather than the chapter
                # label and the chapter number. In the latter case, split()[0] won't
                # change anything and so it is safe to use for either case here.
                self.chapterLabel.split()[0],
                token.value,
            )
        )

    def renderV(self, token: VToken) -> None:
        self.closeFootnote()
        self.cv = token.value.zfill(3)
        self.write(self.stopLI())
        self.write(
            '<span id="{0}-ch-{1}-v-{2}" class="v-num"><sup><b>{3}</b></sup></span>'.format(
                self.cb, self.cc, self.cv, token.value
            )
        )

    def renderWJS(self, token: WJSToken) -> None:
        self.write('<span class="woc">')

    def renderWJE(self, token: WJEToken) -> None:
        self.write("</span>")

    def renderTEXT(self, token: TEXTToken) -> None:
        self.write(" {} ".format(self.escape(token.value)))

    def renderQ(self, token: QToken) -> None:
        self.writeIndent(1)

    def renderQ1(self, token: Q1Token) -> None:
        self.writeIndent(1)

    def renderQ2(self, token: Q2Token) -> None:
        self.writeIndent(2)

    def renderQ3(self, token: Q3Token) -> None:
        self.writeIndent(3)

    def renderNB(self, token: NBToken) -> None:
        self.write(self.stopIndent())

    def renderB(self, token: BToken) -> None:
        self.write(self.stopLI())
        self.write('\n\n<p class="indent-0">&nbsp;</p>')

    def renderIS(self, token: ISToken) -> None:
        self.write("<i>")

    def renderIE(self, token: IEToken) -> None:
        self.write("</i>")

    def renderNDS(self, token: NDSToken) -> None:
        self.write('<span class="tetragrammaton">')

    def renderNDE(self, token: NDEToken) -> None:
        self.write("</span>")

    def renderPBR(self, token: PBRToken) -> None:
        self.write("<br></br>")

    def renderSCS(self, token: SCSToken) -> None:
        self.write("<b>")

    def renderSCE(self, token: SCEToken) -> None:
        self.write("</b>")

    def renderFS(self, token: FSToken) -> None:
        self.closeFootnote()
        self.footnote_id = "fn-{0}-{1}-{2}-{3}".format(
            self.cb, self.cc, self.cv, self.footnote_num
        )
        self.write(
            '<span id="ref-{0}"><sup><i>[<a href="#{0}">{1}</a>]</i></sup></span>'.format(
                self.footnote_id, self.footnote_num
            )
        )
        self.footnoteFlag = True
        text = token.value
        if text.startswith("+ "):
            text = text[2:]
        elif text.startswith("+"):
            text = text[1:]
        self.footnote_text = text

    def renderFT(self, token: FTToken) -> None:
        self.footnote_text += token.value

    def renderFE(self, token: FEToken) -> None:
        self.closeFootnote()

    def renderFP(self, token: FPToken) -> None:
        self.write("<br />")

    def renderQSS(self, token: QSSToken) -> None:
        self.write('<i class="quote selah" style="float:right;">')

    def renderQSE(self, token: QSEToken) -> None:
        self.write("</i>")

    def renderLI(self, token: LIToken) -> None:
        self.renderLI1(LI1Token(token.value))

    def renderLI1(self, token: LI1Token) -> None:
        self.write(self.startLI(1))

    def renderLI2(self, token: LI2Token) -> None:
        self.write(self.startLI(2))

    def renderLI3(self, token: LI3Token) -> None:
        self.write(self.startLI(3))

    def renderS5(self, token: S5Token) -> None:
        self.write('\n<span class="chunk-break"></span>\n')

    def render_imt1(self, token: IMT1_Token) -> None:
        self.write("\n\n<h2>" + token.value + "</h2>")

    def render_imt2(self, token: IMT2_Token) -> None:
        self.write("\n\n<h3>" + token.value + "</h3>")

    def render_imt3(self, token: IMT3_Token) -> None:
        self.write("\n\n<h4>" + token.value + "</h4>")

    def renderCL(self, token: CLToken) -> None:
        # Produces: 'Capitulo 1' for example.
        logger.debug("token.value: {}".format(token.value))
        self.chapterLabel = token.value

    def renderQR(self, token: QRToken) -> None:
        self.write(
            '<i class="quote right" style="display:block;float:right;">'
            + token.value
            + "</i>"
        )

    def renderFQA(self, token: FQAToken) -> None:
        self.footnote_text += "<i>" + token.value
        self.fqaFlag = True

    def renderFQAE(self, token: FQAEToken) -> None:
        if self.fqaFlag:
            self.footnote_text += "</i>" + token.value
        self.fqaFlag = False

    def closeFootnote(self) -> None:
        if self.footnoteFlag:
            self.footnoteFlag = False
            self.renderFQAE(FQAEToken(""))
            self.footnotes[self.footnote_id] = {
                "text": self.footnote_text,
                "book": self.cb,
                "chapter": self.cc,
                "verse": self.cv,
                "footnote": str(self.footnote_num),
            }
            self.footnote_num += 1
            self.footnote_text = ""
            self.footnote_id = ""

    def writeFootnotes(self) -> None:
        fkeys = list(self.footnotes.keys())
        if len(fkeys) > 0:
            self.write('<div class="footnotes">')
            self.write('<hr class="footnotes-hr"/>')
            for fkey in sorted(fkeys):
                footnote = self.footnotes[fkey]
                self.write(
                    '<div id="{0}" class="footnote">{1}:{2} <sup><i>[<a href="#ref-{0}">{3}</a>]</i></sup><span class="text">{4}</span></div>'.format(
                        fkey,
                        footnote["chapter"].lstrip("0"),
                        footnote["verse"].lstrip("0"),
                        # footnote["chapter"],
                        # footnote["verse"],
                        footnote["footnote"],
                        footnote["text"],
                    )
                )
            self.write("</div>")
        self.footnotes = {}

    def renderQA(self, token: QAToken) -> None:
        self.write(
            '<p class="quote acrostic heading" style="text-align:center;text-style:italic;">'
            + token.value
            + "</p>"
        )

    def renderQAC(self, token: QACToken) -> None:
        self.write('<i class="quote acrostic character">')

    def renderQACE(self, token: QACEToken) -> None:
        self.write("</i>")
