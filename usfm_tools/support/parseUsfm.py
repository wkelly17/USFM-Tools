import sys
from pyparsing import (  # type: ignore
    Word,
    OneOrMore,
    nums,
    Literal,
    White,
    Group,
    Suppress,
    NoMatch,
    Optional,
    CharsNotIn,
    MatchFirst,
    ParseResults,
)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from usfm_tools.support.abstractRenderer import AbstractRenderer
import logging
from typing import Any

logger = logging.getLogger("usfm_tools")


def usfmToken(key: str) -> Group:
    return Group(Suppress(backslash) + Literal(key) + Suppress(White()))


def usfmBackslashToken(key: str) -> Group:
    return Group(Literal(key))


def usfmEndToken(key: str) -> Group:
    return Group(Suppress(backslash) + Literal(key + "*"))


def usfmTokenValue(key: str, value: CharsNotIn) -> Group:
    return Group(
        Suppress(backslash) + Literal(key) + Suppress(White()) + Optional(value)
    )


def usfmTokenNumber(key: str) -> Group:
    return Group(
        Suppress(backslash)
        + Literal(key)
        + Suppress(White())
        + Word(nums + "-()")
        + Suppress(White())
    )


# define grammar
# phrase = Word( alphas + "-.,!? —–‘“”’;:()'\"[]/&%=*…{}" + nums )
phrase = CharsNotIn("\n\\")
backslash = Literal("\\")
plus = Literal("+")

textBlock = Group(Optional(NoMatch(), "text") + phrase)
unknown = Group(
    Optional(NoMatch(), "unknown") + Suppress(backslash) + CharsNotIn(" \n\t\\")
)
escape = usfmTokenValue("\\", phrase)

id_token = usfmTokenValue("id", phrase)
ide = usfmTokenValue("ide", phrase)
sts = usfmTokenValue("sts", phrase)
h = usfmTokenValue("h", phrase)

mt = usfmTokenValue("mt", phrase)
mt1 = usfmTokenValue("mt1", phrase)
mt2 = usfmTokenValue("mt2", phrase)
mt3 = usfmTokenValue("mt3", phrase)
ms = usfmTokenValue("ms", phrase)
ms1 = usfmTokenValue("ms1", phrase)
ms2 = usfmTokenValue("ms2", phrase)
mr = usfmTokenValue("mr", phrase)
s = usfmTokenValue("s", phrase)
s1 = usfmTokenValue("s1", phrase)
s2 = usfmTokenValue("s2", phrase)
s3 = usfmTokenValue("s3", phrase)
s4 = usfmTokenValue("s4", phrase)
s5 = usfmTokenValue("s5", phrase)
r = usfmTokenValue("r", phrase)
p = usfmToken("p")
pi = usfmToken("pi")
pi2 = usfmToken("pi2")
b = usfmToken("b")
c = usfmTokenNumber("c")
cas = usfmToken("ca")
cae = usfmEndToken("ca")
cl = usfmTokenValue("cl", phrase)
v = usfmTokenNumber("v")
wjs = usfmToken("wj")
wje = usfmEndToken("wj")
q = usfmToken("q")
q1 = usfmToken("q1")
q2 = usfmToken("q2")
q3 = usfmToken("q3")
q4 = usfmToken("q4")
qa = usfmTokenValue("qa", phrase)
qac = usfmToken("qac")
qace = usfmEndToken("qac")
qc = usfmToken("qc")
qm = usfmToken("qm")
qm1 = usfmToken("qm1")
qm2 = usfmToken("qm2")
qm3 = usfmToken("qm3")
qr = usfmTokenValue("qr", phrase)
qss = usfmToken("qs")
qse = usfmEndToken("qs")
qts = usfmToken("qt")
qte = usfmEndToken("qt")
nb = usfmToken("nb")
m = usfmToken("m")

# Footnotes
fs = usfmTokenValue("f", plus)
fr = usfmTokenValue("fr", phrase)
fre = usfmEndToken("fr")
fk = usfmTokenValue("fk", phrase)
ft = usfmTokenValue("ft", phrase)
fq = usfmTokenValue("fq", phrase)
fqa = usfmTokenValue("fqa", phrase)
fqae = usfmTokenValue("fqa*", phrase)
fqb = usfmTokenValue("fqb", phrase)
fe = usfmEndToken("f")
fp = usfmToken("fp")

# Cross References
xs = usfmTokenValue("x", plus)
xdcs = usfmToken("xdc")
xdce = usfmEndToken("xdc")
xo = usfmTokenValue("xo", phrase)
xt = usfmTokenValue("xt", phrase)
xe = usfmEndToken("x")

# Transliterated
tls = usfmToken("tl")
tle = usfmEndToken("tl")

# Transliterated
scs = usfmToken("sc")
sce = usfmEndToken("sc")

# Italics
ist = usfmToken("it")
ien = usfmEndToken("it")

# Bold
bds = usfmToken("bd")
bde = usfmEndToken("bd")
bdits = usfmToken("bdit")
bdite = usfmEndToken("bdit")

li = usfmToken("li")
li1 = usfmToken("li1")
li2 = usfmToken("li2")
li3 = usfmToken("li3")
li4 = usfmToken("li4")
d = usfmTokenValue("d", phrase)
sp = usfmToken("sp")
adds = usfmToken("add")
adde = usfmEndToken("add")
nds = usfmToken("nd")
nde = usfmEndToken("nd")
pbr = usfmBackslashToken("\\\\")
mi = usfmToken("mi")

# Comments
rem = usfmTokenValue("rem", phrase)

# Tables
tr = usfmToken("tr")
th1 = usfmToken("th1")
th2 = usfmToken("th2")
th3 = usfmToken("th3")
th4 = usfmToken("th4")
th5 = usfmToken("th5")
th6 = usfmToken("th6")
thr1 = usfmToken("thr1")
thr2 = usfmToken("thr2")
thr3 = usfmToken("thr3")
thr4 = usfmToken("thr4")
thr5 = usfmToken("thr5")
thr6 = usfmToken("thr6")
tc1 = usfmToken("tc1")
tc2 = usfmToken("tc2")
tc3 = usfmToken("tc3")
tc4 = usfmToken("tc4")
tc5 = usfmToken("tc5")
tc6 = usfmToken("tc6")
tcr1 = usfmToken("tcr1")
tcr2 = usfmToken("tcr2")
tcr3 = usfmToken("tcr3")
tcr4 = usfmToken("tcr4")
tcr5 = usfmToken("tcr5")
tcr6 = usfmToken("tcr6")

# Table of Contents
toc = usfmTokenValue("toc", phrase)
toc1 = usfmTokenValue("toc1", phrase)
toc2 = usfmTokenValue("toc2", phrase)
toc3 = usfmTokenValue("toc3", phrase)

# Introductory Materials
is1 = usfmTokenValue("is1", phrase) | usfmTokenValue("is", phrase)
ip = usfmToken("ip")
iot = usfmToken("iot")
io1 = usfmToken("io1") | usfmToken("io")
io2 = usfmToken("io2")
ior_s = usfmToken("ior")
ior_e = usfmEndToken("ior")
imt = usfmTokenValue("imt", phrase)
imt1 = usfmTokenValue("imt1", phrase)
imt2 = usfmTokenValue("imt2", phrase)
imt3 = usfmTokenValue("imt3", phrase)

# Quoted book title
bk_s = usfmToken("bk")
bk_e = usfmEndToken("bk")

element = MatchFirst(
    [
        ide,
        id_token,
        sts,
        h,
        toc,
        toc1,
        toc2,
        toc3,
        mt,
        mt1,
        mt2,
        mt3,
        ms,
        ms1,
        ms2,
        mr,
        s,
        s1,
        s2,
        s3,
        s4,
        s5,
        r,
        pi2,
        pi,
        p,
        mi,
        b,
        c,
        cas,
        cae,
        cl,
        v,
        wjs,
        wje,
        nds,
        nde,
        q,
        q1,
        q2,
        q3,
        q4,
        qa,
        qac,
        qace,
        qc,
        qm,
        qm1,
        qm2,
        qm3,
        qr,
        qss,
        qse,
        qts,
        qte,
        nb,
        m,
        fs,
        fr,
        fre,
        fk,
        ft,
        fq,
        fqa,
        fqae,
        fqb,
        fe,
        fp,
        xs,
        xdcs,
        xdce,
        xo,
        xt,
        xe,
        ist,
        ien,
        bds,
        bde,
        bdits,
        bdite,
        li,
        li1,
        li2,
        li3,
        li4,
        d,
        sp,
        adds,
        adde,
        tls,
        tle,
        is1,
        ip,
        iot,
        io1,
        io2,
        ior_s,
        ior_e,
        imt,
        imt1,
        imt2,
        imt3,
        bk_s,
        bk_e,
        scs,
        sce,
        pbr,
        rem,
        tr,
        th1,
        th2,
        th3,
        th4,
        th5,
        th6,
        thr1,
        thr2,
        thr3,
        thr4,
        thr5,
        thr6,
        tc1,
        tc2,
        tc3,
        tc4,
        tc5,
        tc6,
        tcr1,
        tcr2,
        tcr3,
        tcr4,
        tcr5,
        tcr6,
        textBlock,
        escape,
        unknown,
    ]
)

usfm = OneOrMore(element)


# input string
def parseString(unicodeString: str) -> list[Any]:
    try:
        cleaned = clean(unicodeString)
        tokens = usfm.parseString(cleaned, parseAll=True)
    except Exception as e:
        logger.error(e)
        logger.error(repr(unicodeString[:50]))
        sys.exit()
    return [createToken(t) for t in tokens]


def clean(unicodeString: str) -> str:
    # We need to clean the input a bit. For a start, until
    # we work out what to do, non breaking spaces will be ignored
    # ie 0xa0
    ret_value = unicodeString.replace("\xa0", " ")

    # escape illegal USFM sequences
    ret_value = ret_value.replace("\\ ", "\\\\ ")
    ret_value = ret_value.replace("\\\n", "\\\\\n")
    ret_value = ret_value.replace("\\\r", "\\\\\r")
    ret_value = ret_value.replace("\\\t", "\\\\\t")

    # check edge case if backslash is at end of line
    l = len(ret_value)
    if (l > 0) and (ret_value[l - 1] == "\\"):
        ret_value += "\\"  # escape it

    return ret_value


def createToken(t: ParseResults) -> UsfmToken:
    options = {
        "id": IDToken,
        "ide": IDEToken,
        "sts": STSToken,
        "h": HToken,
        "mt": MTToken,
        "mt1": MTToken,
        "mt2": MT2Token,
        "mt3": MT3Token,
        "ms": MSToken,
        "ms1": MSToken,
        "ms2": MS2Token,
        "mr": MRToken,
        "p": PToken,
        "pi": PIToken,
        "pi2": PI2Token,
        "b": BToken,
        "s": SToken,
        "s1": SToken,
        "s2": S2Token,
        "s3": S3Token,
        "s4": S4Token,
        "s5": S5Token,
        "mi": MIToken,
        "r": RToken,
        "c": CToken,
        "ca": CASToken,
        "ca*": CAEToken,
        "cl": CLToken,
        "v": VToken,
        "wj": WJSToken,
        "wj*": WJEToken,
        "q": QToken,
        "q1": Q1Token,
        "q2": Q2Token,
        "q3": Q3Token,
        "q4": Q4Token,
        "qa": QAToken,
        "qac": QACToken,
        "qac*": QACEToken,
        "qc": QCToken,
        "qm": QMToken,
        "qm1": QM1Token,
        "qm2": QM2Token,
        "qm3": QM3Token,
        "qr": QRToken,
        "qs": QSSToken,
        "qs*": QSEToken,
        "qt": QTSToken,
        "qt*": QTEToken,
        "nb": NBToken,
        "f": FSToken,
        "fr": FRToken,
        "fr*": FREToken,
        "fk": FKToken,
        "ft": FTToken,
        "fq": FQToken,
        "fqa": FQAToken,
        "fqae": FQAEToken,
        "fqa*": FQAEToken,
        "fqb": FQAEToken,
        "f*": FEToken,
        "fp": FPToken,
        "x": XSToken,
        "xdc": XDCSToken,
        "xdc*": XDCEToken,
        "xo": XOToken,
        "xt": XTToken,
        "x*": XEToken,
        "it": ISToken,
        "it*": IEToken,
        "bd": BDSToken,
        "bd*": BDEToken,
        "bdit": BDITSToken,
        "bdit*": BDITEToken,
        "li": LIToken,
        "li1": LI1Token,
        "li2": LI2Token,
        "li3": LI3Token,
        "li4": LI4Token,
        "d": DToken,
        "sp": SPToken,
        "i*": IEToken,
        "add": ADDSToken,
        "add*": ADDEToken,
        "nd": NDSToken,
        "nd*": NDEToken,
        "sc": SCSToken,
        "sc*": SCEToken,
        "m": MToken,
        "tl": TLSToken,
        "tl*": TLEToken,
        "\\\\": EscapedToken,
        "rem": REMToken,
        "tr": TRToken,
        "th1": TH1Token,
        "th2": TH2Token,
        "th3": TH3Token,
        "th4": TH4Token,
        "th5": TH5Token,
        "th6": TH6Token,
        "thr1": THR1Token,
        "thr2": THR2Token,
        "thr3": THR3Token,
        "thr4": THR4Token,
        "thr5": THR5Token,
        "thr6": THR6Token,
        "tc1": TC1Token,
        "tc2": TC2Token,
        "tc3": TC3Token,
        "tc4": TC4Token,
        "tc5": TC5Token,
        "tc6": TC6Token,
        "tcr1": TCR1Token,
        "tcr2": TCR2Token,
        "tcr3": TCR3Token,
        "tcr4": TCR4Token,
        "tcr5": TCR5Token,
        "tcr6": TCR6Token,
        "toc1": TOC1Token,
        "toc2": TOC2Token,
        "toc3": TOC3Token,
        "is": IS1_Token,
        "is1": IS1_Token,
        "imt": IMT1_Token,
        "imt1": IMT1_Token,
        "imt2": IMT2_Token,
        "imt3": IMT3_Token,
        "ip": IP_Token,
        "iot": IOT_Token,
        "io": IO1_Token,
        "io1": IO1_Token,
        "io2": IO2_Token,
        "ior": IOR_S_Token,
        "ior*": IOR_E_Token,
        "bk": BK_S_Token,
        "bk*": BK_E_Token,
        "text": TEXTToken,
        "unknown": UnknownToken,
    }
    for opt_key, opt_val in options.items():
        if t[0] == opt_key:
            if len(t) == 1:
                return opt_val()
            else:
                return opt_val(t[1])
    raise Exception(t[0])


class UsfmToken(object):
    def __init__(self, value: str = "") -> None:
        self.value = value

    def getValue(self) -> str:
        return self.value

    def isUnknown(self) -> bool:
        return False

    def isID(self) -> bool:
        return False

    def isIDE(self) -> bool:
        return False

    def isSTS(self) -> bool:
        return False

    def isH(self) -> bool:
        return False

    def isTOC1(self) -> bool:
        return False

    def isTOC2(self) -> bool:
        return False

    def isTOC3(self) -> bool:
        return False

    def isMT(self) -> bool:
        return False

    def isMT2(self) -> bool:
        return False

    def isMT3(self) -> bool:
        return False

    def isMS(self) -> bool:
        return False

    def isMS2(self) -> bool:
        return False

    def isMR(self) -> bool:
        return False

    def isR(self) -> bool:
        return False

    def isP(self) -> bool:
        return False

    def isPI(self) -> bool:
        return False

    def isPI2(self) -> bool:
        return False

    def isS(self) -> bool:
        return False

    def isS2(self) -> bool:
        return False

    def isS3(self) -> bool:
        return False

    def isS4(self) -> bool:
        return False

    def isS5(self) -> bool:
        return False

    def isMI(self) -> bool:
        return False

    def isC(self) -> bool:
        return False

    def isCAS(self) -> bool:
        return False

    def isCAE(self) -> bool:
        return False

    def isCL(self) -> bool:
        return False

    def isV(self) -> bool:
        return False

    def isWJS(self) -> bool:
        return False

    def isWJE(self) -> bool:
        return False

    def isTEXT(self) -> bool:
        return False

    def isQ(self) -> bool:
        return False

    def isQ1(self) -> bool:
        return False

    def isQ2(self) -> bool:
        return False

    def isQ3(self) -> bool:
        return False

    def isQ4(self) -> bool:
        return False

    def isQA(self) -> bool:
        return False

    def isQAC(self) -> bool:
        return False

    def isQACE(self) -> bool:
        return False

    def isQC(self) -> bool:
        return False

    def isQM(self) -> bool:
        return False

    def isQM1(self) -> bool:
        return False

    def isQM2(self) -> bool:
        return False

    def isQM3(self) -> bool:
        return False

    def isQR(self) -> bool:
        return False

    def isQSS(self) -> bool:
        return False

    def isQSE(self) -> bool:
        return False

    def isQTS(self) -> bool:
        return False

    def isQTE(self) -> bool:
        return False

    def isNB(self) -> bool:
        return False

    def isFS(self) -> bool:
        return False

    def isFR(self) -> bool:
        return False

    def isFRE(self) -> bool:
        return False

    def isFK(self) -> bool:
        return False

    def isFT(self) -> bool:
        return False

    def isFQ(self) -> bool:
        return False

    def isFQA(self) -> bool:
        return False

    def isFQAE(self) -> bool:
        return False

    def isFQB(self) -> bool:
        return False

    def isFE(self) -> bool:
        return False

    def isFP(self) -> bool:
        return False

    def isXS(self) -> bool:
        return False

    def isXDCS(self) -> bool:
        return False

    def isXDCE(self) -> bool:
        return False

    def isXO(self) -> bool:
        return False

    def isXT(self) -> bool:
        return False

    def isXE(self) -> bool:
        return False

    def isIS(self) -> bool:
        return False

    def isIE(self) -> bool:
        return False

    def isSCS(self) -> bool:
        return False

    def isSCE(self) -> bool:
        return False

    def isLI(self) -> bool:
        return False

    def isLI1(self) -> bool:
        return False

    def isLI2(self) -> bool:
        return False

    def isLI3(self) -> bool:
        return False

    def isLI4(self) -> bool:
        return False

    def isD(self) -> bool:
        return False

    def isSP(self) -> bool:
        return False

    def isADDS(self) -> bool:
        return False

    def isADDE(self) -> bool:
        return False

    def isNDS(self) -> bool:
        return False

    def isNDE(self) -> bool:
        return False

    def isTLS(self) -> bool:
        return False

    def isTLE(self) -> bool:
        return False

    def isBDS(self) -> bool:
        return False

    def isBDE(self) -> bool:
        return False

    def isBDITS(self) -> bool:
        return False

    def isBDITE(self) -> bool:
        return False

    def isPBR(self) -> bool:
        return False

    def isM(self) -> bool:
        return False

    def isREM(self) -> bool:
        return False

    def isTR(self) -> bool:
        return False

    def isTH1(self) -> bool:
        return False

    def isTH2(self) -> bool:
        return False

    def isTH3(self) -> bool:
        return False

    def isTH4(self) -> bool:
        return False

    def isTH5(self) -> bool:
        return False

    def isTH6(self) -> bool:
        return False

    def isTHR1(self) -> bool:
        return False

    def isTHR2(self) -> bool:
        return False

    def isTHR3(self) -> bool:
        return False

    def isTHR4(self) -> bool:
        return False

    def isTHR5(self) -> bool:
        return False

    def isTHR6(self) -> bool:
        return False

    def isTC1(self) -> bool:
        return False

    def isTC2(self) -> bool:
        return False

    def isTC3(self) -> bool:
        return False

    def isTC4(self) -> bool:
        return False

    def isTC5(self) -> bool:
        return False

    def isTC6(self) -> bool:
        return False

    def isTCR1(self) -> bool:
        return False

    def isTCR2(self) -> bool:
        return False

    def isTCR3(self) -> bool:
        return False

    def isTCR4(self) -> bool:
        return False

    def isTCR5(self) -> bool:
        return False

    def isTCR6(self) -> bool:
        return False

    def is_toc1(self) -> bool:
        return False

    def is_toc2(self) -> bool:
        return False

    def is_toc3(self) -> bool:
        return False

    def is_is1(self) -> bool:
        return False

    def is_imt1(self) -> bool:
        return False

    def is_imt2(self) -> bool:
        return False

    def is_imt3(self) -> bool:
        return False

    def is_ip(self) -> bool:
        return False

    def is_iot(self) -> bool:
        return False

    def is_io1(self) -> bool:
        return False

    def is_io2(self) -> bool:
        return False

    def is_ior_s(self) -> bool:
        return False

    def is_ior_e(self) -> bool:
        return False

    def is_bk_s(self) -> bool:
        return False

    def is_bk_e(self) -> bool:
        return False


class UnknownToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderUnknown(self)

    def isUnknown(self) -> bool:
        return True


class EscapedToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        self.value = "\\"
        printer.renderTEXT(TEXTToken(self.value))

    def isUnknown(self) -> bool:
        return True


class IDToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderID(self)

    def isID(self) -> bool:
        return True


class IDEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderIDE(self)

    def isIDE(self) -> bool:
        return True


class STSToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderSTS(self)

    def isSTS(self) -> bool:
        return True


class HToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderH(self)

    def isH(self) -> bool:
        return True


class TOC1Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderTOC1(self)

    def isTOC1(self) -> bool:
        return True


class TOC2Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderTOC2(self)

    def isTOC2(self) -> bool:
        return True


class TOC3Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderTOC3(self)

    def isTOC3(self) -> bool:
        return True


class MTToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderMT(self)

    def isMT(self) -> bool:
        return True


class MT2Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderMT2(self)

    def isMT2(self) -> bool:
        return True


class MT3Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderMT3(self)

    def isMT3(self) -> bool:
        return True


class MSToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderMS(self)

    def isMS(self) -> bool:
        return True


class MS2Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderMS2(self)

    def isMS2(self) -> bool:
        return True


class MRToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderMR(self)

    def isMR(self) -> bool:
        return True


class MIToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderMI(self)

    def isMI(self) -> bool:
        return True


class RToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderR(self)

    def isR(self) -> bool:
        return True


class PToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderP(self)

    def isP(self) -> bool:
        return True


class BToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderB(self)

    def isB(self) -> bool:
        return True


class CToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderC(self)

    def isC(self) -> bool:
        return True


class CASToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderCAS(self)
        pass

    def isCAS(self) -> bool:
        return True


class CAEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderCAE(self)
        pass

    def isCAE(self) -> bool:
        return True


class CLToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderCL(self)
        pass

    def isCL(self) -> bool:
        return True


class VToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderV(self)

    def isV(self) -> bool:
        return True


class TEXTToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderTEXT(self)

    def isTEXT(self) -> bool:
        return True


class WJSToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderWJS(self)

    def isWJS(self) -> bool:
        return True


class WJEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderWJE(self)

    def isWJE(self) -> bool:
        return True


class SToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderS(self)

    def isS(self) -> bool:
        return True


class S2Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderS2(self)

    def isS2(self) -> bool:
        return True


class S3Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderS3(self)

    def isS3(self) -> bool:
        return True


class S4Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderS4(self)
        pass

    def isS4(self) -> bool:
        return True


class S5Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderS5(self)
        pass

    def isS5(self) -> bool:
        return True


class QToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderQ(self)

    def isQ(self) -> bool:
        return True


class Q1Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderQ1(self)

    def isQ1(self) -> bool:
        return True


class Q2Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderQ2(self)

    def isQ2(self) -> bool:
        return True


class Q3Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderQ3(self)

    def isQ3(self) -> bool:
        return True


class Q4Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderQ4(self)
        pass

    def isQ4(self) -> bool:
        return True


class QAToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderQA(self)
        pass

    def isQA(self) -> bool:
        return True


class QACToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderQAC(self)
        pass

    def isQAC(self) -> bool:
        return True


class QACEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderQACE(self)
        pass

    def isQACE(self) -> bool:
        return True


class QCToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderQC(self)
        pass

    def isQC(self) -> bool:
        return True


class QMToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderQM(self)
        pass

    def isQM(self) -> bool:
        return True


class QM1Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderQM1(self)
        pass

    def isQM1(self) -> bool:
        return True


class QM2Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderQM2(self)
        pass

    def isQM2(self) -> bool:
        return True


class QM3Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderQM3(self)
        pass

    def isQM3(self) -> bool:
        return True


class QRToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderQR(self)
        pass

    def isQR(self) -> bool:
        return True


class QSSToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderQSS(self)
        pass

    def isQSS(self) -> bool:
        return True


class QSEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderQSE(self)
        pass

    def isQSE(self) -> bool:
        return True


class QTSToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderQTS(self)

    def isQTS(self) -> bool:
        return True


class QTEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderQTE(self)

    def isQTE(self) -> bool:
        return True


class NBToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderNB(self)

    def isNB(self) -> bool:
        return True


class FSToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderFS(self)

    def isFS(self) -> bool:
        return True


class FRToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderFR(self)

    def isFR(self) -> bool:
        return True


class FREToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderFRE(self)

    def isFRE(self) -> bool:
        return True


class FKToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderFK(self)

    def isFK(self) -> bool:
        return True


class FTToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderFT(self)

    def isFT(self) -> bool:
        return True


class FQToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderFQ(self)

    def isFQ(self) -> bool:
        return True


class FQAToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderFQA(self)
        pass

    def isFQA(self) -> bool:
        return True


class FQAEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderFQAE(self)
        pass

    def isFQAE(self) -> bool:
        return True


class FQBToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderFQAE(self)
        pass

    def isFQB(self) -> bool:
        return True


class FEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderFE(self)

    def isFE(self) -> bool:
        return True


class FPToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderFP(self)

    def isFP(self) -> bool:
        return True


class ISToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderIS(self)

    def isIS(self) -> bool:
        return True


class IEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderIE(self)

    def isIE(self) -> bool:
        return True


class BDSToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderBDS(self)

    def isBDS(self) -> bool:
        return True


class BDEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderBDE(self)

    def isBDE(self) -> bool:
        return True


class BDITSToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderBDITS(self)

    def isBDITS(self) -> bool:
        return True


class BDITEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderBDITE(self)

    def isBDITE(self) -> bool:
        return True


class LIToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderLI(self)

    def isLI(self) -> bool:
        return True


class LI1Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderLI1(self)
        pass

    def isLI1(self) -> bool:
        return True


class LI2Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderLI2(self)
        pass

    def isLI1(self) -> bool:
        return True


class LI3Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderLI3(self)
        pass

    def isLI1(self) -> bool:
        return True


class LI4Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderLI4(self)
        pass

    def isLI1(self) -> bool:
        return True


class DToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderD(self)

    def isD(self) -> bool:
        return True


class SPToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderSP(self)

    def isSP(self) -> bool:
        return True


class ADDSToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderADDS(self)

    def isADDS(self) -> bool:
        return True


class ADDEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderADDE(self)

    def isADDE(self) -> bool:
        return True


class NDSToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderNDS(self)

    def isNDS(self) -> bool:
        return True


class NDEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderNDE(self)

    def isNDE(self) -> bool:
        return True


class PBRToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderPBR(self)

    def isPBR(self) -> bool:
        return True


# Cross References
class XSToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderXS(self)

    def isXS(self) -> bool:
        return True


class XDCSToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderXDCS(self)

    def isXDCS(self) -> bool:
        return True


class XDCEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderXDCE(self)

    def isXDCE(self) -> bool:
        return True


class XOToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderXO(self)

    def isXO(self) -> bool:
        return True


class XTToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderXT(self)

    def isXT(self) -> bool:
        return True


class XEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderXE(self)

    def isXE(self) -> bool:
        return True


class MToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderM(self)

    def isM(self) -> bool:
        return True


# Transliterated Words
class TLSToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderTLS(self)

    def isTLS(self) -> bool:
        return True


class TLEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderTLE(self)

    def isTLE(self) -> bool:
        return True


# Indenting paragraphs
class PIToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderPI(self)

    def isPI(self) -> bool:
        return True


class PI2Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderPI2(self)

    def isPI2(self) -> bool:
        return True


# Small caps
class SCSToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderSCS(self)

    def isSCS(self) -> bool:
        return True


class SCEToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderSCE(self)

    def isSCE(self) -> bool:
        return True


# REMarks
class REMToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.renderREM(self)

    def isREM(self) -> bool:
        return True


# Tables
class TRToken(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTR(self)
        pass

    def isTR(self) -> bool:
        return True


class TH1Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTH1(self)
        pass

    def isTH1(self) -> bool:
        return True


class TH2Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTH2(self)
        pass

    def isTH2(self) -> bool:
        return True


class TH3Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTH3(self)
        pass

    def isTH3(self) -> bool:
        return True


class TH4Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTH4(self)
        pass

    def isTH4(self) -> bool:
        return True


class TH5Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTH5(self)
        pass

    def isTH5(self) -> bool:
        return True


class TH6Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTH6(self)
        pass

    def isTH6(self) -> bool:
        return True


class THR1Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTHR1(self)
        pass

    def isTHR1(self) -> bool:
        return True


class THR2Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTHR2(self)
        pass

    def isTHR2(self) -> bool:
        return True


class THR3Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTHR3(self)
        pass

    def isTHR3(self) -> bool:
        return True


class THR4Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTHR4(self)
        pass

    def isTHR4(self) -> bool:
        return True


class THR5Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTHR5(self)
        pass

    def isTHR5(self) -> bool:
        return True


class THR6Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTHR6(self)
        pass

    def isTHR6(self) -> bool:
        return True


class TC1Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTC1(self)
        pass

    def isTC1(self) -> bool:
        return True


class TC2Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTC2(self)
        pass

    def isTC2(self) -> bool:
        return True


class TC3Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTC3(self)
        pass

    def isTC3(self) -> bool:
        return True


class TC4Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTC4(self)
        pass

    def isTC4(self) -> bool:
        return True


class TC5Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTC5(self)
        pass

    def isTC5(self) -> bool:
        return True


class TC6Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTC6(self)
        pass

    def isTC6(self) -> bool:
        return True


class TCR1Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTCR1(self)
        pass

    def isTCR1(self) -> bool:
        return True


class TCR2Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTCR2(self)
        pass

    def isTCR2(self) -> bool:
        return True


class TCR3Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTCR3(self)
        pass

    def isTCR3(self) -> bool:
        return True


class TCR4Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTCR4(self)
        pass

    def isTCR4(self) -> bool:
        return True


class TCR5Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTCR5(self)
        pass

    def isTCR5(self) -> bool:
        return True


class TCR6Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        # printer.renderTCR6(self)
        pass

    def isTCR6(self) -> bool:
        return True


# Introductions
class IS1_Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.render_is1(self)

    def is_is1(self) -> bool:
        return True


class IMT1_Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.render_imt1(self)

    def is_imt1(self) -> bool:
        return True


class IMT2_Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.render_imt2(self)

    def is_imt2(self) -> bool:
        return True


class IMT3_Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.render_imt3(self)

    def is_imt3(self) -> bool:
        return True


class IP_Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.render_ip(self)

    def is_ip(self) -> bool:
        return True


class IOT_Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.render_iot(self)

    def is_iot(self) -> bool:
        return True


class IO1_Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.render_io1(self)

    def is_io1(self) -> bool:
        return True


class IO2_Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.render_io2(self)

    def is_io2(self) -> bool:
        return True


class IOR_S_Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.render_ior_s(self)

    def is_ior_s(self) -> bool:
        return True


class IOR_E_Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.render_ior_e(self)

    def is_ior_e(self) -> bool:
        return True


# Quoted book title
class BK_S_Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.render_bk_s(self)

    def is_bk_s(self) -> bool:
        return True


class BK_E_Token(UsfmToken):
    def renderOn(self, printer: AbstractRenderer) -> None:
        printer.render_bk_e(self)

    def is_bk_e(self) -> bool:
        return True
