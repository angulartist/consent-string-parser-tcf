meta:
  id: oob_segment
  title: 'Out-of-Band'
  endian: be
seq:
  - id: segment_type
    type: b3
  - id: vendor_consent
    type: vendor_section
types:
  vendor_section:
    seq:
      - id: max_vendor_id
        type: b16
      - id: is_range_encoding
        type: b1
      - id: bit_field
        type: b1
        repeat: expr
        repeat-expr: max_vendor_id
        if: not is_range_encoding
      - id: range_section
        type: range_section
        if: is_range_encoding
  range_section:
    seq:
      - id: num_entries
        type: b12
      - id: range_entries
        type: range_entry
        repeat: expr
        repeat-expr: num_entries
  range_entry:
    seq:
      - id: is_a_range
        type: b1
      - id: start_or_only_vendor_id
        type: b16
      - id: end_vendor_id
        type: b16
        if: is_a_range
