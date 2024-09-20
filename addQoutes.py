str =  """
{
  snapshot_context {
    snapshot_type: SNAPSHOT_TYPE_EOD
    business_date {
      year: 2013
      month: 12
      day: 18
    }
  }
  instrument_ids {
    unique_contract_id: 2
  }

}
"""

last = str[0]
out = ""
quote = '"'
for s in str[1:]:
    print(s)
    if s.isalpha():
        if not (last.isalpha() or last.isdigit() or last in "_:"  ) :
            out += quote

    if last.isalpha() or last.isdigit() or last in "_:":
        if not (s.isalpha() or s.isdigit() or s in "_:"  ) :
            out += quote

    out += s
    last = s
print (out)