# -*- coding: utf-8 -*-
#

import logging
import pathlib
import time

try:
    from books import loadBook, silNames
    from parseUsfm import parseString
except:
    from .books import loadBook, silNames
    from .parseUsfm import parseString

logger = logging.getLogger("usfm_tools")


class AbstractRenderer(object):

    # booksUsfm = None
    booksUsfm: dict

    # FIXME This needs to be localized for non-English languages,
    # however it is used.
    # chapterLabel = "Chapter"
    chapterLabel = ""

    def writeLog(self, s):
        pass

    # def loadUSFM(self, usfmDir):
    def loadUSFM(self, filePath: pathlib.Path) -> None:
        # self.booksUsfm = loadBooks(usfmDir)
        # self.booksUsfm = loadBooks(files)
        logger.info("About to loadBook")
        self.booksUsfm = loadBook(filePath)

    # def loadUSFM(self, files: List[pathlib.Path]) -> None:
    #     # self.booksUsfm = loadBooks(usfmDir)
    #     self.booksUsfm = loadBooks(files)

    def run(self):
        self.unknowns = []
        try:
            # self.renderBook = self.booksUsfm[list(self.booksUsfm.keys())[0]]
            # bookName = self.renderBook  # FIXME renderBook doesn't exist
            for bookName in self.booksUsfm:
                self.writeLog("     (" + bookName + ")")
                # tokens = parseUsfm.parseString(self.booksUsfm[bookName])
                t0 = time.time()
                tokens = parseString(self.booksUsfm[bookName])
                t1 = time.time()
                logger.info("Time for parsing USFM, {}: {}".format(bookName, t1 - t0))
                print("Time for parsing USFM, {}: {}".format(bookName, t1 - t0))
                t0 = time.time()
                for t in tokens:
                    t.renderOn(self)
                t1 = time.time()
                logger.info(
                    "Time for rendering parsed/reified USFM, {}, to output format (e.g., HTML): {}".format(
                        bookName, t1 - t0
                    )
                )
        except:
            for bookName in silNames:
                if bookName in self.booksUsfm:
                    self.writeLog("     (" + bookName + ")")
                    # tokens = parseUsfm.parseString(self.booksUsfm[bookName])
                    t0 = time.time()
                    tokens = parseString(self.booksUsfm[bookName])
                    t1 = time.time()
                    logger.info(
                        "Time for parsing USFM, {}: {}".format(bookName, t1 - t0)
                    )
                    print("Time for parsing USFM, {}: {}".format(bookName, t1 - t0))
                    t0 = time.time()
                    for t in tokens:
                        t.renderOn(self)
                    t1 = time.time()
                    logger.info(
                        "Time for rendering parsed/reified USFM, {}, to output format (e.g., HTML): {}".format(
                            bookName, t1 - t0
                        )
                    )
        if len(self.unknowns):
            print("Skipped unknown tokens: {0}".format(", ".join(set(self.unknowns))))

    def renderID(self, token):
        pass

    def renderIDE(self, token):
        pass

    def renderSTS(self, token):
        pass

    def renderH(self, token):
        pass

    def renderM(self, token):
        pass

    def renderTOC1(self, token):
        pass

    def renderTOC2(self, token):
        pass

    def renderTOC3(self, token):
        pass

    def renderMT(self, token):
        pass

    def renderMT2(self, token):
        pass

    def renderMT3(self, token):
        pass

    def renderMS(self, token):
        pass

    def renderMS2(self, token):
        pass

    def renderMR(self, token):
        pass

    def renderMI(self, token):
        pass

    def renderP(self, token):
        pass

    def renderSP(self, token):
        pass

    def renderS(self, token):
        pass

    def renderS2(self, token):
        pass

    def renderS3(self, token):
        pass

    def renderC(self, token):
        pass

    def renderV(self, token):
        pass

    def renderWJS(self, token):
        pass

    def renderWJE(self, token):
        pass

    def renderTEXT(self, token):
        pass

    def renderQ(self, token):
        pass

    def renderQ1(self, token):
        pass

    def renderQ2(self, token):
        pass

    def renderQ3(self, token):
        pass

    def renderNB(self, token):
        pass

    def renderB(self, token):
        pass

    def renderQTS(self, token):
        pass

    def renderQTE(self, token):
        pass

    def renderR(self, token):
        pass

    def renderFS(self, token):
        pass

    def renderFE(self, token):
        pass

    def renderFR(self, token):
        pass

    def renderFRE(self, token):
        pass

    def renderFK(self, token):
        pass

    def renderFT(self, token):
        pass

    def renderFQ(self, token):
        pass

    def renderFP(self, token):
        pass

    def renderIS(self, token):
        pass

    def renderIE(self, token):
        pass

    def renderNDS(self, token):
        pass

    def renderNDE(self, token):
        pass

    def renderPBR(self, token):
        pass

    def renderD(self, token):
        pass

    def renderREM(self, token):
        pass

    def renderPI(self, token):
        pass

    def renderPI2(self, token):
        pass

    def renderLI(self, token):
        pass

    def renderXS(self, token):
        pass

    def renderXE(self, token):
        pass

    def renderXO(self, token):
        pass

    def renderXT(self, token):
        pass

    def renderXDCS(self, token):
        pass

    def renderXDCE(self, token):
        pass

    def renderTLS(self, token):
        pass

    def renderTLE(self, token):
        pass

    def renderADDS(self, token):
        pass

    def renderADDE(self, token):
        pass

    def render_is1(self, token):
        pass

    def render_imt1(self, token):
        pass

    def render_imt2(self, token):
        pass

    def render_imt3(self, token):
        pass

    def render_ip(self, token):
        pass

    def render_iot(self, token):
        pass

    def render_io1(self, token):
        pass

    def render_io2(self, token):
        pass

    def render_ior_s(self, token):
        pass

    def render_ior_e(self, token):
        pass

    def render_bk_s(self, token):
        pass

    def render_bk_e(self, token):
        pass

    def renderSCS(self, token):
        pass

    def renderSCE(self, token):
        pass

    def renderBDS(self, token):
        pass

    def renderBDE(self, token):
        pass

    def renderBDITS(self, token):
        pass

    def renderBDITE(self, token):
        pass

    # Add unknown tokens to list
    def renderUnknown(self, token):
        self.unknowns.append(token.value)
