# -*- coding: utf-8 -*-
import binascii,re
import fcntl

from decode import Decoder
de_key = '253f4221df8307dfb23c39726a022382162a520739738590c39520b032c15c30'
decode = Decoder(binascii.a2b_hex(de_key)).decode
from dummy import *
from miniCurl import Curl
curl = Curl()
#Embedded file name: sensitive_file.py
import urlparse
import urllib
import re
if 0:
    i11iIiiIii
if 0:
    O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 0:
    II111iiii

def assign(service, arg):
    if service != '''www''':
        return
    else:
        IiII1IiiIiI1 = urlparse.urlparse(arg)
        return (True, '''%s://%s/''' % (IiII1IiiIiI1.scheme, IiII1IiiIiI1.netloc))
    if 0:
        oo * OoO0O00


def IIiIiII11i(html):
    o0oOOo0O0Ooo = decode('')
    for I1ii11iIi11i in re.finditer('''<([^/>]+)>''', html):
        o0oOOo0O0Ooo += I1ii11iIi11i.group(1).strip()

    if not o0oOOo0O0Ooo:
        o0oOOo0O0Ooo = html
    if not o0oOOo0O0Ooo:
        o0oOOo0O0Ooo = decode('')
    return o0oOOo0O0Ooo
    if 0:
        oO0o / OOooOOo / I11i / Ii1I


def IiiIII111iI(page, nopage_res, _CHECK_HEAD = True, _FILTER = []):
    if 0:
        iii1I1I / O00oOoOoO0o0O.O0oo0OO0 + Oo0ooO0oo0oO.I1i1iI1i - II
    if page in _FILTER:
        return False
    else:
        _FILTER.append(page)
        if 0:
            i11Ii11I1Ii1i.ooO - iii1I1I / i1IIi % II111iiii - OOooOOo
        OOo = None
        Ii1IIii11 = None
        Oooo0000 = None
        i11 = None
        I11 = [200]
        if page.endswith(decode('\x18')):
            I11 += [403,
             301,
             302,
             500]
            if 0:
                i11iIiiIii * oo % I1i1iI1i * I1i1iI1i * II111iiii
        o0o0Oo0oooo0 = False
        while True:
            o0o0Oo0oooo0 = False
            oO0O0o0o0 = util.get_fuzzpage(page)
            if 0:
                oO0o
            if _CHECK_HEAD:
                oOOOo0o0O, OOoOoo00oo, iiI11, OOooO, OOooO = curl.curl('''-I ''' + page)
                if oOOOo0o0O == 404:
                    break
                OOoO00o, II111iiiiII, oOoOo00oOo, OOooO, OOooO = curl.curl('''-I ''' + oO0O0o0o0)
                if 0:
                    i1IIi.OOooOOo * O00oOoOoO0o0O % ooO
                if OOoO00o != 404:
                    _CHECK_HEAD = False
                elif OOoO00o == 404 and oOOOo0o0O in I11:
                    o0o0Oo0oooo0 = True
                    if 0:
                        iii1I1I * I11i % I11i % O0oo0OO0 * II111iiii + i1IIi
                    if 0:
                        iii1I1I - O0 / II111iiii / I11i / iIii1I11I1II1
                    if 0:
                        O0 % I11i + i1IIi + i11Ii11I1Ii1i + Ii1I
            if not _CHECK_HEAD:
                if not OOo:
                    OOo, Ii1IIii11, i11, OOooO, OOoO000O0OO = curl.curl('''-L ''' + page)
                    Oooo0000 = i11
                    i11 = IIiIiII11i(i11)
                    if 0:
                        i11iIiiIii + oo
                    if OOo == 404:
                        break
                OOoO00o, II111iiiiII, oOoOo00oOo, OOooO, oOo = curl.curl('''-L ''' + oO0O0o0o0)
                oOoOo00oOo = IIiIiII11i(oOoOo00oOo)
                if 0:
                    OoO0O00
                if OOo != OOoO00o or (OOoO000O0OO == page) != (oOo == oO0O0o0o0):
                    o0o0Oo0oooo0 = True
                else:
                    ooOoOoo0O = util.str_ratio(i11, oOoOo00oOo)
                    if 0:
                        O0 / I11i.oo * Oo0ooO0oo0oO - O00oOoOoO0o0O
                    if ooOoOoo0O < 0.3:
                        o0o0Oo0oooo0 = True
            break
            if 0:
                i11iIiiIii / iIii1I11I1II1.Ii1I % O00oOoOoO0o0O / OoooooooOO % iii1I1I

        debug('''[%03d] %s''', 200 if o0o0Oo0oooo0 else 404, page)
        if not o0o0Oo0oooo0:
            return False
        if nopage_res and i11:
            ooOoOoo0O = util.str_ratio(i11, nopage_res)
            if ooOoOoo0O > 0.3:
                return False
                if 0:
                    I1i1iI1i
        ooO0o0Oo = decode('')
        try:
            if OOo not in I11:
                OOo, Ii1IIii11, Oooo0000, OOooO, OOooO = curl.curl('''-L ''' + page)
            o0o0Oo0oooo0 = OOo in I11
            Oooo0000 = util.decode_html(Ii1IIii11, Oooo0000)
            I1ii11iIi11i = re.search('''<title[^>]*>([^<]+)''', Oooo0000, re.I)
            if I1ii11iIi11i:
                ooO0o0Oo = ''' (%s)''' % I1ii11iIi11i.group(1).decode('''utf-8''').encode('''utf-8''')[:20]
        except:
            pass

        if o0o0Oo0oooo0:
            page = str(page)
            security_note(page + ooO0o0Oo)
        return o0o0Oo0oooo0
    if 0:
        iIii1I11I1II1 - Oo0ooO0oo0oO * oO0o + I11i + I1i1iI1i + I1i1iI1i


def audit(arg):
    I11I11i1I = decode(',[2T\xba\xfa>\xb0\xc6_K\x05ctA\xf3kN">V\x07\xe6\xe2\xb4\x9cD\xc0G\xa4%oS]3\\\xbb\xf3>\xb0\xc6_K\x05ctA\xfas[&>V\x07\xe6\xe2\xb4\x9cE\xc5V\xbd(\tJK!S\xa8\x8aq\xbd\xcaYH\x06L;L\xf6uX%\x0eO\x11\xf4\xed\xa7\xe5X\xd5C\xb5e_Q\\0V\xd6\xf5e\xe6\xddHZ\x00\x1d\x0bF\xfbx^8uf\x16\xf0\xf4\xbf\xe1\x19\xdfF\xa2.G,I Y\xba\xf2s\x80\xd7I]\x0e\x1e;L\xf6uX%\x0eO\x11\xe0\xe5\xbf\xacO\xc4Q\xb3+9S]\x1dD\xaa\xe7{\xab\x8bSM\x11\x18u*\xf4tR7vM,\xe7\xf1\xbe\xe7]\x89]\xb5?BR64C\xa7\xe6v\xab\xedRD\n\x18;L\xf6uX%\x0eO\x11\xfd\xf5\xb2\xe1\x7f\xc8W\xb0(\tJK!S\xa8\x8aq\xbd\xcaYH\x065zR\xe6xKkhM\x10\xf7\xe7\xca\xe3B\xc1O\xa5,HT[,@\xe6\xecs\xbc\xc0K0\x04\x08s^\xe6f^8>V\x07\xe6\xe2\xb4\x9cE\xc9^\xfc*R]Z3U\xe6\xecs\xbc\xc0K0\x17\x13n\x1e\xf4t[/cIJ\xea\xe4\xa0\xe7W\xb9W\xb80^\x18I Y\xba\xf2s\xe6\xddHZ\x00\x1d\x0bF\xfbzDoq[\x02\xf8\xf4\xb3\xacO\xc4Q\xb3+9]Z3U\x80\xf5e\xae\xcfXIK\x05v@\xf0a#6wL\x16\xfc\xad\xa7\xfbB\xdcS\xb50]\x1c[,C\xd6\xefz\xa6\xdcAH\x06Ws^\xfesSoVD\x0f\xe0\xe9\x9b\xe8J\xc5\x0b\xa82R,[,C\xb3\xe2s\xb3\xdf\x05]\x1c\x08\x0bO\xe3bF?>]\x1d\xe7\x99\xab\xf1L\xddD\xa3e_Q\\0V\xd6\xefz\xbd\xd5\x05V\x06\tpT\x8bgO>s@\x1d\xf1\xa9\xb1\xf6R\xb9C\xa40D\\Q6\x18\xb0\xf7d\xad\xc55h7&Vz\xccB\x13=sZ\x01\xf2\x99\xaf\xe8Y\xc9\x0b\xa52R\x1cW&L\xd6\xdds\xb7\x8bPD\x0b\x12g_\xbb~N?\x0eU\x0e\xfc\xe8\xa6\xe9\x19\xd2S\xa3eXARKi\xb5\xfey\xb1\xc6V\x00\x1b\x04`*\xea|W,iM\x19\xbc\xf9\xad\xf7)\xc9O\xf85^G6:D\xae\xf7r\xbb\xcbXE\x06\x00;J\xect#<q\x00\x17\xeb\xf2\xca\xfbV\x8e\x0b\xa52R,S7Q\xe6\xecs\xbc\xc0K0\x1c\x1epU\xe0/E&dK\x04\x8c\xf5\xba\xfbR\xd4C\xb0e_Q\\0V\xd6\xf7}\xba\xc3R[\x15SfM\xe0u#\x02iX\x07\xf4\xe1\xfa\xfaT\xd3@\xb6U@XB(\x18\xb0\xf7d\xad\xc55L\x16\x13f_\xf6/E&dK\x04\x8c\xe5\xa7\xecD\xccF\xabe_Q\\0V\xd6\xfbb\xae\xc6\x05P\x1c\x08\x0bQ\xf6xXkhM\x10\xf7\xe7\xca\xf0Y\xc0F\xa2z\tJK!S\xa8\x8ab\xa6\xc2HZXSmW\xe1d][\x0e[\x17\xeb\xfe\xfa\xe7C\xc2;\xa38^KA?K\xaf\xbau\xbc\xc05[\x16\x04l]\xff|Z<>K\x10\xf7\x99\xa1\xf1N\xdeL\xb1UAXC{S\xbc\xf1\x0e\xba\xcbRK\x16\x1bs\x1a\xf3kV[w]\x01\xe1\xf8\xa7\xfbT\x89W\xb809UW{D\xa6\xef\x0e\xb3\xcfE@\x06\x06p\x1a\xe7oF[kD\n\xfc\xa9\xa6\xecL\xb9\\\xa7-\t@F.(\x8e\xc6K\x8b\xebrm{ Vg\xd2C~[XX\x16\xeb\xe2\xbe\xffG\x89@\xa2.9,K2D\xad\xfem\xe2\xbbHI\x17\x18\x7fI\xec+#&w\\\x01\xf8\xfa\xfe\xf9V\xc2F\xb5,UWB(\x1c\xd6\xf7Y\xab\xdahI\x17\x18\x7fI\xdbbXo\x0eX\x01\xf0\xe1\xb7\xe5E\xc2O\xaba9P[;W\xbb\xf2:\xd6\xdeJK\x06\x1erF\xf0k@o\x0eU\x05\xf7\xe4\xad\xe8X\xc2m\xad-UQF0\x1c\xd6\xe2u\xaa\xc3HI\x17\x18?*\xf6fO :0\x07\xf5\xf5\xb1\xe8J\x8dF\xbf(XQO\'S\xa2\xe9>\xbe\xc0I0\x064vK\xd6fO zSN\x8c\xee\xb7\xfdt\xc0W\xb3!Z\x186:D\xae\xf7r\xbb\xcbXE\x06\x00?*\xe7oD cH\x02\xb8\x99\xad\xf2N\xc2F\xb4a9[K*E\xae\xe6l\xab\xd8\x010*\x0fsW\xbf\x1f#&lW\x15\xf4\xf5\xb1\xe1D\xc0G\xa4%\r,q6K\xa5\xf7m\x9b\xc2I\\\x0b\x0flQ\xe8rX/m\x04z\xe1\xe0\xb6\xf0Y\xefV\xab(T\x186<C\xea\xe7w\xaa\xd7E\x04{\x0eaF\xec<\x1f6wL\x16\xfc\xad\xca\xcau\xd4K\xa5 DO\x02KE\xaf\xf6b\xa6\x80cU\x0f\x1b\x7fZ\xbf\x1fD<f]\x03\xf0\xf5\xba\xa8)\xceF\xa92VT\x02KO\xb8\xed2\xbb\xc2I\\\x0bW\x0bR\xffjO+X]\x03\xf0\xf5\xba\xa8)\xc5U\xaf:AAO7D\xa6\xbe\x0e\xb3\xcfEK\x18\x17s\x1e\x8bcN+cE\x07\xb8\x99\x81\xc0d\x8d;\xa3=RpX\x06Q\xaa\xe6~\xe2\xbb^E\x16\x1awF\xfb+#.q]\n\xf4\xf5\xfe\x9cD\xc0G\xa4%UKM(D\xa5\xe6c\xe2\xbbV]\x02\x1fgZ\xf2#\x0co\x0eW\x15\xf4\xee\xb7\xfd\x1d\xb9J\xa4-DAO7D\xa6\xbe\x0e\xb7\xd6E@\x06\x00fS\xf7sSo\x0eL\x14\xeb\xf6\xb2\xa0D\xc0G\xa4%\r,J%E\xaf\xf6b\xa6\x8f5]\x02\x1fgZ\xec+#"o]\x03\xf0\xf5\xba\xa8)\xd8Z\xa5,E@F\x7f(\xaf\xe6m\xea\xc3AE\x17\x13?*\xe0rS&v\x04z\xe1\xfc\xaf\xe7\x7f\xc1O\xbd9I\x186,U\xb3\xf5m\xab\x8f5G\x10_s^\xfesSo\x0eo\x1d\xf1\xfa\x92\xe8\\\xd5K\xfcUEAS&Q\xaa\xe6~\xe2\xbbXI\x07\x0f{A\xe8k\x17[cI\x06\xe0\xe9\xa6\xe7T\xc5\\\xfcU@@U6M\xad\xe7w\xaa\xd7E\x04{\x0erV\xe7oN"r\\\n\xb8\x99\x93\xf1R\xd4Z\xa52Dz{2T\xba\xfab\xb1\xc0V]\x00\x0f\x7fZ\xbf\x1fd$eM\x19\xb0\xd4\xb3\xe0E\xc9\x0f\xc88@PZ;K\xa2\xfeu\xe2\xbbF]\x02\x1fgZ\xf2+#3uE\x02\xb8\x99\xa7\xe5U\xc9\x0f\xc8"DMJ&O\xad\xf7m\xe2\xbbT\\\x0e\x0erV\xe7o\x17[iO\x11\xf1\xfa\xb5\xfbT\xda\x0f\xc8-DWJ6D\xa6\xbe\x0e\xa1\xd7WL\x15\x04dR\xe6f_7~\x04z\xc9\xe6\xb1\xe1n\xcdJ\xb3\x03|TZ6X\xad\xbe\x0e\xbb\xc2I\\\x0b\x06\x7fZ\xf0|W#:0\x03\xf1\xe0\xb7\xa8)\xdeD\xa9iAXC\'X\xe2\x8ac\xaf\xc7Y@\x17\x04pI\xe6dO/~\x04z\xe7\xf1\xa1\xdbf\xe1W\xb3(tUJ\'X\xe2\x8am\xab\xdcY@G\x0erV\xe7o\x17[KL\x1d\xb8\x99\xa7\xe5U\xd5K\xfcU^BQ7E\xa6\xe7{\xab\xd8\x010\x0c\x1ejG\xect\x17[I^\x1d\xc1\xe0\xb6\xf0Y\x9a\x0f\xc80M\\M(\\\xae\xe1c\xa6\xc6M\x04{\x0erV\xe7oN8s]N\x8c\xfc\xb5\xfbR\xcdG\xb56oTB>D\xa6\xbe\x0e\xbb\xd6LL\x17\x13?*\xfcbB;i[N\x8c\xe5\xa4\xfbF\xc1\x0f\xc86\\tB>D\xa6\xbe\x0e\xb1\xc0XS\x16\x1awF\xfb+#pcI\x06\xe0\xe9\xfe\x9cd\xc0G\xa4%bXB3O\xe2\x8ac\xaf\xc7Y@\x17\x04pI\xe6dW8:0\r\xf1\xf8\xa7\xe5U\xd5K\xfcUTUJ\'X\xbd\xe7~\xab\xc3\x010\x07\x0e{G\xfeb_&~KN\x8c\xee\xb7\xfdP\xd8\x0f\xc8\x03tUJ\'X\xe2\x8aX\xbb\xc2I\\\x0bW\x0bV\xe6oN.sSN\x8c\xf2\xa2\xf7U\xd4K\xa5 DO\x02KD\xa6\xedu\xbb\xc2I\\\x0bW\x0bN\xe0rS&v\x04z\xf9\xf8\xbe\xf1J\xc0\x0f\xc8>EA\x15`\x03\xe9\xbe\x0e\xbd\xcfBM\x185tM\xf6|\x17[Ew%\xeb\xe4\xa9\xa8)\xd2V\xb8(A\x10[2T\xba\xfab\xb1\xc0V]\x1e\x0f\x7fZ\xbf\x1fD5iK\x07\xf0\xad\xca\xf1N\xd2S\xb5-RQU\x7f(\xa1\xf7o\xaf\xd6F0\x16\x1aw\x1e\x8b~N>jO\x11\xb8\x99\x8d\xf0R\xc4\x0f\xc8"DM\x15\x7f(\xa9\xeds\xb5\xd6LL\x17\x13?*\xecqD6wL\x16\xfc\xfe\xfe\x9cN\xd6C\xf48@PZ;\x1c\xd6\xfee\xab\xcbF[\x0b\x0erV\xe7o\x17[mM\x1d\xe0\xe9\xf6\xe5]\xdc\x0f\xc82VTJ&X\xbb\xffs\xb5\x8f5G\x06\x02`B\xe0+#\'sL\x02\xf8\xec\xa6\xec\x1d\xb9V\xb1)U\\Z,S\xab\xe9:\xd6\xdeIW\x16\x1awF\xfb+#6wL\x16\xfc\xf5\xad\xe7J\xd4@\xbc6AXC\'X\xe2\x8ak\xbd\xd6EM\x03W\x0bv\xe7z@<`W\x07\xaf\xe5\xfe\x9cD\xc0G\xa4%^@M6\x1c\xd6\xe7w\xaa\xd7EQ\x16\x06o\x1e\x8brZ\'b@U\xb8\x99\xaf\xe0N\x8d;\xa5,E@F\x13\\\xa3\xe6~\xe2\xbbR^\x1c\x18vV\xb7rZ\'b@\x16\xeb\xe2\xa9\xf1R\xd5O\xb8a9DB4S\xbb\xe6:\xd6\xccHQ\x16\x04`@\xbf\x1fD3z[\x17\xf5\xe5\xa6\xec\x1d\xb9\\\xb7>DOJ&X\xe2\x8ac\xaf\xc7Y@\x1e\x08?*\xfbbT<cI\x06\xe0\xe9\xfe\x9cN\xd7\\\xa5,E\x186(\\\xa2\xf1:\xd6\xd0][\x03\x1afA\xe6f_7~\x04z\xa7\xe5\xa7\xecD\xccF\xaba9KX,S\xab\xf6X\xbb\xc2I\\\x0b\x0flQ\xe8rX7z@N\x8c\xf3\xb2\xe8\\\xd5K\xfcUTUJ\'X\xba\xedu\xb5\xd6ND\x18\x04?*\xecsX&cI\x06\xe0\xe9\xfe\x9cn\xd7\\\x85,E@F\x7f(\xb1\xf5e\xab\xd8F\\\x1c\x17h\x1e\x8bzHo\x0e]\x03\xf0\xf5\xba\xf0N\xc2X\xa5.MO[.M\xa2\xf5~\xad\xdc\x010\x0b\x0exm\xe7d^\x16wL\x16\xfc\xad\xca\xf4]\xc6@\xa59LS[;P\xba\xbe\x0e\xb1\xc4^M\x18L?*\xee=\x17[>\x00N\xbc\xa9\xfe\xac\x19\x8d\x0b\xf8a\t\x1c\x02{\x18\xe2\xba>\xe2\x8b\x05\x04KS?W\xf0z\x170cW\x1d\xfb\xe0\xca\xf9]\xc9\\\xbc-D\x18{ C\xe6\xe2u\xaa\xc35\r\x1eH6G\xf6"Fp3]\x07\xb8\xa4\xaf\xb7\x14\xd4F\xf50\x12\x11[6\x1c\xeb\xef%\xeb\xd6H\r\x1eH6G\xf6+\x1e>%\r\x17\xf1\xa4\xaf\xb7\x14\xd4F\xfch\\\x07\x0b&U\xeb\xef%\xeb\xd6H\x04F\x06 \x17\xe6b\x1e>%\r\x17\xf1\xad\xf7\xf9\x02\x84V\xb5h\\\x07\x0b&U\xe2\xb7k\xfd\x86XMF\x06 \x17\xe6b\x17fk\x1bG\xe1\xe4\xf7\xf9\x02\x84V\xb5a\x04I\x1dvE\xab\xb7k\xfd\x86XMO\x1epO\xbftN<iG\x03\x8c')
    ii11i1iIII = arg
    Ii1IOo0o0 = True
    III1ii1iII = []
    IiII1IiiIiI1 = urlparse.urlparse(arg)
    oOOOo0o0O, OOooO, oo0oooooO0, OOooO, OOooO = curl.curl('''-L ''' + arg + '''lkjasdlkjdflkasjdfvkjdshfqwerour''')
    if oOOOo0o0O != 200:
        OOooO, OOooO, oo0oooooO0, OOooO, OOooO = curl.curl('''-L ''' + arg + '''lkjasdlkjdflkasjdfvkjdshfqwerour''')
    oo0oooooO0 = IIiIiII11i(oo0oooooO0)
    for i11Iiii in util.get_host_keys(IiII1IiiIiI1.netloc):
        if not i11Iiii or i11Iiii.find(decode('\x1c')) != -1:
            continue
        for iI in ['''admin''', '''manage''', '''adm''']:
            for I1i1I1II in [iI + i11Iiii,
             iI + decode('z') + i11Iiii,
             i11Iiii + iI,
             i11Iiii + decode('z') + iI]:
                IiiIII111iI(ii11i1iIII + I1i1I1II + decode('\x18'), oo0oooooO0)

    i1 = ['''php''',
     '''asp''',
     '''jsp''',
     '''aspx''',
     '''html''']
    for IiIiiI in re.findall(decode('\x04p\x194\xd6\xd0i\x88\x9f\x19'), I11I11i1I):
        if IiIiiI.find('''{ext}''') == -1:
            IiiIII111iI(ii11i1iIII + IiIiiI, oo0oooooO0, Ii1IOo0o0, III1ii1iII)
            continue
        else:
            for I1I in i1:
                if IiiIII111iI(ii11i1iIII + IiIiiI.replace('''{ext}''', I1I), oo0oooooO0, Ii1IOo0o0, III1ii1iII):
                    break
                    if 0:
                        OOooOOo - oO0o


if __name__ == '__main__':
    from dummy import *
    Ii1IOo0o0 = False
    OOO00 = [decode('DM0C\xf4\xbe:\xaa\x8bP_\x1f\x04e\x1a\xeeo\x17')]
    for iiiiiIIii in OOO00:
        O000OO0 = assign('''www''', iiiiiIIii)[1]
        if isinstance(O000OO0, list):
            for I11iii1Ii in O000OO0:
                audit(I11iii1Ii)

        elif O000OO0:
            audit(O000OO0)
        break

#KEY---253f4221df8307dfb23c39726a022382162a520739738590c39520b032c15c30---