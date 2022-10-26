import pathlib

from usfm_tools.support.books import loadBook, silNames
from usfm_tools.support.parseUsfm import (
    parseString,
    UsfmToken,
    IDToken,
    IDEToken,
    STSToken,
    HToken,
    MToken,
    TOC1Token,
    TOC2Token,
    TOC3Token,
    MTToken,
    MT2Token,
    MT3Token,
    MSToken,
    MS2Token,
    MRToken,
    MIToken,
    PToken,
    SPToken,
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
    QTSToken,
    QTEToken,
    RToken,
    FSToken,
    FEToken,
    FRToken,
    FREToken,
    FKToken,
    FTToken,
    FQToken,
    FPToken,
    ISToken,
    IEToken,
    NDSToken,
    NDEToken,
    PBRToken,
    DToken,
    REMToken,
    PIToken,
    PI2Token,
    LIToken,
    XSToken,
    XEToken,
    XOToken,
    XTToken,
    XDCSToken,
    XDCEToken,
    TLSToken,
    TLEToken,
    ADDSToken,
    ADDEToken,
    IS1_Token,
    IMT1_Token,
    IMT2_Token,
    IMT3_Token,
    IP_Token,
    IOT_Token,
    IO1_Token,
    IO2_Token,
    IOR_S_Token,
    IOR_E_Token,
    BK_S_Token,
    BK_E_Token,
    SCSToken,
    SCEToken,
    BDSToken,
    BDEToken,
    BDITSToken,
    BDITEToken,
)


class AbstractRenderer(object):

    booksUsfm: dict[str, str]

    chapterLabel = ""

    def writeLog(self, s: str) -> None:
        pass

    def loadUSFM(self, filePath: pathlib.Path) -> None:
        self.booksUsfm = loadBook(filePath)

    def run(self) -> None:
        self.unknowns: list[str] = []
        try:
            for bookName in self.booksUsfm:
                self.writeLog("     (" + bookName + ")")
                tokens = parseString(self.booksUsfm[bookName])
                for t in tokens:
                    t.renderOn(self)
        except:
            for bookName in silNames:
                if bookName in self.booksUsfm:
                    self.writeLog("     (" + bookName + ")")
                    tokens = parseString(self.booksUsfm[bookName])
                    for t in tokens:
                        t.renderOn(self)
        if len(self.unknowns):
            print("Skipped unknown tokens: {0}".format(", ".join(set(self.unknowns))))

    def renderID(self, token: IDToken) -> None:
        pass

    def renderIDE(self, token: IDEToken) -> None:
        pass

    def renderSTS(self, token: STSToken) -> None:
        pass

    def renderH(self, token: HToken) -> None:
        pass

    def renderM(self, token: MToken) -> None:
        pass

    def renderTOC1(self, token: TOC1Token) -> None:
        pass

    def renderTOC2(self, token: TOC2Token) -> None:
        pass

    def renderTOC3(self, token: TOC3Token) -> None:
        pass

    def renderMT(self, token: MTToken) -> None:
        pass

    def renderMT2(self, token: MT2Token) -> None:
        pass

    def renderMT3(self, token: MT3Token) -> None:
        pass

    def renderMS(self, token: MSToken) -> None:
        pass

    def renderMS2(self, token: MS2Token) -> None:
        pass

    def renderMR(self, token: MRToken) -> None:
        pass

    def renderMI(self, token: MIToken) -> None:
        pass

    def renderP(self, token: PToken) -> None:
        pass

    def renderSP(self, token: SPToken) -> None:
        pass

    def renderS(self, token: SToken) -> None:
        pass

    def renderS2(self, token: S2Token) -> None:
        pass

    def renderS3(self, token: S3Token) -> None:
        pass

    def renderC(self, token: CToken) -> None:
        pass

    def renderV(self, token: VToken) -> None:
        pass

    def renderWJS(self, token: WJSToken) -> None:
        pass

    def renderWJE(self, token: WJEToken) -> None:
        pass

    def renderTEXT(self, token: TEXTToken) -> None:
        pass

    def renderQ(self, token: QToken) -> None:
        pass

    def renderQ1(self, token: Q1Token) -> None:
        pass

    def renderQ2(self, token: Q2Token) -> None:
        pass

    def renderQ3(self, token: Q3Token) -> None:
        pass

    def renderNB(self, token: NBToken) -> None:
        pass

    def renderB(self, token: BToken) -> None:
        pass

    def renderQTS(self, token: QTSToken) -> None:
        pass

    def renderQTE(self, token: QTEToken) -> None:
        pass

    def renderR(self, token: RToken) -> None:
        pass

    def renderFS(self, token: FSToken) -> None:
        pass

    def renderFE(self, token: FEToken) -> None:
        pass

    def renderFR(self, token: FRToken) -> None:
        pass

    def renderFRE(self, token: FREToken) -> None:
        pass

    def renderFK(self, token: FKToken) -> None:
        pass

    def renderFT(self, token: FTToken) -> None:
        pass

    def renderFQ(self, token: FQToken) -> None:
        pass

    def renderFP(self, token: FPToken) -> None:
        pass

    def renderIS(self, token: ISToken) -> None:
        pass

    def renderIE(self, token: IEToken) -> None:
        pass

    def renderNDS(self, token: NDSToken) -> None:
        pass

    def renderNDE(self, token: NDEToken) -> None:
        pass

    def renderPBR(self, token: PBRToken) -> None:
        pass

    def renderD(self, token: DToken) -> None:
        pass

    def renderREM(self, token: REMToken) -> None:
        pass

    def renderPI(self, token: PIToken) -> None:
        pass

    def renderPI2(self, token: PI2Token) -> None:
        pass

    def renderLI(self, token: LIToken) -> None:
        pass

    def renderXS(self, token: XSToken) -> None:
        pass

    def renderXE(self, token: XEToken) -> None:
        pass

    def renderXO(self, token: XOToken) -> None:
        pass

    def renderXT(self, token: XTToken) -> None:
        pass

    def renderXDCS(self, token: XDCSToken) -> None:
        pass

    def renderXDCE(self, token: XDCEToken) -> None:
        pass

    def renderTLS(self, token: TLSToken) -> None:
        pass

    def renderTLE(self, token: TLEToken) -> None:
        pass

    def renderADDS(self, token: ADDSToken) -> None:
        pass

    def renderADDE(self, token: ADDEToken) -> None:
        pass

    def render_is1(self, token: IS1_Token) -> None:
        pass

    def render_imt1(self, token: IMT1_Token) -> None:
        pass

    def render_imt2(self, token: IMT2_Token) -> None:
        pass

    def render_imt3(self, token: IMT3_Token) -> None:
        pass

    def render_ip(self, token: IP_Token) -> None:
        pass

    def render_iot(self, token: IOT_Token) -> None:
        pass

    def render_io1(self, token: IO1_Token) -> None:
        pass

    def render_io2(self, token: IO2_Token) -> None:
        pass

    def render_ior_s(self, token: IOR_S_Token) -> None:
        pass

    def render_ior_e(self, token: IOR_E_Token) -> None:
        pass

    def render_bk_s(self, token: BK_S_Token) -> None:
        pass

    def render_bk_e(self, token: BK_E_Token) -> None:
        pass

    def renderSCS(self, token: SCSToken) -> None:
        pass

    def renderSCE(self, token: SCEToken) -> None:
        pass

    def renderBDS(self, token: BDSToken) -> None:
        pass

    def renderBDE(self, token: BDEToken) -> None:
        pass

    def renderBDITS(self, token: BDITSToken) -> None:
        pass

    def renderBDITE(self, token: BDITEToken) -> None:
        pass

    # Add unknown tokens to list
    def renderUnknown(self, token: UsfmToken) -> None:
        self.unknowns.append(token.value)
