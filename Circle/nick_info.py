# Encoded By PyEncryptor
# A Product Of ToxicNoob
# https://github.com/Toxic-Noob

import marshal, base64, zlib

exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))