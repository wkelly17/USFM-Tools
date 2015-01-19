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

    def render(self):
        self.f = codecs.open(self.outputFilename, 'w', 'utf_8_sig')
        self.loadUSFM(self.inputDir)
        self.run()
        self.f.close()

    def writeLog(self, s):
        print s

    # Support

    def escape(self, s):
        return s

    def renderTEXT(self, token):    self.f.write(self.escape(token.value))

    def renderH(self, token):       self.book = token.getValue()
    def renderMT(self, token):      self.f.write(u'\n<para style="mt">' + token.value.upper() + u'</para>')
    def renderMT1(self, token):     self.f.write(u'\n<para style="mt1">' + token.value.upper() + u'</para>')
    def renderMT2(self, token):     self.f.write(u'\n<para style="mt2">' + token.value.upper() + u'</para>')
    def renderMT3(self, token):     self.f.write(u'\n<para style="mt3">' + token.value.upper() + u'</para>')
    def renderMT4(self, token):     self.f.write(u'\n<para style="mt4">' + token.value.upper() + u'</para>')
    def renderMT5(self, token):     self.f.write(u'\n<para style="mt5">' + token.value.upper() + u'</para>')
    def renderMS(self, token):      self.f.write(u'\n<para style="ms">' + token.value + u'</para>')
    def renderMS1(self, token):     self.f.write(u'\n<para style="ms1">' + token.value + u'</para>')
    def renderMS2(self, token):     self.f.write(u'\n<para style="ms2">' + token.value + u'</para>')
    def renderMS3(self, token):     self.f.write(u'\n<para style="ms3">' + token.value + u'</para>')
    def renderMS4(self, token):     self.f.write(u'\n<para style="ms4">' + token.value + u'</para>')
    def renderMS5(self, token):     self.f.write(u'\n<para style="ms5">' + token.value + u'</para>')
    def renderP(self, token):       self.f.write(u'\n<para style="p"></para>')
    def renderB(self, token):       self.f.write(u'\n<para style="b" />')
    def renderS(self, token):       self.f.write(u'\n<para style="s">' + token.value + u'</para>')
    def renderS1(self, token):      self.f.write(u'\n<para style="s1">' + token.value + u'</para>')
    def renderS2(self, token):      self.f.write(u'\n<para style="s2">' + token.value + u'</para>')
    def renderS3(self, token):      self.f.write(u'\n<para style="s3">' + token.value + u'</para>')
    def renderS4(self, token):      self.f.write(u'\n<para style="s4">' + token.value + u'</para>')
    def renderS5(self, token):      self.f.write(u'\n<para style="s5">' + token.value + u'</para>')
    def renderC(self, token):       self.currentC = token.value; self.f.write(u'\n<chapter number="' + self.currentC + u'" style="c" />')
    def renderV(self, token):       self.f.write(u'\n<verse number="' + token.value + u'" style="v" />')
    def renderQ(self, token):       self.f.write(u'\n<para style="q">' + token.value + u'</para>')
    def renderQ1(self, token):      self.f.write(u'\n<para style="q1">' + token.value + u'</para>')
    def renderQ2(self, token):      self.f.write(u'\n<para style="q2">' + token.value + u'</para>')
    def renderQ3(self, token):      self.f.write(u'\n<para style="q3">' + token.value + u'</para>')
    def renderNB(self, token):      self.f.write(u'\n|  ')
    def renderLI(self, token):      self.f.write(u'* ')
    def renderPBR(self, token):     self.f.write(u'\n')

    def renderBDS(self, token):     self.f.write( u'**')
    def renderBDE(self, token):     self.f.write( u'**')
    def renderBDITS(self, token):   pass
    def renderBDITE(self, token):   pass

    def renderFS(self,token):       self.f.write(u'^[')
    def renderFE(self,token):       self.f.write(u']')
    def renderFR(self, token):      self.f.write(self.escape(token.value))
    def renderFT(self, token):      self.f.write(self.escape(token.value))
    def renderFQ(self, token):      self.f.write(self.escape(token.value))

    def renderXS(self,token):       self.f.write(u'^[')
    def renderXE(self,token):       self.f.write(u']')
    def renderXO(self, token):      self.f.write(self.escape(token.value))
    def renderXT(self, token):      self.f.write(self.escape(token.value))