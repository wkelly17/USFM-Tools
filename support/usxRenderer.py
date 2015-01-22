# -*- coding: utf-8 -*-
#

import abstractRenderer
import codecs

#
#   Simplest renderer. Ignores everything except ascii text.
#

class USXRenderer(abstractRenderer.AbstractRenderer):

    def __init__(self, inputDir, outputFilename):
        # Unset
        self.f = None  # output file stream
        # IO
        self.outputFilename = outputFilename
        self.inputDir = inputDir
        # Position
        self.currentC = 1
        self.book = u''
        # Flags
        self.printerState = {u'p': False, u'q': False, u'li': False}

    def render(self):
        self.f = codecs.open(self.outputFilename, 'w', 'utf_8_sig')
        self.loadUSFM(self.inputDir)
        self.run()
        self.f.write( self.stopP() + self.stopQ() + self.stopLI() )
        self.f.close()

    def writeLog(self, s):
        print s

    # Support

    def startP(self):
        if self.printerState[u'p'] == False:
            self.printerState[u'p'] = True
        return u'\n<para style="p">'

    def indent(self):
        if self.printerState[u'p'] == False:
          return u''
        else:
          return u'  '

    def stopP(self):
        if self.printerState[u'p'] == False:
            return u''
        else:
            self.printerState[u'p'] = False
            return u'</para>'

    def startQ(self, n):
        if self.printerState[u'q'] == False:
            self.printerState[u'q'] = True
        return u'\n<para style="q' + str(n) + u'">'

    def stopQ(self):
        if self.printerState[u'q'] == False:
            return u''
        else:
            self.printerState[u'q'] = False
            return u'</para>'

    def startLI(self, n):
        if self.printerState[u'li'] == False:
            self.printerState[u'li'] = True
        return u'\n<para style="li' + str(n) + u'">'

    def stopLI(self):
        if self.printerState[u'li'] == False:
            return u''
        else:
            self.printerState[u'li'] = False
            return u'</para>'

    def escape(self, s):
        return s

    def renderTEXT(self, token):    self.f.write( self.escape(token.value) )

    def renderH(self, token):       self.book = token.getValue()
    def renderMT(self, token):      self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n<para style="mt">' + token.value.upper() + u'</para>' )
    def renderMT1(self, token):     self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n<para style="mt1">' + token.value.upper() + u'</para>' )
    def renderMT2(self, token):     self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n<para style="mt2">' + token.value.upper() + u'</para>' )
    def renderMT3(self, token):     self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n<para style="mt3">' + token.value.upper() + u'</para>' )
    def renderMT4(self, token):     self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n<para style="mt4">' + token.value.upper() + u'</para>' )
    def renderMT5(self, token):     self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n<para style="mt5">' + token.value.upper() + u'</para>' )
    def renderMS(self, token):      self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n<para style="ms">' + token.value + u'</para>' )
    def renderMS1(self, token):     self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n<para style="ms1">' + token.value + u'</para>' )
    def renderMS2(self, token):     self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n<para style="ms2">' + token.value + u'</para>' )
    def renderMS3(self, token):     self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n<para style="ms3">' + token.value + u'</para>' )
    def renderMS4(self, token):     self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n<para style="ms4">' + token.value + u'</para>' )
    def renderMS5(self, token):     self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n<para style="ms5">' + token.value + u'</para>' )
    def renderP(self, token):       self.f.write( self.stopP() + self.stopQ() + self.stopLI() + self.startP() )
    def renderB(self, token):       self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n<para style="b" />')
    def renderS(self, token):       self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n\n<para style="s">' + token.value + u'</para>' )
    def renderS1(self, token):      self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n\n<para style="s1">' + token.value + u'</para>' )
    def renderS2(self, token):      self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n\n<para style="s2">' + token.value + u'</para>' )
    def renderS3(self, token):      self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n\n<para style="s3">' + token.value + u'</para>' )
    def renderS4(self, token):      self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n\n<para style="s4">' + token.value + u'</para>' )
    def renderS5(self, token):      self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n\n<para style="s5">' + token.value + u'</para>' )
    def renderC(self, token):       self.currentC = token.value; self.f.write( self.stopP() + self.stopQ() + self.stopLI() + u'\n<chapter number="' + self.currentC + u'" style="c" />' )
    def renderV(self, token):       self.f.write( u'\n' + self.indent() + u'<verse number="' + token.value + u'" style="v" />' )
    def renderQ(self, token):       self.renderQ1(token)
    def renderQ1(self, token):      self.f.write( self.stopP() + self.stopQ() + self.stopLI() + self.startQ(1) )
    def renderQ2(self, token):      self.f.write( self.stopP() + self.stopQ() + self.stopLI() + self.startQ(2) )
    def renderQ3(self, token):      self.f.write( self.stopP() + self.stopQ() + self.stopLI() + self.startQ(3) )
    def renderNB(self, token):      self.f.write( u'\n<char style="nb">' + self.indent() + u'</char>' )
    def renderLI(self, token):      self.f.write( self.stopP() + self.stopQ() + self.stopLI() + self.startLI() )
    def renderPBR(self, token):     self.f.write( u'\n' )

    def renderBDS(self, token):     self.f.write( u'<char style="bd">' )
    def renderBDE(self, token):     self.f.write( u'</char>' )
    def renderBDITS(self, token):   self.f.write( u'<char style="bdit">' )
    def renderBDITE(self, token):   self.f.write( u'</char>' )
    def renderEMS(self, token):   self.f.write( u'<char style="em">' )
    def renderEME(self, token):   self.f.write( u'</char>' )
    def renderITS(self, token):   self.f.write( u'<char style="it">' )
    def renderITE(self, token):   self.f.write( u'</char>' )
    def renderNOS(self, token):   self.f.write( u'<char style="no">' )
    def renderNOE(self, token):   self.f.write( u'</char>' )
    def renderSCS(self, token):   self.f.write( u'<char style="sc">' )
    def renderSCE(self, token):   self.f.write( u'</char>' )

    def renderFS(self,token):       self.f.write( u'\n<note caller="+" style="f">' )
    def renderFE(self,token):       self.f.write( u'\n</note>' )
    def renderFR(self, token):      self.f.write( u'\n  <char style="fr">' + self.escape(token.value) + u'</char>' )
    def renderFT(self, token):      self.f.write( u'\n  <char style="ft">' + self.escape(token.value) + u'</char>' )
    def renderFQ(self, token):      self.f.write( u'\n  <char style="fq">' + self.escape(token.value) + u'</char>' )

    def renderXS(self,token):       self.f.write( u'\n<note caller="-" style="x">' )
    def renderXE(self,token):       self.f.write( u'\n</note>' )
    def renderXO(self, token):      self.f.write( u'\n  <char style="xo">' + self.escape(token.value) + u'</char>' )
    def renderXT(self, token):      self.f.write( u'\n  <char style="xt">' + self.escape(token.value) + u'</char>' )