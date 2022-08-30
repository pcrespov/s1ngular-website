import json
from pathlib import Path

import segno
from segno import helpers


def main(basedir):
    #
    # https://segno.readthedocs.io/en/latest/contact-information.html
    #

    with open(basedir / "vcard.json") as fh:
        data = json.load(fh)

    vcard = helpers.make_vcard_data(**data)

    with open(basedir / "s1ngular.vcard", "wt") as fh:
        fh.write(vcard)

    qrcode = segno.make(vcard, error="H")

    qrcode.save(basedir / "qr_s1ngular.png")


if __name__ == "__main__":
    main(Path("./ignore.keep"))
