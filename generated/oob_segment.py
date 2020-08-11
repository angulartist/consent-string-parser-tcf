# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class OobSegment(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.segment_type = self._io.read_bits_int(3)
        self._io.align_to_byte()
        self.vendor_consent = self._root.VendorSection(self._io, self, self._root)

    class VendorSection(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.max_vendor_id = self._io.read_bits_int(16)
            self.is_range_encoding = self._io.read_bits_int(1) != 0
            if not (self.is_range_encoding):
                self.bit_field = [None] * (self.max_vendor_id)
                for i in range(self.max_vendor_id):
                    self.bit_field[i] = self._io.read_bits_int(1) != 0


            self._io.align_to_byte()
            if self.is_range_encoding:
                self.range_section = self._root.RangeSection(self._io, self, self._root)



    class RangeSection(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_entries = self._io.read_bits_int(12)
            self._io.align_to_byte()
            self.range_entries = [None] * (self.num_entries)
            for i in range(self.num_entries):
                self.range_entries[i] = self._root.RangeEntry(self._io, self, self._root)



    class RangeEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.is_a_range = self._io.read_bits_int(1) != 0
            self.start_or_only_vendor_id = self._io.read_bits_int(16)
            if self.is_a_range:
                self.end_vendor_id = self._io.read_bits_int(16)




