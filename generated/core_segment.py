# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class CoreSegment(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.metadata = self._root.Metadata(self._io, self, self._root)
        self.structure = self._root.Structure(self._io, self, self._root)

    class Alpha(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.left = self._io.read_bits_int(6)
            self.right = self._io.read_bits_int(6)


    class Metadata(KaitaiStruct):
        """TC Consent Management Platform."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._io.read_bits_int(6)
            self.created = self._io.read_bits_int(36)
            self.updated = self._io.read_bits_int(36)
            self._io.align_to_byte()
            self.cmp = self._root.Metadata.Cmp(self._io, self, self._root)
            self.gvl_version = self._io.read_bits_int(12)

        class Cmp(KaitaiStruct):
            """Consent Management Platform."""
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.id = self._io.read_bits_int(12)
                self.version = self._io.read_bits_int(12)
                self.screen = self._io.read_bits_int(6)
                self._io.align_to_byte()
                self.language = self._root.Alpha(self._io, self, self._root)



    class Structure(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.policy_version = self._io.read_bits_int(6)
            self.is_service_specific = self._io.read_bits_int(1) != 0
            self.use_non_standard_stacks = self._io.read_bits_int(1) != 0
            self.special_feature_opt_ins = [None] * (12)
            for i in range(12):
                self.special_feature_opt_ins[i] = self._io.read_bits_int(1) != 0

            self.purposes_consent = [None] * (24)
            for i in range(24):
                self.purposes_consent[i] = self._io.read_bits_int(1) != 0

            self.purposes_li_transparency = [None] * (24)
            for i in range(24):
                self.purposes_li_transparency[i] = self._io.read_bits_int(1) != 0

            self._io.align_to_byte()
            self.sj_disclosures = self._root.Structure.SjDisclosures(self._io, self, self._root)
            self.vendor_consent = self._root.Structure.VendorSection(self._io, self, self._root)
            self.vendor_li = self._root.Structure.VendorSection(self._io, self, self._root)
            self.pub_restrictions = self._root.Structure.PubRestrictionsSection(self._io, self, self._root)

        class PubRestrictionsSection(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.num_pub_restrictions = self._io.read_bits_int(12)
                self._io.align_to_byte()
                if self.num_pub_restrictions > 0:
                    self.pub_restriction_entries = [None] * (self.num_pub_restrictions)
                    for i in range(self.num_pub_restrictions):
                        self.pub_restriction_entries[i] = self._root.Structure.PubRestrictionsSection.PubRestrictionEntry(self._io, self, self._root)



            class PubRestrictionEntry(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.purpose_id = self._io.read_bits_int(6)
                    self.restriction_type = self._io.read_bits_int(2)
                    self._io.align_to_byte()
                    self.range_section = self._root.Structure.RangeSection(self._io, self, self._root)



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
                    self.range_section = self._root.Structure.RangeSection(self._io, self, self._root)



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
                    self.range_entries[i] = self._root.Structure.RangeEntry(self._io, self, self._root)



        class SjDisclosures(KaitaiStruct):
            """Specific Jurisdiction Disclosures."""
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.purpose_one_treatment = self._io.read_bits_int(1) != 0
                self._io.align_to_byte()
                self.pub_country = self._root.Alpha(self._io, self, self._root)


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





