import string

# Generate ISO 3166-1 alpha-2 codes with their index
ALPHA_MAPPING = {n: ch for n, ch in enumerate(string.ascii_lowercase)}

OOB_SEGMENT_TYPES = {1, 2}
PUBLISHER_TC_SEGMENT_TYPE = 3
