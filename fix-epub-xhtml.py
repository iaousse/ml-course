import os
import re
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile


rendered_files = os.environ.get("QUARTO_PROJECT_OUTPUT_FILES", "").splitlines()
if not any(Path(name).suffix.lower() == ".epub" for name in rendered_files):
    raise SystemExit(0)

output_dir = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "docs"))
if not output_dir.is_absolute():
    output_dir = Path.cwd() / output_dir
epub_path = output_dir / "Machine-Learning.epub"
if not epub_path.is_file():
    raise SystemExit(0)

temporary_path = None
try:
    with tempfile.NamedTemporaryFile(
        dir=epub_path.parent, prefix=".Machine-Learning.", suffix=".epub", delete=False
    ) as temporary:
        temporary_path = Path(temporary.name)

    replacements = 0
    with ZipFile(epub_path, "r") as source:
        with ZipFile(temporary_path, "w") as destination:
            destination.comment = source.comment
            for info in source.infolist():
                content = source.read(info.filename)
                if info.filename.endswith(".xhtml"):
                    content, count = re.subn(
                        rb"(?<![\w:-])data-tabby-default(?=[\s/>])",
                        b'data-tabby-default=""',
                        content,
                    )
                    replacements += count
                destination.writestr(info, content)

    if replacements:
        with ZipFile(temporary_path, "r") as archive:
            if archive.testzip() is not None:
                raise RuntimeError("The repaired EPUB archive failed its ZIP integrity check.")
            for name in archive.namelist():
                if name.endswith(".xhtml"):
                    ET.fromstring(archive.read(name))
        os.replace(temporary_path, epub_path)
        print(f"Fixed {replacements} invalid XHTML tab attribute(s) in {epub_path.name}.")
    else:
        temporary_path.unlink()
except Exception:
    if temporary_path is not None:
        temporary_path.unlink(missing_ok=True)
    raise
