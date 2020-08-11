# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class PtcSegment(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.segment_type = self._io.read_bits_int(3)
        self.pub_purposes_consent = [None] * (24)
        for i in range(24):
            self.pub_purposes_consent[i] = self._io.read_bits_int(1) != 0

        self.pub_purposes_li_transparency = [None] * (24)
        for i in range(24):
            self.pub_purposes_li_transparency[i] = self._io.read_bits_int(1) != 0

        self.num_custom_purposes = self._io.read_bits_int(6)
        if self.num_custom_purposes > 0:
            self.custom_purposes_consent = [None] * (self.num_custom_purposes)
            for i in range(self.num_custom_purposes):
                self.custom_purposes_consent[i] = self._io.read_bits_int(1) != 0


        if self.num_custom_purposes > 0:
            self.custom_purposes_li_transparency = [None] * (self.num_custom_purposes)
            for i in range(self.num_custom_purposes):
                self.custom_purposes_li_transparency[i] = self._io.read_bits_int(1) != 0




