rule malicious_excel_file
{
    meta:
        description = "malicious_excel_file"
        author      = ""
        date        = "2023-04-06"

    strings:

        $rule0_bytes = { D0CF11E0A1B11AE1000000000000000000000000000000003E000300FEFF090006000000000000000000000001000000300000000000000000100000FE }

    condition:
        all of them
}
