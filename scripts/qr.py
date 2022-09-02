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

    for name, url in [
        ("ytb_losgallardos", "https://youtu.be/ToriXXzdrqM"),
        ("ytb_tijola", "https://youtu.be/sMcGpewYT6Q"),
        ("ytb_mojacar", "https://youtu.be/sshzFr8bnow"),
        ("ytb_vera_80v", "https://youtu.be/YQZKpu6Nofo"),
        *zip(
            "web facebook youtube linkedin".split(),
            (
                "http://www.s1ngular.es/",
                "https://www.facebook.com/ingenierias1NGular/",
                "https://www.youtube.com/channel/UCh2u4MCFwSwHNANTmbWy2nw",
                "https://es.linkedin.com/in/alejandro-crespo-valero-2b764a35",
            ),
        ),
    ]:
        q = segno.make(url)
        q.save(basedir / f"{name}.pdf")

    q = segno.make("http://www.s1ngular.es", error="h")
    q.to_artistic(
        background="assets/s1ng-avatar.jpg", target=basedir / "s1nglogo.pdf", scale=10
    )


if __name__ == "__main__":
    main(Path("./ignore.keep"))
