import base64

from kaitaistruct import BytesIO

from core_segment import CoreSegment
from lib.consts import (
    OOB_SEGMENT_TYPES,
    PUBLISHER_TC_SEGMENT_TYPE,
)
from lib.models import (
    UnalignedStream,
)
from oob_segment import OobSegment
from ptc_segment import PtcSegment


def decode(cs: str):
    decoder = Decoder(consent_string=cs)
    data = decoder.process()

    return data


class Decoder:
    def __init__(self, consent_string: str):
        self.consent_string: str = consent_string
        self.results = []

    @staticmethod
    def base64_to_stream(segment: str) -> UnalignedStream:
        encoded = (segment + "===").encode()
        source = BytesIO(base64.urlsafe_b64decode(encoded))

        return UnalignedStream(source)

    def obj_to_dict(self, obj):
        if not hasattr(obj, "__dict__"):
            return obj
        result = {}
        for key, val in obj.__dict__.items():
            if key.startswith("_"):
                continue
            element = []
            if isinstance(val, list):
                for item in val:
                    element.append(self.obj_to_dict(item))
            else:
                element = self.obj_to_dict(val)
            result[key] = element
        return result

    def process(self):
        core, *other_segments = self.consent_string.split(".")

        stream = self.base64_to_stream(core)

        try:
            obj = CoreSegment(stream)
        except Exception:
            raise Exception('Core: Incorrect consent string format.')
        self.results.append(self.obj_to_dict(obj))

        for segment in other_segments:
            stream = self.base64_to_stream(segment)
            segment_type = stream.segment_type

            if not isinstance(segment_type, int) and segment_type not in {0, 1, 2, 3}:
                raise ValueError(
                    f"segment_type: Unknown segment type. Expected int in range [0, 3], Got {stream.segment_type}."
                )

            if segment_type in OOB_SEGMENT_TYPES:
                try:
                    obj = OobSegment(stream)
                except Exception:
                    raise Exception('OOB: Incorrect consent string format.')

            if segment_type == PUBLISHER_TC_SEGMENT_TYPE:
                try:
                    obj = PtcSegment(stream)
                except Exception:
                    raise Exception('PTC: Incorrect consent string format.')

            self.results.append(self.obj_to_dict(obj))

        return self.results
