import base64

from kaitaistruct import BytesIO

from generated.core_segment import CoreSegment
from generated.oob_segment import OobSegment
from generated.ptc_segment import PtcSegment
from lib.models import (
    UnalignedStream,
)


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
        segments = self.consent_string.split(".")

        for segment in segments:
            stream = self.base64_to_stream(segment)
            segment_type = stream.segment_type

            if not isinstance(segment_type, int) and segment_type not in {0, 1, 2, 3}:
                raise ValueError(
                    f"segment_type: Unknown segment type. Expected int in range [0, 3], Got {stream.segment_type}."
                )

            try:
                obj = {
                    0: CoreSegment,
                    1: OobSegment,
                    2: OobSegment,
                    3: PtcSegment
                }[segment_type](stream)

            except Exception:
                raise Exception('Incorrect consent string format.')
            else:
                self.results.append(self.obj_to_dict(obj))

        return self.results
