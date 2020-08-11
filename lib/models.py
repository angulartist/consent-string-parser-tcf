from io import BytesIO

from kaitaistruct import KaitaiStream


class UnalignedStream(KaitaiStream):
    """
    Overrides align_to_byte to make an unaligned bit stream.
    """

    def __init__(self, io: BytesIO):
        super().__init__(io)
        self.bits = 0
        self.bits_left = 0

    def align_to_byte(self):
        """
        We want an unaligned stream.
        :return:
        """
        pass

    def reset(self):
        """
        Used to reset the stream.
        :return:
        """
        self.bits = 0
        self.bits_left = 0
        self.seek(0)

    @property
    def segment_type(self):
        _type = self.read_bits_int(3)
        self.reset()

        return _type
